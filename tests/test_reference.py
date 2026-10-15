"""Discriminating negative tests for the documentary publication boundary."""
import copy, importlib.util, json, tempfile, shutil, unittest
from pathlib import Path
from jsonschema import ValidationError
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reference',ROOT/'scripts/reference.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
class BoundaryTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(prefix='fy2press-reference-test-');self.addCleanup(self.temp.cleanup)
  self.root=Path(self.temp.name)/'candidate';shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','.venv'))
 def load(self,path):return p.load(self.root,path)
 def save(self,path,data):(self.root/path).write_bytes(p.encoded(data))
 def mutate(self,path,fn):
  data=self.load(path);fn(data);self.save(path,data)
 def keep_translation_hash(self,source):
  self.mutate('artefacts/translation-map.json',lambda d:[t.update(source_sha256=p.digest((self.root/source).read_bytes())) for t in d['translations'] if t['source']==source])
 def test_future_observation_and_review_rejected(self):
  from datetime import datetime, timezone, timedelta
  future=datetime.now(timezone.utc)+timedelta(days=2)
  self.mutate('examples/morrowfield-observation.json',lambda d:d.update(observed_at=future.strftime('%Y-%m-%dT%H:%M:%SZ')))
  with self.assertRaisesRegex(ValueError,'future Morrowfield'):p.check(self.root)
  self.save('examples/morrowfield-observation.json',p.load(ROOT,'examples/morrowfield-observation.json'))
  self.mutate('artefacts/translation-map.json',lambda d:d['translations'][0].update(reviewed_on=future.strftime('%Y-%m-%d')))
  with self.assertRaisesRegex(ValueError,'future translation'):p.check(self.root)
 def test_other_empty_component_is_not_mislabeled(self):
  self.mutate('sources/developer-observation.json',lambda d:next(x for x in d['shortcodes'] if x['name']=='fy2press_product_vendor')['test'].update(output_bytes=0))
  for fr in [False,True]:
   text=p.dev_page(self.root,'shortcodes',fr).decode().split('## fy2press_product_vendor')[1].split('\n## ')[0]
   self.assertIn('**Sortie vide observée' if fr else '**Empty output observed',text)
   self.assertNotIn('compatibility-and-evidence.md',text)
   self.assertNotIn('Product-type display',text)
 def test_french_prose_preserves_identifiers_and_destinations(self):
  tick=chr(96);code=tick+'id=123; type:x'+tick
  source='Contexte: texte; [shortcodes](../developer/shortcodes.md) '+code+' https://example.invalid/a?x=1\n'+tick*3+'text\na:b; c?\n'+tick*3+'\n'
  source+='<!-- generated:claims -->\n![Image](../assets/picture.png)'
  result=p.french_prose(source)
  self.assertIn('<!-- generated:claims -->',result)
  self.assertIn('\n![Image](../assets/picture.png)',result)
  self.assertIn('Contexte\u00a0: texte\u00a0; [codes courts](../developer/shortcodes.md)',result)
  self.assertIn(code,result);self.assertIn('https://example.invalid/a?x=1',result)
  self.assertIn(tick*3+'text\na:b; c?\n'+tick*3,result)

 def test_current_confirmation_supersedes_local_not_run(self):
  manifest=self.load('sources/manifest-projection.json')
  confirmation=manifest['capability_observation']['current_validation']
  cap={'id':'sync.scheduled','implementation':'delivered'}
  self.assertEqual(p.current_validation(manifest,cap)['state'],'PUBLISHER_CONFIRMED')
  self.assertIn(confirmation['confirmed_by'],p.current_validation(manifest,cap)['scope'])
  manifest['capability_observation'].pop('current_validation')
  self.assertEqual(p.current_validation(manifest,cap)['state'],'NOT_RUN')
 def test_confirmation_cannot_invent_execution_or_independence(self):
  for key,value in [('test_execution_date','2026-10-15'),('tested_environment','all themes'),('independent_audit',True)]:
   with self.subTest(key=key):
    manifest=self.load('sources/manifest-projection.json')
    manifest['capability_observation']['current_validation'][key]=value
    with self.assertRaisesRegex(ValueError,'invent execution'):p.current_validation(manifest,{'id':'sync.scheduled','implementation':'delivered'})
 def test_confirmation_does_not_make_absent_or_unknown_features_available(self):
  manifest=self.load('sources/manifest-projection.json')
  original=copy.deepcopy(manifest)
  for state in ['absent','unknown',None]:
   self.assertEqual(p.current_validation(manifest,{'id':'builders.gutenberg','implementation':state})['state'],'NOT_RUN')
  self.assertEqual(manifest,original)

 def test_baseline(self):p.check(self.root)
 def test_source_modified_without_lock(self):
  self.mutate('sources/manifest-projection.json',lambda d:d['capability_observation']['capabilities'][0].update(implementation='absent'))
  with self.assertRaisesRegex(ValueError,'source hash drift'):p.check(self.root)
 def test_claim_drift(self):
  self.mutate('artefacts/claims.json',lambda d:d['claims'][0].update(implementation_status='absent'))
  with self.assertRaisesRegex(ValueError,'claim/source mismatch'):p.check(self.root)
 def test_unknown_is_not_false(self):
  self.mutate('sources/manifest-projection.json',lambda d:d['capability_observation']['capabilities'][0].update(implementation=None))
  claims=p.make_claims(self.root);self.assertIsNone(claims['claims'][0]['implementation_status'])
  self.assertNotEqual(claims['claims'][0]['implementation_status'],'absent')
 def test_unknown_package_match_not_false(self):
  self.mutate('sources/manifest-projection.json',lambda d:d['capability_observation'].update(source_matches_distributed_package=False))
  with self.assertRaisesRegex(ValueError,'source hash drift'):p.check(self.root)
 def test_invalid_state_rejected(self):
  self.mutate('artefacts/claims.json',lambda d:d['claims'][0].update(implementation_status='excellent'))
  with self.assertRaises(Exception) as ctx:p.check(self.root)
  self.assertIn('excellent',str(ctx.exception))
 def test_partial_requires_specific_limit(self):
  self.mutate('artefacts/claims.json',lambda d:d['claims'][2].update(limitations=[]))
  with self.assertRaisesRegex(ValueError,'claim/source mismatch'):p.check(self.root)
 def test_policy_not_software_maturity(self):
  self.mutate('artefacts/claims.json',lambda d:d['claims'][0].update(policy_status='proposed'))
  with self.assertRaises(Exception) as ctx:p.check(self.root)
  self.assertIn('null',str(ctx.exception))
 def test_wrong_edition(self):
  self.mutate('artefacts/claims.json',lambda d:d['claims'][0].update(edition='PRO'))
  with self.assertRaisesRegex(ValueError,'claim/source mismatch'):p.check(self.root)
 def test_wrong_package(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['FREE'].update(zip_sha256='a'*64))
  with self.assertRaisesRegex(ValueError,'edition/package mix'):p.check(self.root)
 def test_digest_prefix_refused(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['FREE'].update(zip_sha256='ef6c0a38fef2'))
  with self.assertRaises(Exception) as ctx:p.check(self.root)
  self.assertIn('64',str(ctx.exception))
 def test_translation_stale(self):
  with (self.root/'README.md').open('a',encoding='utf-8') as f:f.write('\nChanged source prose.\n')
  with self.assertRaisesRegex(ValueError,'stale translation'):p.check(self.root)
 def test_translation_target_changed(self):
  with (self.root/'fr-ca/README.md').open('a',encoding='utf-8') as f:f.write('\nTexte modifié.\n')
  with self.assertRaisesRegex(ValueError,'stale translation'):p.check(self.root)
 def test_broken_link(self):
  with (self.root/'README.md').open('a',encoding='utf-8') as f:f.write('\n[Missing](missing-document.md)\n')
  self.keep_translation_hash('README.md')
  with self.assertRaisesRegex(ValueError,'broken or escaped local link'):p.check(self.root)
 def test_fragment_only_links_work_with_noncanonical_root(self):
  p.check(self.root/'..'/'candidate')
 def test_broken_anchor(self):
  with (self.root/'README.md').open('a',encoding='utf-8') as f:f.write('\n[Missing](scope.md#nonexistent-heading)\n')
  self.keep_translation_hash('README.md')
  with self.assertRaisesRegex(ValueError,'broken anchor'):p.check(self.root)
 def test_extra_file(self):
  (self.root/'unselected.txt').write_text('synthetic')
  with self.assertRaisesRegex(ValueError,'outside explicit publication'):p.export_manifest(self.root)
 def test_package_refused(self):
  (self.root/'package.zip').write_bytes(b'fictional archive')
  with self.assertRaisesRegex(ValueError,'package or excluded'):p.export_manifest(self.root)
 def test_fake_secret_refused(self):
  with (self.root/'README.md').open('a') as f:f.write('\n'+'gh'+'p_'+'A'*36)
  with self.assertRaisesRegex(ValueError,'sensitive pattern'):p.export_manifest(self.root)
 def test_private_path_refused(self):
  with (self.root/'README.md').open('a') as f:f.write('\n'+'C:'+chr(92)+'Users'+chr(92)+'Synthetic'+chr(92)+'private')
  with self.assertRaisesRegex(ValueError,'sensitive pattern'):p.export_manifest(self.root)
 def test_private_repository_link_refused(self):
  with (self.root/'README.md').open('a') as f:f.write('\nhttps://github.com/'+'GautierDorval/'+'fy2press-'+'plugin/blob/main/file')
  with self.assertRaisesRegex(ValueError,'private repository link'):p.export_manifest(self.root)
 def test_traversal_refused(self):
  with self.assertRaisesRegex(ValueError,'path traversal'):p.safe_path(self.root,'../private.txt')
 def test_symlink_refused(self):
  target=Path(self.temp.name)/'outside';target.write_text('synthetic')
  try:(self.root/'linked.txt').symlink_to(target)
  except OSError as e:self.skipTest('OS symlink privilege unavailable: '+type(e).__name__)
  with self.assertRaisesRegex(ValueError,'symlink'):p.export_manifest(self.root)
 def test_unavailable_preserves_data(self):
  before=(self.root/'artefacts/claims.json').read_bytes()
  def unavailable(url):raise OSError('synthetic network outage')
  result=p.upstream(self.root,unavailable)
  self.assertTrue(all(x['state']=='UNAVAILABLE' for x in result));self.assertEqual(before,(self.root/'artefacts/claims.json').read_bytes())
 def test_readme_change_same_version_detected(self):
  lock={s['id']:s for s in self.load('artefacts/source-lock.json')['sources']}
  def changed(url):
   key=next(k for k,v in p.URLS.items() if v==url)
   if key=='wordpress':return p.encoded(self.load('sources/wordpress-projection.json'))
   return b'changed bytes at the same version'
  result=p.upstream(self.root,changed)
  self.assertEqual(next(x for x in result if x['source']=='developer')['state'],'DRIFT_DETECTED')
  self.assertEqual(self.load('artefacts/release-reference.json')['FREE']['version'],'1.0.0')
 def test_unapproved_url_refused(self):
  with self.assertRaisesRegex(ValueError,'allowlist'):p.fetch('https://example.invalid/private')
 def test_edition_table_drift(self):
  file=self.root/'docs/editions-and-integrations.md';file.write_text(file.read_text(encoding='utf-8').replace('Connect one Shopify store','Connect unlimited stores'),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'generated drift'):p.generate(self.root,True)
 def test_deterministic_generation(self):
  first=p.generated(self.root);p.generate(self.root);second=p.generated(self.root);self.assertEqual(first,second)
 def test_untrusted_ci_refused(self):
  path=self.root/'.github/workflows/validate.yml';path.write_text(path.read_text(encoding='utf-8').replace('pull_request:','pull_request_target:'),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'unsafe workflow surface'):p.check(self.root)
 def test_runner_refused(self):
  path=self.root/'.github/workflows/validate.yml';path.write_text(path.read_text(encoding='utf-8').replace('ubuntu-latest','self-hosted'),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'unsafe workflow surface'):p.check(self.root)
 def test_write_permission_refused(self):
  path=self.root/'.github/workflows/validate.yml';path.write_text(path.read_text(encoding='utf-8').replace('contents: read','contents: write'),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'workflow permissions'):p.check(self.root)
 def test_source_precedence_allows_contradiction(self):
  precedence=self.load('artefacts/source-precedence.json')
  self.assertEqual(precedence['by_question']['behaviour'][0],'identified distributed package')
  self.assertIn('A manifest does not invalidate reproducible contrary behaviour.',precedence['rules'])
 def git(self,*args):
  import subprocess
  return subprocess.check_output(['git','-C',str(self.root),*args],text=True,encoding='utf-8')
 def init_history(self):
  self.git('init','-b','main');self.git('add','--',*self.load('publication-files.json')['files'])
  self.git('-c','user.name=Synthetic Test','-c','user.email=test@example.invalid','commit','-m','Synthetic documentary root')
 def test_fresh_history(self):
  self.init_history();self.assertEqual(len(p.check_history(self.root)),1)
 def test_unreachable_imported_history_object(self):
  self.init_history()
  extra=Path(self.temp.name)/'synthetic-private.txt';extra.write_text('synthetic private history',encoding='utf-8')
  self.git('hash-object','-w',str(extra))
  with self.assertRaisesRegex(ValueError,'unreachable or imported'):p.check_history(self.root)
 def test_historical_excluded_blob(self):
  self.init_history();(self.root/'private-fixture.txt').write_text('synthetic',encoding='utf-8')
  self.git('add','private-fixture.txt');self.git('-c','user.name=Synthetic Test','-c','user.email=test@example.invalid','commit','-m','Synthetic forbidden object')
  with self.assertRaisesRegex(ValueError,'unapproved historical'):p.check_history(self.root)
 def test_published_release_requires_date(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentary_publications'][0].update(published_at=None))
  with self.assertRaisesRegex(ValidationError,"None is not of type 'string'"):p.check(self.root)
 def test_publication_timestamp_must_be_valid(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentary_publications'][0].update(published_at='2026-99-99T22:28:51Z'))
  with self.assertRaisesRegex(Exception,'date-time|invalid publication timestamp'):p.check(self.root)
 def test_release_link_must_match_tag(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentary_publications'][0].update(release_url='https://github.com/GautierDorval/fy2press/releases/tag/nonexistent'))
  with self.assertRaisesRegex(ValueError,'publication URL/version'):p.check(self.root)
 def test_local_entity_cannot_describe_published_reference(self):
  self.mutate('artefacts/repository-entity.jsonld',lambda d:d.update(creativeWorkStatus='Local publication candidate'))
  with self.assertRaisesRegex(ValueError,'edition entity'):p.check(self.root)
 def test_citation_must_identify_current_edition(self):
  self.mutate('CITATION.cff',lambda d:d['preferred-citation'].update(version='docs-v1.0.0-rc.1'))
  with self.assertRaisesRegex(ValueError,'citation/edition'):p.check(self.root)
 def test_edition_cannot_claim_provider_receipt_fields(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentation'].update(published_at='2026-10-14T22:28:51Z'))
  with self.assertRaisesRegex(ValidationError,'Additional properties'):p.check(self.root)
 def test_edition_link_must_match_version(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentation'].update(release_url='https://github.com/GautierDorval/fy2press/releases/tag/docs-v1.0.0-rc.1'))
  with self.assertRaisesRegex(ValueError,'edition URL/version'):p.check(self.root)
 def test_source_lock_must_name_current_edition(self):
  self.mutate('artefacts/source-lock.json',lambda d:d.update(documentation_version='docs-v1.0.0-rc.1'))
  with self.assertRaisesRegex(ValueError,'source-lock/edition'):p.check(self.root)
 def test_unverified_citation_date_refused(self):
  self.mutate('CITATION.cff',lambda d:d.update(**{'date-released':'2026-10-14'}))
  with self.assertRaisesRegex(ValueError,'citation date requires'):p.check(self.root)
 def test_unverified_entity_date_refused(self):
  self.mutate('artefacts/repository-entity.jsonld',lambda d:d.update(datePublished='2026-10-14T22:28:51Z'))
  with self.assertRaisesRegex(ValueError,'publication date belongs'):p.check(self.root)
 def test_duplicate_publication_receipt_refused(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentary_publications'].append(copy.deepcopy(d['documentary_publications'][0])))
  with self.assertRaisesRegex(ValueError,'duplicate publication'):p.check(self.root)
 def test_future_publication_receipt_refused(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentary_publications'][0].update(published_at='2099-01-01T00:00:00Z'))
  with self.assertRaisesRegex(ValueError,'future publication'):p.check(self.root)
 def test_matching_current_edition_receipt_is_supported(self):
  # Synthetic receipt in the disposable fixture only; not a publication assertion.
  ref=self.load('artefacts/release-reference.json');receipt=copy.deepcopy(ref['documentary_publications'][0])
  receipt.update(version=ref['documentation']['version'],release_url=ref['documentation']['release_url'])
  ref['documentary_publications'].append(receipt);self.save('artefacts/release-reference.json',ref)
  path=self.root/'CHANGELOG.md';text=path.read_text(encoding='utf-8')
  text=text.replace('## '+receipt['version']+'\n','## '+receipt['version']+' (published '+receipt['published_at'][:10]+')\n')
  path.write_text(text,encoding='utf-8')
  cff=self.load('CITATION.cff')
  for record in [cff,cff['preferred-citation']]:record['date-released']=receipt['published_at'][:10]
  self.save('CITATION.cff',cff);p.check(self.root)
  cff['preferred-citation']['date-released']='2026-10-13';self.save('CITATION.cff',cff)
  with self.assertRaisesRegex(ValueError,'citation date requires'):p.check(self.root)
 def test_readme_edition_disagreement_refused(self):
  for name in ['README.md','fr-ca/README.md']:
   with self.subTest(readme=name):
    path=self.root/name;original=path.read_text(encoding='utf-8')
    path.write_text(original.replace('docs-v1.0.0-rc.2','docs-v1.0.0-rc.1'),encoding='utf-8')
    mapping=self.load('artefacts/translation-map.json')
    for row in mapping['translations']:
     if row['source']=='README.md':
      row['source_sha256']=p.digest((self.root/row['source']).read_bytes())
      row['translation_sha256']=p.digest((self.root/row['translation']).read_bytes())
    self.save('artefacts/translation-map.json',mapping)
    with self.assertRaisesRegex(ValueError,'README/edition disagreement'):p.check(self.root)
    path.write_text(original,encoding='utf-8')
    self.save('artefacts/translation-map.json',p.load(ROOT,'artefacts/translation-map.json'))
 def test_readme_release_link_missing_refused(self):
  path=self.root/'README.md';text=path.read_text(encoding='utf-8')
  text=text.replace(self.load('artefacts/release-reference.json')['documentation']['release_url'],'https://github.com/GautierDorval/fy2press/releases')
  path.write_text(text,encoding='utf-8');self.keep_translation_hash('README.md')
  with self.assertRaisesRegex(ValueError,'README/edition disagreement'):p.check(self.root)
 def test_changed_example_requires_new_browser_observation(self):
  with (self.root/'examples/morrowfield.html').open('a',encoding='utf-8') as f:f.write('<!-- changed -->')
  with self.assertRaisesRegex(ValueError,'stale Morrowfield browser'):p.check(self.root)
 def test_changed_screenshot_requires_new_observation(self):
  (self.root/'assets/morrowfield-collection-en.png').write_bytes(b'changed screenshot')
  with self.assertRaisesRegex(ValueError,'stale Morrowfield screenshot'):p.check(self.root)
 def test_malformed_citation(self):
  self.mutate('CITATION.cff',lambda d:d.update(authors=27))
  with self.assertRaises(Exception):p.check(self.root)
 def test_junction_refused(self):
  import os,subprocess
  if os.name!='nt':self.skipTest('Windows junction test')
  outside=Path(self.temp.name)/'outside-directory';outside.mkdir()
  link=self.root/'linked-directory'
  command="New-Item -ItemType Junction -Path '"+str(link).replace("'","''")+"' -Target '"+str(outside).replace("'","''")+"' | Out-Null"
  subprocess.run(['pwsh','-NoProfile','-Command',command],check=True,capture_output=True)
  try:
   with self.assertRaisesRegex(ValueError,'linked directory'):p.export_manifest(self.root)
  finally:link.rmdir()

 def rehash_html(self):
  self.mutate('examples/morrowfield-observation.json',lambda d:d.update(source_sha256=p.digest((self.root/'examples/morrowfield.html').read_bytes())))
 def test_capture_cannot_be_unbound(self):
  self.mutate('examples/morrowfield-observation.json',lambda d:d['views'][0].update(screenshot=None))
  (self.root/'assets/morrowfield-collection-en.png').write_bytes(b'not a png')
  with self.assertRaisesRegex(ValueError,'Morrowfield screenshot coverage'):p.check(self.root)
 def test_empty_or_duplicate_views_refused(self):
  original=self.load('examples/morrowfield-observation.json')
  for views in [[],original['views'][:-1]+[original['views'][0]]]:
   with self.subTest(views=len(views)):
    changed=copy.deepcopy(original);changed['views']=views;self.save('examples/morrowfield-observation.json',changed)
    with self.assertRaisesRegex(ValueError,'Morrowfield view coverage'):p.check(self.root)
 def test_failed_observation_refused(self):
  for field,value in [('state','FAIL'),('visual_inspection',{'state':'PENDING'}),('visual_inspection','PASS')]:
   with self.subTest(field=field,value=value):
    original=self.load('examples/morrowfield-observation.json');changed=copy.deepcopy(original);changed[field]=value;self.save('examples/morrowfield-observation.json',changed)
    with self.assertRaisesRegex(ValueError,'incomplete Morrowfield observation'):p.check(self.root)
    self.save('examples/morrowfield-observation.json',original)
 def test_invalid_observation_dates_refused(self):
  for value in [None,'not-a-date','2026-02-30T12:00:00Z','2026-10-15T24:00:00Z','2026-10-15']:
   with self.subTest(value=value):
    self.mutate('examples/morrowfield-observation.json',lambda d:d.update(observed_at=value))
    with self.assertRaisesRegex(ValueError,'invalid Morrowfield observation timestamp'):p.check(self.root)
 def test_failed_browser_or_view_refused(self):
  original=self.load('examples/morrowfield-observation.json')
  for field,value in [('external_request_attempts',1),('uncaught_javascript_errors',False),('direct_file_navigation_pass',False)]:
   with self.subTest(field=field):
    changed=copy.deepcopy(original);changed[field]=value;self.save('examples/morrowfield-observation.json',changed)
    with self.assertRaisesRegex(ValueError,'failed Morrowfield browser checks'):p.check(self.root)
  self.save('examples/morrowfield-observation.json',original)
  self.mutate('examples/morrowfield-observation.json',lambda d:d['views'][0].update(horizontal_overflow=True))
  with self.assertRaisesRegex(ValueError,'failed Morrowfield view'):p.check(self.root)
 def test_missing_journey_refused(self):
  self.mutate('examples/morrowfield-observation.json',lambda d:d.update(journeys=[]))
  with self.assertRaisesRegex(ValueError,'Morrowfield journey coverage'):p.check(self.root)
 def test_rehashed_corrupt_png_refused(self):
  content=b'not a PNG';(self.root/'assets/morrowfield-collection-en.png').write_bytes(content)
  self.mutate('examples/morrowfield-observation.json',lambda d:d['views'][0].update(screenshot_sha256=p.digest(content)))
  with self.assertRaisesRegex(ValueError,'invalid Morrowfield PNG'):p.check(self.root)
 def test_false_capture_dimensions_refused(self):
  self.mutate('examples/morrowfield-observation.json',lambda d:d['views'][0]['capture_dimensions'].update(height=9999))
  with self.assertRaisesRegex(ValueError,'Morrowfield capture dimensions'):p.check(self.root)
 def test_rehashed_missing_html_link_refused(self):
  path=self.root/'examples/morrowfield.html';path.write_text(path.read_text(encoding='utf-8').replace("'morrowfield.md'","'missing-case.md'"),encoding='utf-8');self.rehash_html()
  with self.assertRaisesRegex(ValueError,'broken Morrowfield HTML link'):p.check(self.root)
 def test_rehashed_noindex_removal_refused(self):
  path=self.root/'examples/morrowfield.html';path.write_text(path.read_text(encoding='utf-8').replace('noindex,nofollow','index,follow'),encoding='utf-8');self.rehash_html()
  with self.assertRaisesRegex(ValueError,'Morrowfield noindex/nofollow required'):p.check(self.root)
 def test_external_html_resource_refused(self):
  path=self.root/'examples/morrowfield.html';path.write_text(path.read_text(encoding='utf-8').replace('</body>','<img src="https://example.invalid/image.png"></body>'),encoding='utf-8');self.rehash_html()
  with self.assertRaisesRegex(ValueError,'Morrowfield external URL'):p.check(self.root)
 def test_licence_inventory_refused(self):
  self.mutate('CITATION.cff',lambda d:d.update(license='CC-BY-4.0'))
  with self.assertRaisesRegex(ValueError,'documentation licence inventory'):p.check(self.root)
 def test_changelog_date_disagreement_refused(self):
  path=self.root/'CHANGELOG.md';path.write_text(path.read_text(encoding='utf-8').replace('(published 2026-10-14)','(published 2026-10-15)'),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'changelog/publication disagreement'):p.check(self.root)

if __name__=='__main__':unittest.main()
