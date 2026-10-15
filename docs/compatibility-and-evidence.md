# Compatibility and evidence

[Français canadien](../fr-ca/docs/compatibility-and-evidence.md) · [Start here](../README.md)

Use this record to decide what to verify on your site. The local tests cover FREE component registration and returned output. They do not establish compatibility with every theme or demonstrate a completed Shopify purchase.

## What was checked

PAGUP maintains this record. The underlying observations identify their tools and methods in the [editorial provenance](../THIRD-PARTY-NOTICES.md) and [detailed results](../sources/developer-observation.json).

| Check | Version and environment | Date | What the result establishes |
| --- | --- | --- | --- |
| Official download | FREE 1.0.0; 488 files; SVN 3744276 | 2026-10-14 | The downloaded package is identified by its full hash in the release reference. |
| Plugin activation | WordPress 7.1 / PHP 8.4, disposable Docker WordPress | 2026-10-14 | Local activation with external network blocked. |
| Component registry | 17 blocks, 27 canonical shortcodes and 27 compatibility aliases | 2026-10-14 | Components registered in WordPress. Aliases are not additional features. |
| Component output | Native do_blocks/do_shortcode with fictional products and a collection | 2026-10-14 | Returned output and context are recorded per component. No store was connected. |
| Product URL shortcode | Scalar URL and HTML link modes | 2026-10-14 | Both modes returned the expected form in local product context. |
| PRO descriptions | Published version 1.0.0 documentation | Dates in the [source record](../artefacts/source-lock.json) | Descriptions only; licensed PRO execution and the current PRO package were not rechecked. |
| Connected checkout and scheduled synchronization | No real store, payment or licence activated | Not run | No conclusion about a completed commercial journey. |

## Package and compatibility scope

Between SVN 3742640 and 3744276, only `readme.txt` changed. Both packages use version 1.0.0, but their ZIP hashes differ. Each observation remains attached to the package actually examined.

The WordPress.org API and package readme declare different tested WordPress versions. Those declarations are not compatibility tests. The environment actually exercised is listed above. [Version details](../artefacts/release-reference.json).

## Product-type shortcode limitation

`fy2press_product_type` is registered, but returned no text in the local test even though the fictional product supplied a type. Static inspection of the same FREE package explains a field-name mismatch: [ShopifyService.php](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/ShopifyService.php) normalizes `productType` to `product_type`, while [ProductType.php](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductType.php) reads `productType`.

Treat the product-type display as a known limitation of this inspected path. The empty result is retained for accuracy; it is not a successful populated example. No plugin correction or new runtime test is claimed here. Before relying on this field, verify the installed version with a populated product.

For other components, returned HTML alone does not verify browser interactions. Test your exact theme, SEO extension and builder versions before client acceptance.

[Developer reference](../developer/README.md) · [Data freshness](data-ownership-and-freshness.md).
