# Public shortcodes

[Français canadien](../fr-ca/developer/shortcodes.md) · [Index](README.md)

Generated from the native WordPress registry of FREE 1.0.0, SVN 3744276. Results below use fictional local data without Shopify requests. Defaults reflect the English lab locale; translatable strings can vary by locale.

Examples with `id="123"` require the real WordPress post ID. Product blocks normally need a product page; collection blocks need a collection archive. A products loop can be placed on an ordinary page.

## fy2press_product

Context: `anywhere`. FREE 1.0.0. Compatibility alias: `shopipress_product`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/Product.php).

```text
[fy2press_product id="123"]
```

Observed local result: 4041 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `handle` | str | `""` |
| `show_description` | str | `"yes"` |
| `show_collections` | str | `"yes"` |
| `show_tags` | str | `"no"` |
| `class` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_title

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTitle.php).

```text
[fy2press_product_title]
```

Observed local result: 89 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `fallback` | str | `"Product Title Placeholder"` |
| `show_fallback_in_editor` | str | `"yes"` |
| `tag` | str | `"h1"` |
| `font_size` | str | `""` |
| `font_weight` | str | `""` |
| `color` | str | `""` |
| `text_align` | str | `""` |
| `margin` | str | `""` |
| `padding` | str | `""` |
| `css_class` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_description

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductDescription.php).

```text
[fy2press_product_description content_type="excerpt"]
```

Observed local result: 173 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `content_type` | str | `"full"` |
| `word_limit` | str | `"150"` |
| `tag` | str | `"div"` |
| `fallback` | str | `""` |
| `font_size` | str | `""` |
| `font_weight` | str | `"400"` |
| `color` | str | `""` |
| `text_align` | str | `""` |
| `line_height` | str | `""` |
| `margin_top` | str | `""` |
| `margin_bottom` | str | `""` |
| `padding` | str | `""` |
| `css_class` | str | `""` |
| `css_id` | str | `""` |
| `debug` | str | `"false"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_price

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_price`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductPrice.php).

```text
[fy2press_product_price type="range"]
```

Observed local result: 67 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `type` | str | `"single"` |
| `currency` | str | `"symbol"` |
| `fallback` | str | `"$29.99"` |
| `tag` | str | `"div"` |
| `font_size` | str | `""` |
| `font_weight` | str | `""` |
| `color` | str | `""` |
| `text_align` | str | `""` |
| `margin` | str | `""` |
| `padding` | str | `""` |
| `css_class` | str | `""` |
| `show_compare` | str | `"no"` |
| `compare_color` | str | `"#9ca3af"` |
| `show_sale_badge` | str | `"no"` |
| `badge_color` | str | `"#ef4444"` |
| `badge_text_color` | str | `"#ffffff"` |
| `badge_text` | str | `"On Sale"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_image

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_image`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductImage.php).

```text
[fy2press_product_image link_to="product"]
```

Observed local result: 272 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `size` | str | `"large"` |
| `width` | str | `""` |
| `height` | str | `""` |
| `object_fit` | str | `""` |
| `align` | str | `""` |
| `link_to` | str | `"none"` |
| `custom_url` | str | `""` |
| `target_blank` | str | `""` |
| `border_radius` | str | `""` |
| `border` | str | `""` |
| `box_shadow` | str | `""` |
| `margin` | str | `""` |
| `css_class` | str | `""` |
| `css_id` | str | `""` |
| `alt_text` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_url

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_url`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductUrl.php).

```text
[fy2press_product_url]
```

Observed local result: 63 returned bytes, 0 bytes echoed outside the return. URL by default; HTML with format=link.

`format="url"` returns a scalar URL; `format="link"` returns an HTML link. Both modes were executed. Without a product the code can return an illustrative URL; always supply valid context.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `format` | str | `"url"` |
| `text` | str | `"View on Shopify"` |
| `target` | str | `"_blank"` |
| `class` | str | `"shopipress-product-url shopipress-d-product-url"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_vendor

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_vendor`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVendor.php).

```text
[fy2press_product_vendor]
```

Observed local result: 86 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-vendor shopipress-d-product-vendor"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_type

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_type`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductType.php).

```text
[fy2press_product_type]
```

Observed local result: 0 returned bytes, 0 bytes echoed outside the return. HTML string.

**Empty output observed with this fixture; populated display is not demonstrated.**

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-type shopipress-d-product-type"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_tags

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_tags`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTags.php).

```text
[fy2press_product_tags]
```

Observed local result: 285 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `separator` | str | `", "` |
| `limit` | int | `0` |
| `class` | str | `"shopipress-product-tags shopipress-d-product-tags"` |
| `tag_class` | str | `"shopipress-product-tag shopipress-d-product-tag"` |
| `style` | str | `"links"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |
| `title` | str | `"Tags:"` |
| `wrapper` | str | `"div"` |
| `wrapper_class` | str | `"shopipress-tags-section shopipress-d-tags-section"` |
| `hide_if_empty` | bool | `true` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_gallery

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_gallery`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductGallery.php).

```text
[fy2press_product_gallery]
```

Observed local result: 263 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `show` | str | `"all"` |
| `layout` | str | `"gallery"` |
| `thumbs` | str | `"bottom"` |
| `size` | str | `"large"` |
| `columns` | int | `4` |
| `class` | str | `"shopipress-product-gallery shopipress-d-product-gallery"` |
| `main_class` | str | `"shopipress-main-image shopipress-d-main-image"` |
| `thumb_class` | str | `"shopipress-thumb-image shopipress-d-thumb-image"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_availability

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_availability`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductAvailability.php).

```text
[fy2press_product_availability]
```

Observed local result: 156 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `show` | str | `"status"` |
| `format` | str | `"text"` |
| `in_stock_text` | str | `"In Stock"` |
| `out_of_stock_text` | str | `"Out of Stock"` |
| `low_stock_text` | str | `"Low Stock"` |
| `low_stock_threshold` | int | `5` |
| `show_quantity` | bool | `false` |
| `class` | str | `"shopipress-product-availability shopipress-d-product-availability"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_variants

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_variants`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVariants.php).

```text
[fy2press_product_variants]
```

Observed local result: 602 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `style` | str | `"dropdown"` |
| `show_prices` | bool | `false` |
| `show_images` | bool | `false` |
| `show_labels` | bool | `true` |
| `class` | str | `"shopipress-product-variants shopipress-d-product-variants"` |
| `option_class` | str | `"shopipress-variant-option shopipress-d-variant-option"` |
| `hide_default_variant` | bool | `true` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_collections

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_product_collections`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductCollections.php).

```text
[fy2press_product_collections]
```

Observed local result: 353 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `style` | str | `"links"` |
| `separator` | str | `", "` |
| `limit` | int | `0` |
| `class` | str | `"shopipress-product-collections shopipress-d-product-collections"` |
| `collection_class` | str | `"shopipress-product-collection shopipress-d-product-collection"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |
| `title` | str | `"Collections:"` |
| `wrapper` | str | `"div"` |
| `wrapper_class` | str | `"shopipress-collections-section shopipress-d-collections-section"` |
| `hide_if_empty` | bool | `true` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_add_to_cart

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_add_to_cart`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/AddToCart.php).

```text
[fy2press_add_to_cart]
```

Observed local result: 1077 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_buy_now

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_buy_now`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/BuyNow.php).

```text
[fy2press_buy_now]
```

Observed local result: 475 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `text` | str | `"Buy Now"` |
| `class` | str | `"shopipress-buy-now-btn shopipress-d-buy-now-btn"` |
| `target` | str | `"_self"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_related_products

Context: `product`. FREE 1.0.0. Compatibility alias: `shopipress_related_products`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/RelatedProducts.php).

```text
[fy2press_related_products limit="4"]
```

Observed local result: 4305 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `limit` | int | `4` |
| `title` | str | `"You may also like"` |
| `orderby` | str | `"date"` |
| `class` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_collection

Context: `anywhere`. FREE 1.0.0. Compatibility alias: `shopipress_collection`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/Collection.php).

```text
[fy2press_collection handle="morrowfield"]
```

Observed local result: 6155 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `id` | str | `""` |
| `handle` | str | `""` |
| `limit` | int | `24` |
| `columns` | int | `4` |
| `show_title` | str | `"yes"` |
| `show_description` | str | `"yes"` |
| `pagination` | str | `"infinite"` |
| `class` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_products_loop

Context: `anywhere`. FREE 1.0.0. Compatibility alias: `shopipress_products_loop`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/ProductsLoop.php).

```text
[fy2press_products_loop collection="morrowfield" limit="12"]
```

Observed local result: 3207 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `limit` | int | `24` |
| `columns` | int | `4` |
| `collection` | str | `""` |
| `class` | str | `"shopipress-d-products-loop"` |
| `item_class` | str | `"shopipress-product-card"` |
| `pagination` | str | `"infinite"` |
| `sort_by` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_collection_title

Context: `collection`. FREE 1.0.0. Compatibility alias: `shopipress_collection_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionTitle.php).

```text
[fy2press_collection_title]
```

Observed local result: 90 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `tag` | str | `"h1"` |
| `class` | str | `"shopipress-collection-title shopipress-d-collection-title"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_collection_description

Context: `collection`. FREE 1.0.0. Compatibility alias: `shopipress_collection_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionDescription.php).

```text
[fy2press_collection_description]
```

Observed local result: 161 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-description shopipress-d-collection-description"` |
| `wrapper` | str | `"div"` |
| `hide_if_empty` | bool | `true` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_collection_sort

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_collection_sort`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionSort.php).

```text
[fy2press_collection_sort]
```

Observed local result: 822 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-sort"` |
| `label` | str | `"Sort by:"` |
| `show_label` | bool | `true` |
| `default_option` | str | `"Sort by..."` |
| `wrapper` | str | `"div"` |
| `wrapper_class` | str | `"shopipress-sort-wrapper shopipress-d-collection-sort"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_product_search

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_product_search`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/ProductSearch.php).

```text
[fy2press_product_search]
```

Observed local result: 482 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `placeholder` | str | `"Search products..."` |
| `class` | str | `"shopipress-product-search"` |
| `wrapper_class` | str | `"shopipress-search-wrapper"` |
| `input_class` | str | `"search-input"` |
| `button_class` | str | `"search-button"` |
| `button_text` | str | `"Search"` |
| `show_results_count` | str | `"yes"` |
| `search_in` | str | `"title,description,tags"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_collection_filter

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_collection_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/CollectionFilter.php).

```text
[fy2press_collection_filter type="dropdown"]
```

Observed local result: 425 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `type` | str | `"dropdown"` |
| `show_count` | str | `"yes"` |
| `class` | str | `"shopipress-collection-filter"` |
| `wrapper_class` | str | `"shopipress-filter-wrapper"` |
| `title` | str | `"Collection"` |
| `show_title` | str | `"yes"` |
| `show_all_option` | str | `"yes"` |
| `all_text` | str | `"All Collections"` |
| `limit` | str | `"0"` |
| `orderby` | str | `"name"` |
| `order` | str | `"ASC"` |
| `hide_empty` | str | `"yes"` |
| `hierarchical` | str | `"yes"` |
| `behavior` | str | `"collection_archive"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_tag_filter

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_tag_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/TagFilter.php).

```text
[fy2press_tag_filter type="tags"]
```

Observed local result: 226 returned bytes, 0 bytes echoed outside the return. HTML string.

Dynamic default: tag-filter type follows a valid saved design setting; otherwise `tags`.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `type` | str | `"tags"` |
| `show_count` | str | `"yes"` |
| `class` | str | `"shopipress-tag-filter"` |
| `wrapper_class` | str | `"shopipress-filter-wrapper"` |
| `title` | str | `"Filter by Tags"` |
| `show_title` | str | `"yes"` |
| `show_all_option` | str | `"yes"` |
| `all_text` | str | `"All Tags"` |
| `limit` | str | `"10"` |
| `orderby` | str | `"count"` |
| `order` | str | `"DESC"` |
| `hide_empty` | str | `"yes"` |
| `multiple` | str | `"yes"` |
| `style` | str | `"badges"` |
| `max_display` | str | `"20"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_filter_sidebar

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_filter_sidebar`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/FilterSidebar.php).

```text
[fy2press_filter_sidebar][fy2press_product_search][fy2press_collection_filter][/fy2press_filter_sidebar]
```

Observed local result: 1234 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `class` | str | `"shopipress-filter-sidebar"` |
| `wrapper_class` | str | `"filter-sidebar-wrapper"` |
| `title` | str | `"Filter Products"` |
| `show_title` | str | `"yes"` |
| `style` | str | `"sidebar"` |
| `background` | str | `"#f8f9fa"` |
| `padding` | str | `"20px"` |
| `border_radius` | str | `"8px"` |
| `gap` | str | `"20px"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_price_filter

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_price_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/PriceFilter.php).

```text
[fy2press_price_filter min="0" max="250"]
```

Observed local result: 3186 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `min` | str | `"0"` |
| `max` | str | `"1000"` |
| `default_min` | str | `"0"` |
| `default_max` | str | `"250"` |
| `step` | str | `"10"` |
| `currency` | str | `"auto"` |
| `title` | str | `"Filter by Price"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## fy2press_availability_filter

Context: `loop`. FREE 1.0.0. Compatibility alias: `shopipress_availability_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/AvailabilityFilter.php).

```text
[fy2press_availability_filter type="checkbox"]
```

Observed local result: 511 returned bytes, 0 bytes echoed outside the return. HTML string.

| Attribute | Type | Default / contract |
| --- | --- | --- |
| `type` | str | `"tags"` |
| `options` | str | `"in_stock,out_of_stock"` |
| `title` | str | `"Availability"` |
| `show_count` | str | `"yes"` |
| `class` | str | `"availability-filter-container"` |

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

[Observation](../sources/developer-observation.json) · [Package](../artefacts/release-reference.json).
