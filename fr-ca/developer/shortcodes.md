# Shortcodes publics

[English](../../developer/shortcodes.md) · [Index](README.md)

Généré depuis le registre WordPress natif du paquet FREE 1.0.0, SVN 3744276. Les résultats ci-dessous proviennent de données fictives locales, sans requête Shopify. Les valeurs par défaut sont celles du laboratoire en anglais; les textes traduisibles peuvent différer selon la langue.

Les exemples avec `id="123"` exigent l’ID WordPress réel. Les blocs produit exigent normalement une fiche produit; les blocs collection exigent une archive de collection. Une boucle peut être placée sur une page ordinaire.

## fy2press_product

Contexte: `anywhere`. FREE 1.0.0. Alias de compatibilité: `shopipress_product`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/Product.php).

```text
[fy2press_product id="123"]
```

Résultat local observé: 4041 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `handle` | str | `""` |
| `show_description` | str | `"yes"` |
| `show_collections` | str | `"yes"` |
| `show_tags` | str | `"no"` |
| `class` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_title

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTitle.php).

```text
[fy2press_product_title]
```

Résultat local observé: 89 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_description

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductDescription.php).

```text
[fy2press_product_description content_type="excerpt"]
```

Résultat local observé: 173 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_price

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_price`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductPrice.php).

```text
[fy2press_product_price type="range"]
```

Résultat local observé: 67 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_image

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_image`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductImage.php).

```text
[fy2press_product_image link_to="product"]
```

Résultat local observé: 272 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_url

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_url`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductUrl.php).

```text
[fy2press_product_url]
```

Résultat local observé: 63 octets retournés, 0 octets imprimés hors retour. URL par défaut; HTML avec format=link.

`format="url"` retourne une URL scalaire; `format="link"` retourne un lien HTML. Les deux modes ont été exécutés. Sans produit, le code peut retourner une URL illustrative; toujours fournir un contexte valide.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `format` | str | `"url"` |
| `text` | str | `"View on Shopify"` |
| `target` | str | `"_blank"` |
| `class` | str | `"shopipress-product-url shopipress-d-product-url"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_vendor

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_vendor`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVendor.php).

```text
[fy2press_product_vendor]
```

Résultat local observé: 86 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-vendor shopipress-d-product-vendor"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_type

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_type`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductType.php).

```text
[fy2press_product_type]
```

Résultat local observé: 0 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

**Sortie vide observée avec cette fixture; affichage rempli non démontré.**

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-type shopipress-d-product-type"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_tags

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_tags`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTags.php).

```text
[fy2press_product_tags]
```

Résultat local observé: 285 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_gallery

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_gallery`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductGallery.php).

```text
[fy2press_product_gallery]
```

Résultat local observé: 263 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_availability

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_availability`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductAvailability.php).

```text
[fy2press_product_availability]
```

Résultat local observé: 156 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_variants

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_variants`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVariants.php).

```text
[fy2press_product_variants]
```

Résultat local observé: 602 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `style` | str | `"dropdown"` |
| `show_prices` | bool | `false` |
| `show_images` | bool | `false` |
| `show_labels` | bool | `true` |
| `class` | str | `"shopipress-product-variants shopipress-d-product-variants"` |
| `option_class` | str | `"shopipress-variant-option shopipress-d-variant-option"` |
| `hide_default_variant` | bool | `true` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_collections

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_collections`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductCollections.php).

```text
[fy2press_product_collections]
```

Résultat local observé: 353 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_add_to_cart

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_add_to_cart`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/AddToCart.php).

```text
[fy2press_add_to_cart]
```

Résultat local observé: 1077 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_buy_now

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_buy_now`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/BuyNow.php).

```text
[fy2press_buy_now]
```

Résultat local observé: 475 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `text` | str | `"Buy Now"` |
| `class` | str | `"shopipress-buy-now-btn shopipress-d-buy-now-btn"` |
| `target` | str | `"_self"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_related_products

Contexte: `product`. FREE 1.0.0. Alias de compatibilité: `shopipress_related_products`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/RelatedProducts.php).

```text
[fy2press_related_products limit="4"]
```

Résultat local observé: 4305 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `limit` | int | `4` |
| `title` | str | `"You may also like"` |
| `orderby` | str | `"date"` |
| `class` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection

Contexte: `anywhere`. FREE 1.0.0. Alias de compatibilité: `shopipress_collection`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/Collection.php).

```text
[fy2press_collection handle="morrowfield"]
```

Résultat local observé: 6155 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `handle` | str | `""` |
| `limit` | int | `24` |
| `columns` | int | `4` |
| `show_title` | str | `"yes"` |
| `show_description` | str | `"yes"` |
| `pagination` | str | `"infinite"` |
| `class` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_products_loop

Contexte: `anywhere`. FREE 1.0.0. Alias de compatibilité: `shopipress_products_loop`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/ProductsLoop.php).

```text
[fy2press_products_loop collection="morrowfield" limit="12"]
```

Résultat local observé: 3207 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `limit` | int | `24` |
| `columns` | int | `4` |
| `collection` | str | `""` |
| `class` | str | `"shopipress-d-products-loop"` |
| `item_class` | str | `"shopipress-product-card"` |
| `pagination` | str | `"infinite"` |
| `sort_by` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_title

Contexte: `collection`. FREE 1.0.0. Alias de compatibilité: `shopipress_collection_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionTitle.php).

```text
[fy2press_collection_title]
```

Résultat local observé: 90 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `tag` | str | `"h1"` |
| `class` | str | `"shopipress-collection-title shopipress-d-collection-title"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_description

Contexte: `collection`. FREE 1.0.0. Alias de compatibilité: `shopipress_collection_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionDescription.php).

```text
[fy2press_collection_description]
```

Résultat local observé: 161 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-description shopipress-d-collection-description"` |
| `wrapper` | str | `"div"` |
| `hide_if_empty` | bool | `true` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_sort

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_collection_sort`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionSort.php).

```text
[fy2press_collection_sort]
```

Résultat local observé: 822 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-sort"` |
| `label` | str | `"Sort by:"` |
| `show_label` | bool | `true` |
| `default_option` | str | `"Sort by..."` |
| `wrapper` | str | `"div"` |
| `wrapper_class` | str | `"shopipress-sort-wrapper shopipress-d-collection-sort"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_search

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_product_search`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/ProductSearch.php).

```text
[fy2press_product_search]
```

Résultat local observé: 482 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `placeholder` | str | `"Search products..."` |
| `class` | str | `"shopipress-product-search"` |
| `wrapper_class` | str | `"shopipress-search-wrapper"` |
| `input_class` | str | `"search-input"` |
| `button_class` | str | `"search-button"` |
| `button_text` | str | `"Search"` |
| `show_results_count` | str | `"yes"` |
| `search_in` | str | `"title,description,tags"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_filter

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_collection_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/CollectionFilter.php).

```text
[fy2press_collection_filter type="dropdown"]
```

Résultat local observé: 425 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_tag_filter

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_tag_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/TagFilter.php).

```text
[fy2press_tag_filter type="tags"]
```

Résultat local observé: 226 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

Défaut dynamique : le type du filtre d’étiquettes vient du design sauvegardé valide; sinon `tags`.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_filter_sidebar

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_filter_sidebar`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/FilterSidebar.php).

```text
[fy2press_filter_sidebar][fy2press_product_search][fy2press_collection_filter][/fy2press_filter_sidebar]
```

Résultat local observé: 1234 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_price_filter

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_price_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/PriceFilter.php).

```text
[fy2press_price_filter min="0" max="250"]
```

Résultat local observé: 3186 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `min` | str | `"0"` |
| `max` | str | `"1000"` |
| `default_min` | str | `"0"` |
| `default_max` | str | `"250"` |
| `step` | str | `"10"` |
| `currency` | str | `"auto"` |
| `title` | str | `"Filter by Price"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_availability_filter

Contexte: `loop`. FREE 1.0.0. Alias de compatibilité: `shopipress_availability_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/AvailabilityFilter.php).

```text
[fy2press_availability_filter type="checkbox"]
```

Résultat local observé: 511 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `type` | str | `"tags"` |
| `options` | str | `"in_stock,out_of_stock"` |
| `title` | str | `"Availability"` |
| `show_count` | str | `"yes"` |
| `class` | str | `"availability-filter-container"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

[Observation](../../sources/developer-observation.json) · [Package](../../artefacts/release-reference.json).
