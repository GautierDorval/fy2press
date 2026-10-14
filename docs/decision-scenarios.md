# Eight project decisions

[Français canadien](../fr-ca/docs/decision-scenarios.md) · [Start here](../README.md)

Choose the smallest architecture that meets the project. Each scenario ends in a check.

## 1. Existing blog

**Starting point** A publisher has useful articles and a Shopify catalog.

**Decision** Selected products in articles, or native catalog pages?

**Role and edition** Use FREE blocks or shortcodes around existing prose. Keep article content separate from synchronized fields.

**Counterexample** One embedded purchase button may suffice for one product; a full catalog then adds maintenance without a clear purpose.

**Verification** Publish one staging article. Check product context, links and the article’s own canonical URL.

## 2. Editorial brand

**Starting point** A brand combines a magazine with commercial collections.

**Decision** Who owns descriptions, advice and prices?

**Role and edition** Use WordPress for original guides and Shopify for product facts. Start with FREE; consider PRO for multiple designs or native builders.

**Counterexample** A guide that links products is not automatically equivalent to a product page.

**Verification** Change a source title in an authorized test store and synchronize staging. Confirm which title changes and that the original guide remains.

## 3. Seasonal campaign

**Starting point** A seasonal selection has its own introduction and navigation.

**Decision** Will the page remain useful after the event?

**Role and edition** Compose a collection and editorial landing page in FREE. Select PRO only for a documented premium layout requirement.

**Counterexample** Do not assume the plugin archives campaigns or redirects expired URLs.

**Verification** Record the end date, content owner and decision to keep, update or retire the page; recheck links afterwards.

## 4. Block-based agency

**Starting point** An agency builds with the native WordPress editor.

**Decision** Can the client maintain the composition?

**Role and edition** Start with FREE Gutenberg blocks. Separate product templates from ordinary pages containing a products loop.

**Counterexample** A product-context block on an ordinary page may show fallback content rather than a selected product.

**Verification** Test a product template and an ordinary page on mobile. Record context requirements in the agency handover.

## 5. Builder-based agency

**Starting point** A project uses Elementor or WPBakery.

**Decision** Are native controls needed or can a shortcode suffice?

**Role and edition** Native builder components belong to PRO. Shortcode insertion is a separate integration path. Builder licences remain separate.

**Counterexample** Do not promise native Elementor controls in FREE or compatibility with every builder version.

**Verification** Test the exact theme, builder and template under an authorized active licence. Check the required return-to-FREE behavior.

## 6. Frequently changing catalog

**Starting point** Price and stock change faster than editorial content.

**Decision** What delay is acceptable for each visible value?

**Role and edition** Define refresh expectations per data path. FREE sync is manual; PRO scheduling uses WordPress cron and still needs scoped connected qualification.

**Counterexample** A runtime product request does not refresh every grid, term, slug or cached page.

**Verification** On an authorized test store, change price, variant availability and title separately. Measure the grid, product and checkout; record the slowest path.

## 7. Several languages

**Starting point** A business publishes guides in several languages.

**Decision** Interface, editorial pages or synchronized product translations?

**Role and edition** Localize editorial pages with established site tools. Neither FREE nor documented PRO scope establishes multilingual catalog synchronization.

**Counterexample** Translated admin strings or nine site languages do not establish translated Shopify catalogs.

**Verification** Trace one product and guide across languages, including URLs and language links. Keep unmet catalog-translation requirements explicit.

## 8. Two product surfaces

**Starting point** Similar product pages exist in Shopify and WordPress.

**Decision** Which URL best serves the intended search and buying journey?

**Role and edition** Assess equivalence and choose a preference by page family. FREE has product canonical and indexing controls; taxonomy controls are separate.

**Counterexample** A WordPress setting does not rewrite Shopify canonicals or guarantee the engine’s selected URL.

**Verification** Compare rendered canonicals, robots, sitemaps and links on both platforms; record the search engine choice when available.

Next: [installation](https://fy2press.com/docs/installation/), [connection](https://fy2press.com/docs/connect-shopify/), [SEO matrix](seo-decision-matrix.md) and [agency handover](../reusable/agency-handover.md). B2B quotations, ACF mapping and multi-store management are not established capabilities.
