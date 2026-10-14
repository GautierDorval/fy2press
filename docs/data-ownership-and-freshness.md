# Data ownership and freshness

[Français canadien](../fr-ca/docs/data-ownership-and-freshness.md) · [Start here](../README.md)

A synchronized record, an API cache and a rendered page are different observations. The table below states the source and reader for each datum; it does not promise that all readers refresh together.

| Datum | Management source and storage | Render reader | Refresh and synchronization effect |
| --- | --- | --- | --- |
| Title | Shopify; saved as post title and product observation. | WordPress lists can read the saved title; product components can read cached product data. | Synchronization can reapply the title. A product fetch is not proof that every title changed. |
| Slug / handle | Shopify handle; WordPress post_name and product metadata. | WordPress routing and product URL generation. | Synchronization can reapply it. Review old links; an automatic redirect is not established. |
| Source description | Shopify description; product cache/meta. | TemplateDataProvider and the selected description component. | A product fetch may refresh its observation. Do not confuse this with preserved WordPress editorial content. |
| WordPress editorial content | WordPress editor; post_content, pages and articles. | The selected template must actually render that content. | Existing post_content is preserved by inspected synchronization updates; theme and component selection still determine visibility. |
| Images | Shopify URLs retained in product observations; optional WordPress fallback. | Browser requests the image URL emitted by the component. | No local media mirroring is established. Cached HTML and the remote image service have separate lifetimes. |
| Grid price | Shopify observation saved through sync snapshot and metadata. | Product card and local catalog query paths. | Refresh the relevant synchronization path; do not infer a fresh grid from a product-page API request. |
| Variant price | Shopify variants; full product cache and synchronized offer evidence. | Product components select an observed price; checkout is a separate Shopify observation. | Context and acquisition age matter. Changing a currency label does not establish market-aware prices. |
| Availability | Shopify product and variant availability; local observations. | Cards, variant controls and cart eligibility may use different observations. | Unknown or stale data is not evidence that a variant can be purchased. Cart acceptance is verified separately. |
| Collections | Shopify relationships; shopipress_collections terms and relationships. | WordPress taxonomy queries and collection components. | Synchronization reconciles membership. Review any locally edited term copy on staging. |
| Tags | Shopify tags; shopipress_tags terms and relationships. | WordPress queries and filter components; indexing policy is a separate setting. | A new synchronization can change relationships; a product render does not prove taxonomy reconciliation. |
| Cart | Shopify cart service; local browser/session references and interface. | Cart requests and responses, then Shopify checkout. | Catalog synchronization does not synchronize orders into WordPress or certify a completed transaction. |
| Structured product data | Local product identity and selected commercial observation. | ProductSchemaService coordinates the emitted product offer. | Inspect JSON-LD against visible price, currency and availability. Valid JSON is not proof of current stock or rich results. |

## Cache, interruptions and checks

These rules complete every row above:

- **Cache:** `CacheService` uses acquisition age and context. The observed default configured duration is 1,800 seconds; HTML or external caches may retain other values. Restoring an evicted cache does not renew the observation’s age.
- **Trigger:** synchronized fields change during synchronization; some product components can request Shopify between synchronizations. WordPress prose changes when an editor saves it; the cart follows its own requests.
- **Interruption:** incomplete discovery, interrupted writing and a failed render-time request are different cases. Components may retain old display data without accepting it as evidence of a purchasable variant. Do not infer write-phase resumption merely from “batches.”
- **Available test:** native registry and local component examples were executed against the identified package. Connected reconciliation, real refresh delays and remote cart behavior were not retested here. The source assignments above are static observations of public services.
- **Limit:** for each row, record the value before change, Shopify change time, next synchronization, cache state and actual rendered value. One product-page measurement does not qualify a grid.

## Separate synchronization contracts

Discovery traverses Shopify pages and prepares a catalog observation. Writing reconciles WordPress records, states and relationships. Resuming discovery does not establish resuming writes. The current package has batched processing paths; their static presence is not an interruption test.

FREE requires manual initiation. PRO describes cron scheduling under an active licence; execution can wait for the next trigger. Scheduling is not a webhook. Webhook queues and multilingual catalog synchronization are not established as available in the publisher’s scope.

For a frequently changing catalog, define a maximum delay for each row and test each change separately. Include cache expiry and network failure in an authorized environment.

Inspected sources: [SyncController](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/controllers/SyncController.php), [CacheService](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/CacheService.php), [TemplateDataProvider](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/TemplateDataProvider.php), [ProductSchemaService](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/ProductSchemaService.php). FREE 1.0.0, SVN 3744276.

[Agency handover template](../reusable/agency-handover.md).
