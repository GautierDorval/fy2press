# Documentation tools

Python 3.11 or newer is required. Install the pinned validation dependencies with PowerShell:

```powershell
python -m pip install -r requirements.txt
python scripts/reference.py check
python scripts/reference.py generate --check
python -B -m unittest discover -s tests
python scripts/reference.py export-public --dry-run
```

`check` is offline and does not write files. It validates schemas, links, provenance hashes, translation hashes, generated content and the explicit publication list. `generate --check` computes expected bytes in memory and compares them without writing. `generate` writes only `artefacts/claims.json`, the edition-table regions and the four EN/FR developer pages.

## Source updates are separate

```powershell
python scripts/reference.py check-upstream
python scripts/reference.py refresh-sources --dry-run
```

Network commands use only the hardcoded public source URLs, reject redirects, cap response size and time out. The trusted-branch workflow checks upstream; a public PR does not control its URLs. Exit codes: 0 CURRENT, 1 DRIFT_DETECTED, 2 UNAVAILABLE. Unavailability never rewrites a capability as absent. For WordPress API metadata, changing download counters is ignored; selected version and requirement fields are compared. The ZIP is hashed independently, so a readme-only archive change at the same product version is detected.

To collect a proposed refresh, explicitly supply a **new private directory outside this repository**:

```powershell
python scripts/reference.py refresh-sources --output C:/approved-private-review/source-refresh
```

This creates raw inputs for review, not public projections. Review field mappings, omissions and conflicts; update the retained projection and both raw/retained hashes only after review. Update the package observation separately. Rerun generation, review both languages, then record hashes in `artefacts/translation-map.json`. A hash update alone is not editorial review. Preserve historical product observations and documentation tags.

## Package extraction

```powershell
python scripts/reference.py extract-reference --package C:/approved-private-review/fy2press-public.zip --sha256 FULL_SHA256
```

The command requires an exact archive digest and lists static metadata and file hashes without executing plugin code. It **does not** claim dynamic registration or full attribute coverage. The retained developer observation was collected separately in native WordPress with outgoing network blocked, fictional records and no commercial credentials. Reproduce that step in a disposable WordPress environment before replacing the dynamic inventory. Do not infer a callback return from its name or use another source checkout as the distributed package.

## Explicit public export

`publication-files.json` is the reviewed file selection. Extra files, packages, linked paths, private paths and secret patterns are refused. Update the selection deliberately when adding original documentation files. A secret-pattern pass is not an absolute guarantee of no sensitive information.

```powershell
python scripts/reference.py export-public --output C:/approved-public-export/fy2press
python scripts/reference.py check-history
```

The export destination must be new. `check-history` requires an independently initialized documentary Git repository and examines all refs and their blob content. Run it before the first public push; the ordinary offline checks also work from a documentation ZIP without Git. These tools neither create a remote nor push, rename repositories, publish releases or connect to a merchant store.

## Scope of generated data

- `claims.json`: one assertion per publisher capability, preserving edition, implementation state, limits and separate validation.
- `source-lock.json`: complete raw-byte hash plus the hash of each reviewed projection. A projection is not described as a byte-identical source copy.
- `release-reference.json`: separate documentation/FREE/PRO identities and provider observations.
- `translation-map.json`: exact English and French UTF-8 hashes; assisted review remains human-review-pending.
- `developer-observation.json`: version-specific native registrations and local callback outcomes, not a stable API promise.

See [contribution rules](../CONTRIBUTING.md) and [source precedence](../artefacts/source-precedence.json).
