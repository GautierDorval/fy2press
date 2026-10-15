# Codes courts publics

[English](../../developer/shortcodes.md) · [Index](README.md)

Généré depuis le registre WordPress natif du paquet FREE 1.0.0, SVN 3744276. Les résultats ci-dessous proviennent de données fictives locales, sans requête Shopify. Les valeurs par défaut sont celles du laboratoire en anglais ; les textes traduisibles peuvent différer selon la langue.

Les exemples avec `id="123"` exigent l’ID WordPress réel. Les blocs produit exigent normalement une fiche produit ; les blocs collection exigent une archive de collection. Une boucle peut être placée sur une page ordinaire.

## fy2press_product

Résultat attendu : Un composant produit complet pour l’ID de fiche WordPress fourni.

Contexte : `anywhere`. FREE 1.0.0. Alias de compatibilité : `shopipress_product`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/Product.php).

```text
[fy2press_product id="123"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 4041 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `handle` | str | `""` |
| `show_description` | str | `"yes"` |
| `show_collections` | str | `"yes"` |
| `show_tags` | str | `"no"` |
| `class` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_title

Résultat attendu : Le titre du produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTitle.php).

```text
[fy2press_product_title]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 89 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_description

Résultat attendu : La description du produit dans le contexte courant.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductDescription.php).

```text
[fy2press_product_description content_type="excerpt"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 173 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_price

Résultat attendu : Le prix formaté selon les données produit disponibles.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_price`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductPrice.php).

```text
[fy2press_product_price type="range"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 67 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_image

Résultat attendu : L’image principale du produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_image`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductImage.php).

```text
[fy2press_product_image link_to="product"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 272 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_url

Résultat attendu : Une URL produit scalaire par défaut, ou un lien HTML avec format="link".

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_url`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductUrl.php).

```text
[fy2press_product_url]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 63 octets retournés, 0 octets imprimés hors retour. URL par défaut ; HTML avec format=link.

</details>

`format="url"` retourne une URL scalaire ; `format="link"` retourne un lien HTML. Les deux modes ont été exécutés. Sans produit, le code peut retourner une URL illustrative ; toujours fournir un contexte valide.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `format` | str | `"url"` |
| `text` | str | `"View on Shopify"` |
| `target` | str | `"_blank"` |
| `class` | str | `"shopipress-product-url shopipress-d-product-url"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_vendor

Résultat attendu : Le nom du fournisseur du produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_vendor`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVendor.php).

```text
[fy2press_product_vendor]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 86 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-vendor shopipress-d-product-vendor"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_type

Résultat attendu : Le type de produit lorsqu’il est disponible ; le parcours FREE 1.0.0 examiné comporte une incohérence de nom de champ. Consultez les notes de compatibilité.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_type`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductType.php).

```text
[fy2press_product_type]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 0 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

**Sortie vide observée ; affichage rempli non démontré.** [Limite connue](../docs/compatibility-and-evidence.md).

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `class` | str | `"shopipress-product-type shopipress-d-product-type"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_tags

Résultat attendu : La liste des étiquettes du produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_tags`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductTags.php).

```text
[fy2press_product_tags]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 285 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_gallery

Résultat attendu : La galerie d’images du produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_gallery`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductGallery.php).

```text
[fy2press_product_gallery]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 263 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_availability

Résultat attendu : L’indication de disponibilité selon les données produit disponibles.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_availability`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductAvailability.php).

```text
[fy2press_product_availability]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 156 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_variants

Résultat attendu : Les contrôles de choix de variante dans un contexte produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_variants`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductVariants.php).

```text
[fy2press_product_variants]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 602 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_collections

Résultat attendu : Les collections associées au produit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_collections`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductCollections.php).

```text
[fy2press_product_collections]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 353 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_add_to_cart

Résultat attendu : Un contrôle d’ajout au panier ; son rendu seul ne prouve pas une requête panier.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_add_to_cart`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/AddToCart.php).

```text
[fy2press_add_to_cart]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 1077 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_buy_now

Résultat attendu : Un contrôle d’achat direct ; le paiement connecté est hors de cette observation locale.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_buy_now`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/BuyNow.php).

```text
[fy2press_buy_now]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 475 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `text` | str | `"Buy Now"` |
| `class` | str | `"shopipress-buy-now-btn shopipress-d-buy-now-btn"` |
| `target` | str | `"_self"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_related_products

Résultat attendu : Une liste de produits associés lorsque le contexte les fournit.

Contexte : `product`. FREE 1.0.0. Alias de compatibilité : `shopipress_related_products`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/RelatedProducts.php).

```text
[fy2press_related_products limit="4"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 4305 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `id` | str | `""` |
| `limit` | int | `4` |
| `title` | str | `"You may also like"` |
| `orderby` | str | `"date"` |
| `class` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection

Résultat attendu : Un composant collection pour le handle fourni.

Contexte : `anywhere`. FREE 1.0.0. Alias de compatibilité : `shopipress_collection`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/Collection.php).

```text
[fy2press_collection handle="morrowfield"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 6155 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_products_loop

Résultat attendu : Une grille de produits selon la limite, les colonnes et la collection configurées.

Contexte : `anywhere`. FREE 1.0.0. Alias de compatibilité : `shopipress_products_loop`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/ProductsLoop.php).

```text
[fy2press_products_loop collection="morrowfield" limit="12"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 3207 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `limit` | int | `24` |
| `columns` | int | `4` |
| `collection` | str | `""` |
| `class` | str | `"shopipress-d-products-loop"` |
| `item_class` | str | `"shopipress-product-card"` |
| `pagination` | str | `"infinite"` |
| `sort_by` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_title

Résultat attendu : Le titre de la collection courante.

Contexte : `collection`. FREE 1.0.0. Alias de compatibilité : `shopipress_collection_title`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionTitle.php).

```text
[fy2press_collection_title]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 90 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `tag` | str | `"h1"` |
| `class` | str | `"shopipress-collection-title shopipress-d-collection-title"` |
| `prefix` | str | `""` |
| `suffix` | str | `""` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_description

Résultat attendu : La description de la collection courante.

Contexte : `collection`. FREE 1.0.0. Alias de compatibilité : `shopipress_collection_description`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionDescription.php).

```text
[fy2press_collection_description]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 161 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-description shopipress-d-collection-description"` |
| `wrapper` | str | `"div"` |
| `hide_if_empty` | bool | `true` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_sort

Résultat attendu : Un contrôle de tri des résultats produit de la collection.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_collection_sort`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/collection/CollectionSort.php).

```text
[fy2press_collection_sort]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 822 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `class` | str | `"shopipress-collection-sort"` |
| `label` | str | `"Sort by:"` |
| `show_label` | bool | `true` |
| `default_option` | str | `"Sort by..."` |
| `wrapper` | str | `"div"` |
| `wrapper_class` | str | `"shopipress-sort-wrapper shopipress-d-collection-sort"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_product_search

Résultat attendu : Un champ de recherche associé à une boucle de produits.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_product_search`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/ProductSearch.php).

```text
[fy2press_product_search]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 482 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_collection_filter

Résultat attendu : Un filtre de collection associé à une boucle de produits.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_collection_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/CollectionFilter.php).

```text
[fy2press_collection_filter type="dropdown"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 425 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_tag_filter

Résultat attendu : Un filtre d’étiquettes selon ses valeurs déclarées ou le type du design enregistré.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_tag_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/TagFilter.php).

```text
[fy2press_tag_filter type="tags"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 226 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

Défaut dynamique : le type du filtre d’étiquettes vient du design sauvegardé valide ; sinon `tags`.

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_filter_sidebar

Résultat attendu : Un panneau de filtres pour un contexte de boucle compatible.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_filter_sidebar`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/FilterSidebar.php).

```text
[fy2press_filter_sidebar][fy2press_product_search][fy2press_collection_filter][/fy2press_filter_sidebar]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 1234 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

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

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_price_filter

Résultat attendu : Un filtre de prix pour les résultats produit associés.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_price_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/PriceFilter.php).

```text
[fy2press_price_filter min="0" max="250"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 3186 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `min` | str | `"0"` |
| `max` | str | `"1000"` |
| `default_min` | str | `"0"` |
| `default_max` | str | `"250"` |
| `step` | str | `"10"` |
| `currency` | str | `"auto"` |
| `title` | str | `"Filter by Price"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

## fy2press_availability_filter

Résultat attendu : Un filtre de disponibilité pour les résultats produit associés.

Contexte : `loop`. FREE 1.0.0. Alias de compatibilité : `shopipress_availability_filter`. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/filters/AvailabilityFilter.php).

```text
[fy2press_availability_filter type="checkbox"]
```

<details>
<summary>Détails de l’essai local</summary>

Trace de l’essai local : 511 octets retournés, 0 octets imprimés hors retour. chaîne HTML.

</details>

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `type` | str | `"tags"` |
| `options` | str | `"in_stock,out_of_stock"` |
| `title` | str | `"Availability"` |
| `show_count` | str | `"yes"` |
| `class` | str | `"availability-filter-container"` |

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé ; une donnée absente peut produire un remplacement ou aucune sortie.

[Observation](../../sources/developer-observation.json) · [Package](../../artefacts/release-reference.json).
