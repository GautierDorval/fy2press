"""Discriminating negative tests for the documentary publication boundary."""
import copy, importlib.util, json, tempfile, shutil, unittest
from pathlib import Path
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
  self.mutate('artefacts/release-reference.json',lambda d:d['documentation'].update(published_at=None))
  with self.assertRaises(Exception):p.check(self.root)
 def test_publication_timestamp_must_be_valid(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentation'].update(published_at='2026-99-99T22:28:51Z'))
  with self.assertRaisesRegex(Exception,'date-time|invalid publication timestamp'):p.check(self.root)
 def test_release_link_must_match_tag(self):
  self.mutate('artefacts/release-reference.json',lambda d:d['documentation'].update(release_url='https://github.com/GautierDorval/fy2press/releases/tag/nonexistent'))
  with self.assertRaisesRegex(ValueError,'publication URL/version'):p.check(self.root)
 def test_local_entity_cannot_describe_published_reference(self):
  self.mutate('artefacts/repository-entity.jsonld',lambda d:d.update(creativeWorkStatus='Local publication candidate'))
  with self.assertRaisesRegex(ValueError,'publication entity'):p.check(self.root)
 def test_citation_must_identify_verified_edition(self):
  self.mutate('CITATION.cff',lambda d:d['preferred-citation'].update(version='docs-v1.0.0-rc.2'))
  with self.assertRaisesRegex(ValueError,'citation/publication'):p.check(self.root)
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
if __name__=='__main__':unittest.main()
