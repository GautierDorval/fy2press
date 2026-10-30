# Developer reference

[Français canadien](../fr-ca/developer/README.md) · [Start here](../README.md)

Use [blocks](blocks.md) in their declared WordPress context and [shortcodes](shortcodes.md) by canonical name. The observed package registers `fy2press_*` shortcodes with `shopipress_*` aliases; block names remain `shopipress/...`. These are technical identifiers for Fy2Press, not a second brand.

The reference comes from FREE 1.0.0 downloaded from WordPress.org, with the [full package identity](../artefacts/release-reference.json). Dynamic attributes and supports were read from WordPress’s native registry in a network-isolated lab. Static `block.json` files alone do not contain the complete registered attribute schema.

Every entry names its source, context, defaults, example and observed local return. Example WordPress IDs are placeholders to replace. Missing context can yield an empty string or fallback; a callback that returns HTML does not prove successful browser interaction or a connected purchase.

The [operational reference](operational-reference.md) describes Fy2Press 1.1.0 as published on WordPress.org: catalog data and page caches, trusted proxies, themes and templates, uninstalling with WP-CLI, and availability and cart checks. It keeps its own version scope.

Only [the explicitly documented extension point](extension-points.md) is presented for integration. Other detected internal hooks and PRO implementation symbols are not promoted to stable public APIs. No prefix migration is requested by this reference.

To refresh: use [the extraction and validation commands](../scripts/README.md), review the package identity and reproduce dynamic observations in an isolated environment before replacing the retained inventory.
