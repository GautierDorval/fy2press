# Compatibility and evidence

[Français canadien](../fr-ca/docs/compatibility-and-evidence.md) · [Start here](../README.md)

Use evidence for the question it actually answers. A local callback test demonstrates a local rendering contract, not Shopify payment completion or universal theme compatibility.

| Observation | Artifact and environment | Producer/date | Scope |
| --- | --- | --- | --- |
| Official download identified | FREE 1.0.0; 488 files; SVN 3744276; full ZIP hash in release reference | Codex, 2026-10-14 | Provider bytes collected; no reconstruction from another source revision. |
| Plugin activation | WordPress 7.1 / PHP 8.4, disposable Docker WordPress | Codex, 2026-10-14 | Local activation with external network blocked. |
| Native component registry | 17 blocks, 27 canonical shortcodes and 27 aliases | Codex, 2026-10-14 | Actual WordPress registration, not counting aliases as extra features. |
| Component examples | Native do_blocks/do_shortcode, fictional records | Codex, 2026-10-14 | See per-entry output, context and limits in developer observation. No connected store. |
| URL shortcode modes | Scalar URL and HTML link modes | Codex, 2026-10-14 | Both observed in local product context. |
| PRO implementation descriptions | Publisher observations, version 1.0.0 | Publisher dates retained in source lock | No licensed PRO runtime or current package identity reverified here. |
| Connected checkout / scheduling | No real store, payment or licence activated | Not run | Not a failed feature or a passed commercial journey. |

The current WordPress ZIP differs from the earlier publisher receipt. SVN comparison from 3742640 to 3744276 lists only `readme.txt`; the plugin version remains 1.0.0. The older receipt is not rewritten as if it had observed today’s bytes.

The API’s tested-version declaration and the package readme declaration differ. Neither is a compatibility test. The actual local WordPress/PHP environment above remains explicit. [Version and divergence record](../artefacts/release-reference.json).

The product-type shortcode returned an empty string in the normalized local fixture. Its example remains an observed empty result, not a demonstrated populated product-type display. Other callbacks producing HTML are not proof of browser interactions. Theme, SEO-extension and builder combinations must be tested with their exact versions before client acceptance.

[Detailed developer observation](../sources/developer-observation.json) · [Developer reference](../developer/README.md) · [Data freshness](data-ownership-and-freshness.md).
