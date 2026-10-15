# Architecture decision record

[Français canadien](../fr-ca/reusable/architecture-decision.md) · [Start here](../README.md)

See the [filled Morrowfield example](../examples/morrowfield.md) before adapting this record.

Copy this record for one project. Replace the blanks with decisions and evidence; an unchecked item is not accepted by default.

| Project field | Value to record |
| --- | --- |
| Project / date / decision owner | … |
| Existing WordPress and Shopify roles | … |
| Reader and merchant objectives | … |
| Content that must remain original in WordPress | … |
| Catalog size and change frequency | … |
| Required languages and markets | … |
| Required builders and versions | … |
| Maximum acceptable refresh delay by datum | … |

## Compare real options

| Option | Why consider it? | Reason selected or rejected | Evidence |
| --- | --- | --- | --- |
| Keep links or one embedded purchase control | Smallest publishing change | … | … |
| FREE native catalog | Blocks, shortcodes, manual refresh | … | … |
| PRO native catalog | A named premium design/builder requirement | … | … |
| Another architecture | An unmet requirement such as catalog translation | … | … |

## Assign operation and costs

| Responsibility | Owner | Update trigger | Cost or subscription to verify |
| --- | --- | --- | --- |
| Shopify products, prices and inventory | … | … | Shopify plan, recorded date … |
| WordPress hosting and original content | … | … | Hosting and maintenance … |
| Synchronization and incident review | … | … | Operational time … |
| PRO and builder licences, if selected | … | … | Exact offer, currency, tax and renewal … |

## Acceptance

Record: package/version; backup and staging; representative product/variant; collection and guide; URL/SEO decision; mobile check; measured freshness; authorized cart/checkout test; downgrade behavior if needed; incident contact; maintenance owner. Link each criterion to an actual result or mark NOT_RUN.

**Decision:** …  **Unmet requirements:** …  **Review trigger/date:** …  **Owner acceptance:** …

[Source and attribution licence](../LICENSE.md). Suggested credit: “Adapted from PAGUP, Fy2Press architecture decision record, CC BY 4.0; changes by [your organization].” No promotional backlink is required beyond the licence conditions.
