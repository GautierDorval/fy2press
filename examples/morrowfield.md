# Morrowfield: collection, product and guide

[Français canadien](../fr-ca/examples/morrowfield.md) · [Start here](../README.md)

## Intended composition

A fictional Morrowfield editorial site has three page roles:

1. **Collection:** explain the selection, then display a products loop for the collection handle.
2. **Product:** show one synchronized product with the correct product context, observed price and purchase control.
3. **Guide:** explain how to choose between items. Keep the guide’s original prose and its own URL; link to products where useful.

## Compose the collection

In a WordPress Shortcode block, use the canonical public shortcode:

```text
[fy2press_products_loop collection="morrowfield" limit="12" columns="3"]
```

Replace `morrowfield` with an actual synchronized collection handle on your staging site. The loop and its filters need a compatible page context. A grid’s displayed price is not evidence of a fresh remote checkout price.

For a single product on an ordinary page:

```text
[fy2press_product id="123"]
```

Replace `123` with the **WordPress product post ID**, not a Shopify product or variant ID. The full component can differ from placing a product-context Gutenberg block on an ordinary page. See [component contracts](../developer/README.md).

## Keep editorial work explicit

Write the guide as normal WordPress content. For example, introduce the selection criteria, explain two use cases and link to the product pages. The guide is not equivalent to one product merely because it mentions it. Apply [SEO-03](../docs/seo-decision-matrix.md#seo-03--original-buying-guide).

## Evidence boundary

The documentation lab used two fictional product records and one collection. Native component examples were executed without Shopify network access. This annotated page combines those observed components into an editorial proposal; a browser journey through this exact three-page composition was not executed. No claim of connected synchronization, actual inventory or completed payment follows.

Before client use: synchronize an authorized test catalog, replace example IDs, inspect each rendered page, test mobile navigation, and verify the intended cart/checkout path under its own authorization.
