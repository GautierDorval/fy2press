"""Original documentation pipeline. Network commands are opt-in and read-only by default."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, urllib.request, urllib.error, zipfile
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1]
URLS = {
 'manifest': 'https://fy2press.com/ai-manifest.json',
 'release': 'https://fy2press.com/governance/release-state.json',
 'policy': 'https://fy2press.com/governance/claim-rules.json',
 'wordpress': 'https://api.wordpress.org/plugins/info/1.2/?action=plugin_information&request[slug]=fy2press',
 'developer': 'https://downloads.wordpress.org/plugin/fy2press.1.0.0.zip',
}
def require(ok, message):
 if not ok: raise ValueError(message)
def digest(data): return hashlib.sha256(data).hexdigest()
def load(root, path): return json.loads((root/path).read_text(encoding='utf-8'))
def encoded(obj): return (json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()
def safe_path(root, rel):
 require(isinstance(rel,str) and rel and not any(x in rel for x in ('\\',':','\x00')),'unsafe path')
 p=Path(rel);require(not p.is_absolute() and '..' not in p.parts,'path traversal')
 dest=root/p
 for q in [dest,*dest.parents]:
  if q==root.parent:break
  require(not q.is_symlink() and not getattr(q,'is_junction',lambda:False)(),'symlink or junction')
 require(dest.resolve().is_relative_to(root.resolve()),'escaped root')
 return dest

def source_checks(root):
 lock=load(root,'artefacts/source-lock.json');ids=set()
 for s in lock['sources']:
  require(s['id'] not in ids,'duplicate source');ids.add(s['id'])
  require(s['url']==URLS[s['id']],'unapproved source URL')
  require(re.fullmatch('[0-9a-f]{64}',s['raw_sha256']) is not None,'incomplete raw digest')
  p=safe_path(root,s['retained_path']);require(digest(p.read_bytes())==s['retained_sha256'],'retained source hash drift: '+s['id'])
 manifest=load(root,'sources/manifest-projection.json')
 seen=set()
 for cap in manifest['capability_observation']['capabilities']:
  require(cap['id'] not in seen,'duplicate capability');seen.add(cap['id'])
  require(cap['edition'] in ['FREE','PRO'],'unknown edition')
  require(cap.get('implementation') in ['delivered','partial','absent','unknown',None],'unknown implementation enum')
  require('implementation' in cap,'missing implementation is not null')
 require(manifest['capability_observation']['source_matches_distributed_package'] is None,'unproven package match')
 return lock

def make_claims(root):
 manifest=load(root,'sources/manifest-projection.json');ed=load(root,'sources/capability-editorial.json')['entries'];claims=[]
 caps=manifest['capability_observation']['capabilities']
 require(set(ed)=={x['id'] for x in caps},'editorial mapping coverage')
 for i,cap in enumerate(caps):
  t=ed[cap['id']]
  claims.append({'id':cap['id'],'subject':'Fy2Press','edition':cap['edition'],'version':manifest['capability_observation']['documented_version'],'statement_en':t['statement_en'],'statement_fr_ca':t['statement_fr_ca'],'implementation_status':cap['implementation'],'behaviour':t['statement_en'],'limitations':[t['limit_en'],t['limit_fr_ca']],'source_refs':[{'source_id':'manifest','pointer':f'/capability_observation/capabilities/{i}'}],'validation':{'state':'LOCAL_COMPONENT_OBSERVATION' if cap['id'] in ['builders.gutenberg','builders.prefixed_shortcodes'] else 'NOT_RUN','scope':'Native FREE registry and local callback examples only' if cap['id'] in ['builders.gutenberg','builders.prefixed_shortcodes'] else 'Publisher description; not a new runtime qualification'},'policy_status':None})
 return {'schema_version':'1.0.0','claims':claims}

def md_value(v):return json.dumps(v,ensure_ascii=False,separators=(',',':')).replace('|','&#124;').replace('`','&#96;')
COMPONENT_PURPOSES = {'product': ('A complete product component for the supplied WordPress product ID.',
             'Un composant produit complet pour l’ID de fiche WordPress fourni.'),
 'product_title': ('The product title.', 'Le titre du produit.'),
 'product_description': ('The product description in the current product context.',
                         'La description du produit dans le contexte courant.'),
 'product_price': ('The formatted product price from the available product data.',
                   'Le prix formaté selon les données produit disponibles.'),
 'product_image': ('The main product image.', 'L’image principale du produit.'),
 'product_url': ('A scalar product URL by default, or an HTML link with format="link".',
                 'Une URL produit scalaire par défaut, ou un lien HTML avec format="link".'),
 'product_vendor': ('The product vendor label.', 'Le nom du fournisseur du produit.'),
 'product_type': ('The product type when available; the inspected FREE 1.0.0 data path has a field-name mismatch. See the compatibility notes.',
                  'Le type de produit lorsqu’il est disponible ; le parcours FREE 1.0.0 examiné comporte une incohérence de nom de champ. Consultez les notes de compatibilité.'),
 'product_tags': ('The product’s tag list.', 'La liste des étiquettes du produit.'),
 'product_gallery': ('The product image gallery.', 'La galerie d’images du produit.'),
 'product_availability': ('The availability label from the available product data.',
                          'L’indication de disponibilité selon les données produit disponibles.'),
 'product_variants': ('Variant-selection controls in a product context.',
                      'Les contrôles de choix de variante dans un contexte produit.'),
 'product_collections': ('The collections associated with the product.',
                         'Les collections associées au produit.'),
 'add_to_cart': ('An add-to-cart control; a returned control alone does not prove a cart request.',
                 'Un contrôle d’ajout au panier; son rendu seul ne prouve pas une requête panier.'),
 'buy_now': ('A direct-purchase control; connected checkout is outside this local observation.',
             'Un contrôle d’achat direct; le paiement connecté est hors de cette observation locale.'),
 'related_products': ('A list of related products when the context supplies them.',
                      'Une liste de produits associés lorsque le contexte les fournit.'),
 'collection': ('A collection component for the supplied collection handle.',
                'Un composant collection pour le handle fourni.'),
 'products_loop': ('A product grid with the configured limit, columns and collection.',
                   'Une grille de produits selon la limite, les colonnes et la collection configurées.'),
 'collection_title': ('The current collection title.', 'Le titre de la collection courante.'),
 'collection_description': ('The current collection description.',
                            'La description de la collection courante.'),
 'collection_sort': ('A sorting control for the collection’s product results.',
                     'Un contrôle de tri des résultats produit de la collection.'),
 'product_search': ('A search field associated with a products loop.',
                    'Un champ de recherche associé à une boucle de produits.'),
 'collection_filter': ('A collection-selection filter associated with a products loop.',
                       'Un filtre de collection associé à une boucle de produits.'),
 'tag_filter': ('A tag filter using its declared defaults or saved design type.',
                'Un filtre d’étiquettes selon ses valeurs déclarées ou le type du design enregistré.'),
 'filter_sidebar': ('A filter panel for a compatible products-loop context.',
                    'Un panneau de filtres pour un contexte de boucle compatible.'),
 'price_filter': ('A price filter for the associated product results.',
                  'Un filtre de prix pour les résultats produit associés.'),
 'availability_filter': ('An availability filter for the associated product results.',
                         'Un filtre de disponibilité pour les résultats produit associés.'),
 'collection_products_per_page': ('A control for the number of products displayed per collection page.',
                                  'Un contrôle du nombre de produits affichés par page de collection.')}

def component_purpose(entry, kind, fr):
 key=entry["name"].removeprefix("fy2press_") if kind=="shortcodes" else entry["name"].split("/",1)[1].replace("-","_")
 if kind=="blocks" and key in {"title","price","description","image","variants","gallery","availability","vendor","collections","tags"}:key="product_"+key
 require(key in COMPONENT_PURPOSES,"missing editorial component purpose")
 return COMPONENT_PURPOSES[key][int(fr)]

def french_prose(text):
 # Preserve fenced code, inline identifiers, link destinations and URLs.
 tick=chr(96)
 pattern=r"(?ms)(^"+tick*3+r".*?^"+tick*3+r"[^\n]*(?:\n|$)|"+tick+r"[^"+tick+r"\n]*"+tick+r"|\]\([^)]+\)|https?://[^\s<>]+|<[^>]+>)"
 parts=re.split(pattern,text)
 for i in range(0,len(parts),2):
  parts[i]=re.sub(r"[ \u00a0\u202f]*([;:?]|!(?!\[))",lambda m:"\u00a0"+m[1],parts[i])
  parts[i]=re.sub(r"\b[Ss]hortcodes?\b",lambda m:("Codes courts" if m[0][0].isupper() else "codes courts") if m[0].endswith("s") else ("Code court" if m[0][0].isupper() else "code court"),parts[i])
 return "".join(parts)

def dev_page(root,kind,fr):
 data=load(root,'sources/developer-observation.json');prefix='../../' if fr else '../'
 title=('Blocs Gutenberg' if kind=='blocks' else 'Shortcodes publics') if fr else ('Gutenberg blocks' if kind=='blocks' else 'Public shortcodes')
 other=('../'+prefix if False else '')
 switch=('../../developer/'+kind+'.md') if fr else ('../fr-ca/developer/'+kind+'.md')
 s=f'# {title}\n\n'+('[English]' if fr else '[Français canadien]')+f'({switch}) · [Index](README.md)\n\n'
 s+=('Généré depuis le registre WordPress natif du paquet FREE 1.0.0, SVN 3744276. Les résultats ci-dessous proviennent de données fictives locales, sans requête Shopify. Les valeurs par défaut sont celles du laboratoire en anglais; les textes traduisibles peuvent différer selon la langue.\n' if fr else 'Generated from the native WordPress registry of FREE 1.0.0, SVN 3744276. Results below use fictional local data without Shopify requests. Defaults reflect the English lab locale; translatable strings can vary by locale.\n')
 s+=('\nLes exemples avec `id="123"` exigent l’ID WordPress réel. Les blocs produit exigent normalement une fiche produit; les blocs collection exigent une archive de collection. Une boucle peut être placée sur une page ordinaire.\n' if fr else '\nExamples with `id="123"` require the real WordPress post ID. Product blocks normally need a product page; collection blocks need a collection archive. A products loop can be placed on an ordinary page.\n')
 for x in data[kind]:
  s+='\n## '+x['name']+'\n\n'
  s+=('Résultat attendu' if fr else 'Expected result')+': '+component_purpose(x,kind,fr)+'\n\n'
  s+=('Contexte' if fr else 'Context')+': `'+x['context']+'`. FREE '+x['version']+'. '
  if kind=='shortcodes':s+=('Alias de compatibilité' if fr else 'Compatibility alias')+': `'+x['alias']+'`. '
  url='https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/'+x['source']
  s+='[Source]('+url+').\n\n```'+('html' if kind=='blocks' else 'text')+'\n'+x['example']+'\n```\n\n'
  test=x['test'];n=test['output_bytes']
  result=('HTML retourné' if kind=='blocks' else {'HTML string':'chaîne HTML','URL by default; HTML with format=link':'URL par défaut; HTML avec format=link'}[x['result_kind']]) if fr else ('Returned HTML' if kind=='blocks' else x['result_kind'])
  s+='<details>\n<summary>'+('Détails de l’essai local' if fr else 'Local test details')+'</summary>\n\n'+('Trace de l’essai local' if fr else 'Local test trace')+f': {n} '+('octets retournés' if fr else 'returned bytes')+f', {test["echo_bytes"]} '+('octets imprimés hors retour' if fr else 'bytes echoed outside the return')+'. '+result+'.\n\n</details>\n\n'
  if not n:
   s+=('**Sortie vide observée ; affichage rempli non démontré.**' if fr else '**Empty output observed; populated display is not demonstrated.**')
   if x['name']=='fy2press_product_type':s+=(' [Limite connue]' if fr else ' [Known limitation]')+'(../docs/compatibility-and-evidence.md).'
   s+='\n\n'
  if x['name']=='fy2press_product_url':s+=('`format="url"` retourne une URL scalaire; `format="link"` retourne un lien HTML. Les deux modes ont été exécutés. Sans produit, le code peut retourner une URL illustrative; toujours fournir un contexte valide.\n\n' if fr else '`format="url"` returns a scalar URL; `format="link"` returns an HTML link. Both modes were executed. Without a product the code can return an illustrative URL; always supply valid context.\n\n')
  if 'dynamic_defaults' in x:s+=('Défaut dynamique : le type du filtre d’étiquettes vient du design sauvegardé valide; sinon `tags`.\n\n' if fr else 'Dynamic default: tag-filter type follows a valid saved design setting; otherwise `tags`.\n\n')
  s+='| '+('Attribut | Type | Défaut / contrat' if fr else 'Attribute | Type | Default / contract')+' |\n| --- | --- | --- |\n'
  attrs=x['attributes'] if kind=='blocks' else x['defaults']
  require(isinstance(attrs,dict),'unextracted defaults')
  for key,v in attrs.items():
   if kind=='blocks':typ=v.get('type','unspecified');default=v['default'] if 'default' in v else {'default_not_declared':True}
   else:typ=type(v).__name__;default=v
   s+='| `'+key+'` | '+str(typ)+' | `'+md_value(default)+'` |\n'
  if kind=='blocks':s+='\n'+('Supports inscrits' if fr else 'Registered supports')+':\n\n```json\n'+json.dumps(x['supports'],ensure_ascii=False,indent=2)+'\n```\n'
  s+='\n'+('Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.\n' if fr else 'Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.\n')
 s+='\n[Observation]('+prefix+'sources/developer-observation.json) · [Package]('+prefix+'artefacts/release-reference.json).\n'
 return (french_prose(s) if fr else s).encode()

def generated(root):
 claims=make_claims(root);out={'artefacts/claims.json':encoded(claims)}
 for fr in (False,True):
  pre='fr-ca/' if fr else '';key='statement_fr_ca' if fr else 'statement_en'
  table='| '+('Usage | Édition | État de l’éditeur | Limite' if fr else 'Use | Edition | Publisher state | Limit')+' |\n| --- | --- | --- | --- |\n'
  for c in claims['claims']:
   value=c['implementation_status'];state=('inconnu' if fr else 'unknown') if value is None else value
   if fr:state={'delivered':'livré','partial':'partiel','absent':'absent','unknown':'inconnu'}.get(state,state)
   table+='| '+c[key]+' | '+c['edition']+' | '+state+' | '+c['limitations'][int(fr)]+' |\n'
  path=pre+'docs/editions-and-integrations.md';text=(root/path).read_text(encoding='utf-8')
  pattern=r'(?s)<!-- generated:claims -->.*?<!-- /generated:claims -->'
  require(len(re.findall(pattern,text))==1,'missing generated table marker')
  page=re.sub(pattern,'<!-- generated:claims -->\n'+table+'<!-- /generated:claims -->',text)
  out[path]=(french_prose(page) if fr else page).encode()
  for kind in ['blocks','shortcodes']:out[pre+'developer/'+kind+'.md']=dev_page(root,kind,fr)
 return out

def generate(root,check=False):
 source_checks(root)
 for path,data in generated(root).items():
  p=root/path
  if check:require(p.is_file() and p.read_bytes()==data,'generated drift: '+path)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)

SECRETS=[re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}'),re.compile(r'github_pat_[A-Za-z0-9_]{35,}'),re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),re.compile(r'(?i)(?:C:|D:)[\\/]Users[\\/][^\s]+'),re.compile(r'(?i)(?:shopify|freemius|cloudflare)[_-](?:secret|token|api_key)\s*[:=]\s*[\"\x27][A-Za-z0-9_-]{20,}')]
def scan(data,name):
 text=data.decode('utf-8',errors='replace')
 require(not any(p.search(text) for p in SECRETS),'sensitive pattern in '+name)
 require(not re.search(r'https://(?:github\.com|api\.github\.com/repos)/GautierDorval/(?:fy2press-plugin|fy2press-site|pagup-internal-docs)(?:[/#?\s\"]|$)',text),'private repository link in '+name)
 require(('version '+'https://git-lfs.github.com/spec/v1') not in text,'LFS pointer')

def inventory(root):
 actual=[]
 for base,dirs,files in os.walk(root,followlinks=False):
  for d in list(dirs):
   p=Path(base)/d
   if p==root/'.git':dirs.remove(d);continue
   require(not p.is_symlink() and not getattr(p,'is_junction',lambda:False)(),'linked directory')
   if d=='__pycache__':dirs.remove(d)
  for name in files:
   p=Path(base)/name;rel=p.relative_to(root).as_posix();safe_path(root,rel)
   require(p.suffix.lower() not in {'.zip','.7z','.tar','.gz','.phar','.mp4','.webm','.env'},'package or excluded file: '+rel)
   actual.append(rel)
 return sorted(actual)

def export_manifest(root):
 allowed=load(root,'publication-files.json')['files']
 require(len(allowed)==len(set(allowed)),'duplicate allowlist file')
 require(sorted(allowed)==inventory(root),'file outside explicit publication list or missing file')
 rows=[]
 for rel in sorted(allowed):
  p=safe_path(root,rel);data=p.read_bytes();scan(data,rel)
  rows.append({'path':rel,'bytes':len(data),'sha256':digest(data)})
 return {'schema_version':'1.0.0','files':rows,'manifest_sha256':digest(encoded(rows))}

def check_history(root):
 def git(*args):return subprocess.check_output(['git','-C',str(root),*args],text=True,encoding='utf-8').strip()
 require((root/'.git').is_dir(),'expected independent .git directory')
 require(not (root/'.git/objects/info/alternates').exists(),'imported alternate object database')
 require(not git('rev-parse','--is-shallow-repository')=='true','shallow history is not proof of clean history')
 roots=git('rev-list','--max-parents=0','--all').splitlines();require(len(roots)==1,'expected one documentary root commit')
 allowed=set(load(root,'publication-files.json')['files'])
 for commit in git('rev-list','--all').splitlines():
  for line in git('ls-tree','-r',commit).splitlines():
   meta,path=line.split('\t',1);mode,kind,oid=meta.split()
   require(mode=='100644' and kind=='blob' and path in allowed,'unapproved historical object')
   data=subprocess.check_output(['git','-C',str(root),'cat-file','blob',oid]);scan(data,path)
 require(not git('for-each-ref','refs/replace','--format=%(refname)'),'replace refs forbidden')
 reachable={line.split()[0] for line in git('rev-list','--objects','--all').splitlines()}
 stored=set(git('cat-file','--batch-all-objects','--batch-check=%(objectname)').splitlines())
 require(stored==reachable,'unreachable or imported objects in object database')
 return roots

def heading_ids(text):
 ids=[];counts={}
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
  h=re.sub(r'[`*]','',h).lower();h=re.sub(r'[^\w\- ]','',h,flags=re.UNICODE).replace(' ','-')
  n=counts.get(h,0);counts[h]=n+1;ids.append(h+('-'+str(n) if n else ''))
 return set(ids)


class ExampleHTML(HTMLParser):
 def __init__(self):
  super().__init__();self.robots=[];self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='meta' and attrs.get('name','').lower()=='robots':self.robots.extend(x.strip().lower() for x in attrs.get('content','').split(','))
  if attrs.get('id'):self.ids.add(attrs['id'])
  for key in ['href','src']:
   if attrs.get(key):self.links.append(attrs[key])

def morrowfield_checks(root):
 example=load(root,'examples/morrowfield-observation.json')
 require(example.get('state')=='PASS' and isinstance(example.get('visual_inspection'),dict) and example['visual_inspection'].get('state')=='PASS','incomplete Morrowfield observation')
 observed=example.get('observed_at')
 require(isinstance(observed,str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z',observed) is not None,'invalid Morrowfield observation timestamp')
 try:observed_date=datetime.strptime(observed,'%Y-%m-%dT%H:%M:%S.%fZ' if '.' in observed else '%Y-%m-%dT%H:%M:%SZ')
 except ValueError as exc:raise ValueError('invalid Morrowfield observation timestamp') from exc
 require(observed_date.replace(tzinfo=timezone.utc)<=datetime.now(timezone.utc),'future Morrowfield observation timestamp')
 source=safe_path(root,'examples/morrowfield.html')
 require(example.get('source_file')=='examples/morrowfield.html' and example.get('source_sha256')==digest(source.read_bytes()),'stale Morrowfield browser observation')
 expected={(page,lang,width,height) for page in ['collection','product','guide'] for lang in ['en','fr-CA'] for width,height in [(1365,1000),(390,844)]}
 views=example.get('views');require(isinstance(views,list) and len(views)==len(expected),'Morrowfield view coverage')
 seen=set();screens=set()
 for view in views:
  require(isinstance(view,dict) and isinstance(view.get('viewport'),dict),'Morrowfield view coverage')
  viewport=view['viewport'];key=(view.get('page'),view.get('language'),viewport.get('width'),viewport.get('height'))
  require(key in expected and key not in seen,'Morrowfield view coverage');seen.add(key)
  require(view.get('horizontal_overflow') is False and all(view.get(k) is True for k in ['one_h1','primary_action_visible','language_preserves_page','history_return_pass']),'failed Morrowfield view')
  require(view.get('purchase_disabled') is (True if key[0]=='product' else None),'Morrowfield purchase state')
  screenshot=('assets/morrowfield-'+key[0]+'-'+('fr' if key[1]=='fr-CA' else 'en')+'.png') if key[2]==1365 else None
  require('screenshot' in view and view['screenshot']==screenshot,'Morrowfield screenshot coverage')
  require(isinstance(view.get('screenshot_sha256'),str) and re.fullmatch('[0-9a-f]{64}',view['screenshot_sha256']) is not None,'Morrowfield screenshot digest')
  size=view.get('capture_dimensions')
  require(isinstance(size,dict) and type(size.get('width')) is int and type(size.get('height')) is int and size['width']==key[2] and size['height']>=key[3],'Morrowfield capture dimensions')
  if screenshot:
   screens.add(screenshot);data=safe_path(root,screenshot).read_bytes()
   require(view['screenshot_sha256']==digest(data),'stale Morrowfield screenshot')
   require(len(data)>=24 and data[:8]==b'\x89PNG\r\n\x1a\n' and data[12:16]==b'IHDR','invalid Morrowfield PNG')
   require((int.from_bytes(data[16:20],'big'),int.from_bytes(data[20:24],'big'))==(size['width'],size['height']),'Morrowfield capture dimensions')
 require(screens=={p.relative_to(root).as_posix() for p in (root/'assets').glob('morrowfield-*.png')},'Morrowfield screenshot coverage')
 journeys=example.get('journeys')
 require(isinstance(journeys,list) and len(journeys)==2 and {x.get('language') for x in journeys if isinstance(x,dict)}=={'en','fr-CA'} and all(x.get('state')=='PASS' and x.get('route')==['collection','product','guide','collection'] for x in journeys),'Morrowfield journey coverage')
 require(all(example.get(k) is True for k in ['invalid_query_falls_back','direct_file_navigation_pass']) and all(type(example.get(k)) is int and example[k]==0 for k in ['external_request_attempts','uncaught_javascript_errors']),'failed Morrowfield browser checks')
 # Static guardrails complement the recorded browser run; they do not execute JavaScript.
 html=source.read_text(encoding='utf-8');parser=ExampleHTML();parser.feed(html)
 require({'noindex','nofollow'}<=set(parser.robots),'Morrowfield noindex/nofollow required')
 require(not re.search(r'(?:https?:)?//[a-zA-Z0-9]',re.sub(r'<!--.*?-->','',html,flags=re.S)),'Morrowfield external URL')
 # The footer chooses between two literal Markdown paths in JavaScript.
 links=parser.links+[m.group(2) for m in re.finditer(r"""(['"])([^'"\s]*\.md(?:#[^'"\s]*)?)\1""",html)]
 for target in links:
  if '$'+'{' in target:continue # Template expressions need the browser observation.
  url=urlsplit(target);require(not url.scheme and not url.netloc,'Morrowfield external link')
  destination=(source.parent/unquote(url.path)).resolve() if url.path else source.resolve()
  require(destination.is_relative_to(root.resolve()) and destination.is_file(),'broken Morrowfield HTML link: '+target)
  if url.fragment:
   ids=heading_ids(destination.read_text(encoding='utf-8')) if destination.suffix=='.md' else parser.ids
   require(unquote(url.fragment) in ids,'broken Morrowfield HTML anchor: '+target)

def check(root):
 import jsonschema, yaml
 source_checks(root)
 for name in ['claims','source-lock','translation-map','release-reference']:
  schema=load(root,'schemas/'+name+'.schema.json');jsonschema.Draft202012Validator.check_schema(schema);jsonschema.validate(load(root,'artefacts/'+name+'.json'),schema,format_checker=jsonschema.FormatChecker())
 require(load(root,'artefacts/claims.json')==make_claims(root),'claim/source mismatch')
 ref=load(root,'artefacts/release-reference.json');wp=load(root,'sources/wordpress-projection.json');dev=load(root,'sources/developer-observation.json')
 require(ref['FREE']['zip_sha256']==wp['zip_sha256']==dev['package_sha256'],'edition/package mix')
 require(ref['FREE']['version']==wp['version']==dev['plugin_version'],'version mix')
 require(ref['FREE']['svn_revision']==wp['svn_revision']==dev['svn_revision'],'revision mix')
 require(ref['policy_status']==load(root,'sources/policy-projection.json')['policy_status'],'policy disagreement')
 require(load(root,'sources/manifest-projection.json')['capability_observation']['source_matches_distributed_package'] is None,'unknown changed to false')
 for kind in ['blocks','shortcodes']:
  entries=dev[kind];require(len({x['name'] for x in entries})==len(entries),'duplicate developer name')
  for x in entries:
   require(x['edition']=='FREE' and x['version']==ref['FREE']['version'],'developer edition mismatch')
   require(re.fullmatch('[0-9a-f]{64}',x['source_sha256']) is not None,'source digest prefix')
   require(x['test']['state']=='PASS' and x['test']['echo_bytes']==0,'callback error or output leak')
   if kind=='shortcodes':require(x['registered'] and x['alias_registered'] and x['test']['same_registered_callback'],'missing native alias proof')
 hashes=load(root,'artefacts/free-file-hashes.json');require(hashes['zip_sha256']==ref['FREE']['zip_sha256'],'file manifest package mix')
 filemap={x['path']:x['sha256'] for x in hashes['files']}
 require(len(filemap)==ref['FREE']['file_count'],'package file count')
 for x in dev['blocks']+dev['shortcodes']:require(filemap[x['source']]==x['source_sha256'],'developer source hash mismatch')
 translation=load(root,'artefacts/translation-map.json')['translations'];seen=set()
 for t in translation:
  require(datetime.strptime(t['reviewed_on'],'%Y-%m-%d').date()<=datetime.now(timezone.utc).date(),'future translation review date')
  require(t['translation'] not in seen,'duplicate translation');seen.add(t['translation'])
  for path,hashkey in [('source','source_sha256'),('translation','translation_sha256')]:
   require(digest(safe_path(root,t[path]).read_bytes())==t[hashkey],'stale translation: '+t['source'])
 require(seen=={p.relative_to(root).as_posix() for p in (root/'fr-ca').rglob('*.md')},'translation coverage')
 for p in root.rglob('*.md'):
  text=p.read_text(encoding='utf-8');require(len(re.findall(r'^```',text,re.M))%2==0,'unbalanced fence')
  require(len(re.findall(r'^# ',text,re.M))==1,'one H1 required: '+str(p.relative_to(root)))
  stripped=re.sub(r'(?ms)^```.*?^```\s*$','',text)
  for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',stripped):
   if target.startswith(('https://','mailto:')):continue
   require(not target.startswith(('http://','file:')),'unsafe link protocol')
   path,_,anchor=target.partition('#');dest=(p.parent/path).resolve() if path else p.resolve()
   require(dest.is_relative_to(root.resolve()) and dest.exists(),'broken or escaped local link: '+target)
   if anchor and dest.suffix=='.md':require(anchor in heading_ids(dest.read_text(encoding='utf-8')),'broken anchor: '+target)
 for p in (root/'.github/workflows').glob('*.yml'):
  text=p.read_text(encoding='utf-8');doc=yaml.load(text,Loader=yaml.BaseLoader)
  require(doc.get('permissions')=={'contents':'read'},'workflow permissions')
  require(not any(x in text for x in ['secrets.','self-hosted','pull_request_target','repository_dispatch','github.event.pull_request.','contents: write']),'unsafe workflow surface')
  for job in doc['jobs'].values():
   require(job['runs-on']=='ubuntu-latest' and int(job['timeout-minutes'])<=10,'unsafe runner/timeout')
   for step in job['steps']:
    if 'uses' in step:require(re.fullmatch(r'actions/(checkout|setup-python)@[0-9a-f]{40}',step['uses']) is not None,'unpinned action')
    if step.get('uses','').startswith('actions/checkout'):require(step['with']['persist-credentials']=='false','persistent checkout credentials')
 require('ref: main' in (root/'.github/workflows/check-upstream.yml').read_text(encoding='utf-8'),'untrusted upstream checkout')
 jsonschema.validate(load(root,'CITATION.cff'),load(root,'schemas/cff-1.2.0.schema.json'))
 cff=load(root,'CITATION.cff');doc=ref['documentation'];entity=load(root,'artefacts/repository-entity.jsonld')
 require(doc['release_url']=='https://github.com/GautierDorval/fy2press/releases/tag/'+doc['version'],'edition URL/version disagreement')
 require(load(root,'artefacts/source-lock.json')['documentation_version']==doc['version'],'source-lock/edition disagreement')
 require(entity.get('creativeWorkStatus')=='Documentary prerelease' and entity.get('version')==doc['version'],'edition entity disagreement')
 require('datePublished' not in entity,'publication date belongs in a verified receipt')
 citation=cff.get('preferred-citation',{})
 require(cff['cff-version']=='1.2.0' and 'reference' in cff['title'] and citation.get('type')=='manual','citation must describe the documentary manual')
 for record in [cff,citation]:
  require(record.get('version')==doc['version'] and record.get('url')==doc['release_url'],'citation/edition disagreement')
 require(cff.get('license')==['CC-BY-4.0','MIT'] and entity.get('license')==['https://creativecommons.org/licenses/by/4.0/','https://opensource.org/license/mit'],'documentation licence inventory')
 require(entity.get('usageInfo')=='https://github.com/GautierDorval/fy2press/blob/main/LICENSE.md','file-specific licence scope')
 changelog=(root/'CHANGELOG.md').read_text(encoding='utf-8')
 require('## '+doc['version']+'\n' in changelog,'changelog/edition disagreement')
 seen_releases=set();current_receipt=None
 for publication in ref['documentary_publications']:
  require(publication['version'] not in seen_releases,'duplicate publication receipt')
  seen_releases.add(publication['version'])
  require(re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',publication['published_at']) is not None,'invalid publication timestamp')
  try:published=datetime.strptime(publication['published_at'],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
  except ValueError as exc:raise ValueError('invalid publication timestamp') from exc
  require(published<=datetime.now(timezone.utc),'future publication timestamp')
  require(publication['release_url']=='https://github.com/GautierDorval/fy2press/releases/tag/'+publication['version'],'publication URL/version disagreement')
  require('## '+publication['version']+' (published '+publication['published_at'][:10]+')' in changelog and publication['published_at'] in changelog and publication['source_commit'] in changelog,'changelog/publication disagreement')
  if publication['version']==doc['version']:current_receipt=publication
 for record in [cff,citation]:
  if 'date-released' in record:
   require(current_receipt is not None and record['date-released']==current_receipt['published_at'][:10],'citation date requires a matching publication receipt')
 morrowfield_checks(root)
 require(len(load(root,'sources/seo-decisions.json')['decisions'])==12,'SEO decision coverage')
 generate(root,True);return export_manifest(root)

class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):raise ValueError('redirect refused')
def fetch(url):
 require(url in URLS.values(),'URL not in source allowlist')
 with urllib.request.build_opener(NoRedirect()).open(urllib.request.Request(url,headers={'User-Agent':'Fy2Press-documentation-check/1.0'}),timeout=20) as response:
  cap=30_000_000 if url.endswith('.zip') else 2_000_000
  data=response.read(cap+1);require(len(data)<=cap,'source size limit');return data

def upstream(root,fetcher=fetch):
 results=[]
 for s in load(root,'artefacts/source-lock.json')['sources']:
  try:
   data=fetcher(URLS[s['id']]);same=digest(data)==s['raw_sha256']
   if s['id']=='wordpress':
    latest=json.loads(data);old=load(root,s['retained_path']);same=all(latest.get(k)==old.get(k) for k in ['name','slug','version','requires','tested','requires_php','last_updated','download_link'])
   results.append({'source':s['id'],'state':'CURRENT' if same else 'DRIFT_DETECTED','sha256':digest(data)})
  except (OSError,ValueError,KeyError) as e:results.append({'source':s['id'],'state':'UNAVAILABLE','reason':type(e).__name__})
 return results

def extract(package,expected):
 data=package.read_bytes();require(digest(data)==expected and re.fullmatch('[0-9a-f]{64}',expected),'exact package hash required')
 with zipfile.ZipFile(package) as z:
  require(sum(x.file_size for x in z.infolist())<80_000_000,'archive expansion limit')
  files=[];blocks=[]
  for x in z.infolist():
   require(not x.filename.startswith('/') and '..' not in Path(x.filename).parts and '\\' not in x.filename,'unsafe archive member')
   require((x.external_attr>>16)&0o170000 != 0o120000,'archive symlink')
   if x.is_dir():continue
   require(x.file_size<5_000_000,'archive member limit');content=z.read(x);files.append({'path':x.filename,'sha256':digest(content)})
   if x.filename.endswith('/block.json'):blocks.append(json.loads(content))
 return {'edition':'FREE','zip_sha256':expected,'files':files,'static_block_metadata':blocks,'dynamic_registry':'NOT_RUN: execute against isolated native WordPress; static metadata omits dynamic attributes'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['check','generate','check-upstream','refresh-sources','extract-reference','export-public','check-history']);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--check',action='store_true');p.add_argument('--dry-run',action='store_true');p.add_argument('--output',type=Path);p.add_argument('--package',type=Path);p.add_argument('--sha256');a=p.parse_args();root=a.root.resolve()
 try:
  if a.command=='check':result=check(root);print(json.dumps({'state':'PASS','files':len(result['files']),'manifest_sha256':result['manifest_sha256']}))
  elif a.command=='generate':generate(root,a.check);print('PASS: generation matches' if a.check else 'Generated designated outputs')
  elif a.command in ['check-upstream','refresh-sources']:
   result=upstream(root);print(json.dumps(result,indent=2))
   if a.command=='refresh-sources' and not a.dry_run:
    require(a.output is not None,'refresh requires an explicit private --output directory')
    require(not a.output.resolve().is_relative_to(root),'raw sources may not be written into public candidate')
    a.output.mkdir(parents=True,exist_ok=False)
    for key,url in URLS.items():(a.output/(key+('.zip' if key=='developer' else '.json'))).write_bytes(fetch(url))
   return 2 if any(x['state']=='UNAVAILABLE' for x in result) else 1 if any(x['state']=='DRIFT_DETECTED' for x in result) else 0
  elif a.command=='extract-reference':
   require(a.package and a.sha256,'package and full SHA-256 required');print(json.dumps(extract(a.package,a.sha256),indent=2))
  elif a.command=='check-history':print(json.dumps({'state':'PASS','roots':check_history(root)}))
  else:
   result=check(root)
   if not a.dry_run:
    require(a.output is not None,'export requires --dry-run or a new --output directory');require(not a.output.exists(),'export destination already exists');a.output.mkdir(parents=True)
    for row in result['files']:
     dest=a.output/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/row['path'],dest)
   print(json.dumps(result,indent=2))
  return 0
 except (ValueError,KeyError,OSError,TypeError) as e:print('FAIL: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
