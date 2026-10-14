# SEO decision matrix

[Français canadien](../fr-ca/docs/seo-decision-matrix.md) · [Start here](../README.md)

Separate where commercial data is managed from which URL should represent a page in search. The twelve records below are an editorial decision matrix; the Fy2Press-control row names the implementation boundary. Recommendations are not measured ranking outcomes.

A canonical is a preference for duplicate or very similar content, not a guarantee. Do not use robots.txt to impose it or combine noindex and canonical as an automatic consolidation recipe. [Google’s guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls). An original buying guide generally keeps its own URL.

## SEO-01 · Similar product, Shopify preferred

| Criterion | Decision |
| --- | --- |
| Object | Product |
| Context | Same offer and substantially similar copy on both platforms. |
| Reader goal | Reach the primary commercial page. |
| Commercial source | Shopify |
| Editorial value | Limited added WordPress content. |
| Possible equivalence | Check similarity; same SKU alone is insufficient. |
| URL preference | Shopify product URL if equivalence is justified. |
| WordPress action | Enable product indexing and select the Shopify product canonical source; inspect output. |
| Shopify action | Keep the preferred product reachable and review its canonical, sitemap and links. |
| Fy2Press control | FREE product canonical source; not a collection setting. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Conflicting links or an unavailable Shopify destination. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-02 · Enriched WordPress product

| Criterion | Decision |
| --- | --- |
| Object | Product |
| Context | WordPress adds substantial product-specific guidance. |
| Reader goal | Read the richer purchase information. |
| Commercial source | Shopify |
| Editorial value | Original comparison, usage or selection advice. |
| Possible equivalence | Evaluate actual overlap; enrichment may change page intent. |
| URL preference | WordPress if it is the intended representative page. |
| WordPress action | Keep product canonical source WordPress; verify self-canonical output with the SEO extension. |
| Shopify action | Review Shopify separately; Fy2Press does not edit that platform’s canonical. |
| Fy2Press control | FREE product preference, with Shopify changes outside the plugin. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Assuming one local option consolidates both sites. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-03 · Original buying guide

| Criterion | Decision |
| --- | --- |
| Object | Editorial page |
| Context | One guide explains a choice across several products. |
| Reader goal | Understand a decision, then visit a product. |
| Commercial source | Shopify |
| Editorial value | The guide itself is the value. |
| Possible equivalence | Not equivalent to one of its linked product pages. |
| URL preference | The guide’s own URL. |
| WordPress action | Use normal WordPress/SEO page controls and link relevant products. |
| Shopify action | Maintain product destinations; no cross-canonical needed merely for links. |
| Fy2Press control | Product canonical settings do not turn an original guide into a product. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Canonicalizing a valuable guide to an unrelated product. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-04 · Useful WordPress collection

| Criterion | Decision |
| --- | --- |
| Object | Collection archive |
| Context | A blog needs a navigable selection with a useful introduction. |
| Reader goal | Explore a relevant set. |
| Commercial source | Shopify |
| Editorial value | Selection rationale and internal links. |
| Possible equivalence | Assess the whole selection and introduction. |
| URL preference | A distinct useful WordPress collection URL. |
| WordPress action | Review collection indexing and the taxonomy canonical emitted by the SEO extension. |
| Shopify action | Review any corresponding Shopify collection independently. |
| Fy2Press control | FREE collection indexing; no Shopify collection-canonical selector found in the inspected service. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Applying the product canonical setting to taxonomies. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-05 · Competing collection pages

| Criterion | Decision |
| --- | --- |
| Object | Collection archives |
| Context | Two pages share a name but may contain different products or introductions. |
| Reader goal | Find the intended selection. |
| Commercial source | Shopify |
| Editorial value | Compare scope, text and merchandising purpose. |
| Possible equivalence | A shared name is not proof of equivalence. |
| URL preference | Choose after comparison, not by platform default. |
| WordPress action | Use verified taxonomy controls or a separately maintained canonical implementation when justified. |
| Shopify action | Coordinate the matching collection and links with its owner. |
| Fy2Press control | Indexing is available; automatic collection canonical mapping is not established. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Consolidating pages with different intent. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-06 · Seasonal selection

| Criterion | Decision |
| --- | --- |
| Object | Campaign page |
| Context | Time-bound content and navigation support a seasonal offer. |
| Reader goal | Choose for the occasion. |
| Commercial source | Shopify |
| Editorial value | Campaign context and curated explanation. |
| Possible equivalence | A campaign can differ from an evergreen collection. |
| URL preference | Campaign URL while useful; record its later lifecycle. |
| WordPress action | Publish original copy and a loop; plan retention, update or a justified redirect. |
| Shopify action | Maintain product availability and offers. |
| Fy2Press control | FREE composition; no automatic campaign expiry contract. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Orphaned seasonal pages and obsolete offers. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-07 · Thin tags

| Criterion | Decision |
| --- | --- |
| Object | Tag archive |
| Context | An automatic label adds little navigation or content. |
| Reader goal | Avoid empty or repetitive destinations. |
| Commercial source | Shopify |
| Editorial value | Little distinct value. |
| Possible equivalence | Do not choose a canonical solely from tag text. |
| URL preference | No search-target URL until value is established. |
| WordPress action | Review tag indexing; default observed setting is false. Keep noindex crawlable when removal from results is intended. |
| Shopify action | Review Shopify tags separately; no taxonomy policy is pushed there. |
| Fy2Press control | FREE tag indexing, separate from products and collections. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Using robots.txt as a canonical control. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-08 · Editorialized tags

| Criterion | Decision |
| --- | --- |
| Object | Tag archive |
| Context | A tag supports a real topic with useful content and navigation. |
| Reader goal | Browse a meaningful topic. |
| Commercial source | Shopify |
| Editorial value | Original topic explanation and selected links. |
| Possible equivalence | Check overlap with collections and guides. |
| URL preference | A useful tag URL, if the taxonomy strategy supports it. |
| WordPress action | Assess consequences before enabling the global tag index option; inspect all affected archives. |
| Shopify action | No matching Shopify action is implied. |
| Fy2Press control | FREE global taxonomy setting; per-tag exceptions are not established here. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Making every thin tag indexable for one useful topic. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-09 · Filters and sorting

| Criterion | Decision |
| --- | --- |
| Object | Parameterized results |
| Context | Visitors filter price, availability or product search. |
| Reader goal | Find a product efficiently. |
| Commercial source | Shopify |
| Editorial value | Often a navigation state, sometimes a deliberate landing page. |
| Possible equivalence | Sort order may repeat a set; filters may change it. |
| URL preference | Decide separately for stable curated pages and transient results. |
| WordPress action | Inspect actual parameter URLs and SEO output; create dedicated useful pages where justified. |
| Shopify action | Review any corresponding Shopify filtering independently. |
| Fy2Press control | FREE discovery controls do not establish a universal parameter canonical policy. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Indexing arbitrary combinations or hiding all useful selections. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-10 · Selected variants

| Criterion | Decision |
| --- | --- |
| Object | Product variant state |
| Context | A visitor selects an option within a product. |
| Reader goal | See the matching price and availability. |
| Commercial source | Shopify |
| Editorial value | Variant details, not necessarily a separate document. |
| Possible equivalence | Inspect whether URLs and page content actually differ. |
| URL preference | Do not invent native variant pages. |
| WordPress action | Check selected state, visible price, structured offer and returned URL together. |
| Shopify action | Confirm the selected merchandise and checkout context. |
| Fy2Press control | Variant controls exist; distinct native variant-page routing is not established. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Publishing an offer inconsistent with the visible selection. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-11 · Unavailable, removed or renamed

| Criterion | Decision |
| --- | --- |
| Object | Product lifecycle |
| Context | Stock loss, absence from a complete catalog or changed handle. |
| Reader goal | Understand whether an item can still be bought. |
| Commercial source | Shopify |
| Editorial value | Replacement advice may remain useful. |
| Possible equivalence | Unavailability, removal and renaming are different events. |
| URL preference | Review the surviving useful URL and redirects case by case. |
| WordPress action | Check status and links after sync. Code soft-removes absent products, default draft; this is not permanent deletion. |
| Shopify action | Confirm the source event and any merchant redirect. |
| Fy2Press control | FREE reconciliation code observed statically; connected lifecycle not retested here. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Treating stock loss as disappearance or assuming automatic redirects. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-12 · Several languages

| Criterion | Decision |
| --- | --- |
| Object | Localized content and catalog |
| Context | A guide and its linked products target several languages. |
| Reader goal | Read relevant content in the intended language. |
| Commercial source | Shopify |
| Editorial value | Original localized editorial work. |
| Possible equivalence | Translation is not identical-language duplication. |
| URL preference | Language-appropriate URLs and relationships. |
| WordPress action | Verify language links and canonicals with the localization stack. |
| Shopify action | Verify the store’s language and market settings independently. |
| Fy2Press control | Interface translation is distinct from multilingual catalog sync, which is not available in the stated scope. |
| SEO extension | Inspect the installed SEO extension and version; registered integration hooks do not prove every version compatible. |
| Risks | Assuming translated UI proves translated synchronized products. |
| Verification | Inspect rendered canonical, robots, sitemap inclusion and internal links; then observe the selected search URL where available. |
| Version | FREE 1.0.0 / SVN 3744276 |

Control source: [SEOIndexingService.php at SVN 3744276](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/SEOIndexingService.php). States: [release reference](../artefacts/release-reference.json).

[Fill out a single-family SEO decision](../reusable/seo-decision-record.md).
