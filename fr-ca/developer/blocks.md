# Blocs Gutenberg

[English](../../developer/blocks.md) · [Index](README.md)

Généré depuis le registre WordPress natif du paquet FREE 1.0.0, SVN 3744276. Les résultats ci-dessous proviennent de données fictives locales, sans requête Shopify. Les valeurs par défaut sont celles du laboratoire en anglais; les textes traduisibles peuvent différer selon la langue.

Les exemples avec `id="123"` exigent l’ID WordPress réel. Les blocs produit exigent normalement une fiche produit; les blocs collection exigent une archive de collection. Une boucle peut être placée sur une page ordinaire.

## shopipress/title

Résultat attendu: Le titre du produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductTitle.php).

```html
<!-- wp:shopipress/title /-->
```

Trace de l’essai local: 160 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `htmlTag` | string | `"h1"` |
| `fallbackText` | string | `"Product title will appear here"` |
| `textAlign` | string | `"left"` |
| `textColor` | string | `"#333333"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontSize` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": false,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true,
    "__experimentalTextTransform": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/price

Résultat attendu: Le prix formaté selon les données produit disponibles.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductPrice.php).

```html
<!-- wp:shopipress/price /-->
```

Trace de l’essai local: 101 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `showCurrency` | boolean | `true` |
| `showComparePrice` | boolean | `true` |
| `priceFormat` | string | `"default"` |
| `fallbackText` | string | `"Price will appear here"` |
| `textAlign` | string | `"left"` |
| `comparePriceColor` | string | `"#999999"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontSize` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true,
    "__experimentalTextTransform": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/description

Résultat attendu: La description du produit dans le contexte courant.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductDescription.php).

```html
<!-- wp:shopipress/description /-->
```

Trace de l’essai local: 248 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `showExcerpt` | boolean | `false` |
| `wordLimit` | number | `0` |
| `stripHtml` | boolean | `false` |
| `fallbackText` | string | `"Product description will appear here"` |
| `textAlign` | string | `"left"` |
| `fontSize` | string | `"medium"` |
| `customFontSize` | number | `16` |
| `textColor` | string | `""` |
| `backgroundColor` | string | `""` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true,
    "__experimentalTextTransform": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/image

Résultat attendu: L’image principale du produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductImage.php).

```html
<!-- wp:shopipress/image /-->
```

Trace de l’essai local: 313 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `imageSize` | string | `"large"` |
| `linkToProduct` | boolean | `false` |
| `showCaption` | boolean | `false` |
| `altText` | string | `""` |
| `fallbackText` | string | `"Product image will appear here"` |
| `textAlign` | string | `"center"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/variants

Résultat attendu: Les contrôles de choix de variante dans un contexte produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductVariants.php).

```html
<!-- wp:shopipress/variants /-->
```

Trace de l’essai local: 814 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `displayStyle` | string | `"buttons"` |
| `showLabels` | boolean | `true` |
| `buttonStyle` | string | `"outline"` |
| `buttonSize` | string | `"medium"` |
| `textColor` | string | `"#333333"` |
| `backgroundColor` | string | `"#ffffff"` |
| `borderColor` | string | `"#dddddd"` |
| `hoverTextColor` | string | `"#333333"` |
| `hoverBackgroundColor` | string | `"#f5f5f5"` |
| `hoverBorderColor` | string | `"#333333"` |
| `activeTextColor` | string | `"#ffffff"` |
| `activeBackgroundColor` | string | `"#333333"` |
| `activeBorderColor` | string | `"#333333"` |
| `borderWidth` | number | `1` |
| `gap` | number | `10` |
| `borderRadius` | number | `4` |
| `fallbackText` | string | `"Product variants will appear here"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/gallery

Résultat attendu: La galerie d’images du produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductGallery.php).

```html
<!-- wp:shopipress/gallery /-->
```

Trace de l’essai local: 309 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `layout` | string | `"gallery"` |
| `thumbnailPosition` | string | `"bottom"` |
| `showThumbnails` | boolean | `true` |
| `showMainImage` | boolean | `true` |
| `enableLightbox` | boolean | `true` |
| `mainImageBorderRadius` | string | `"8px"` |
| `mainImageBoxShadow` | string | `"0 4px 12px rgba(0,0,0,0.1)"` |
| `mainImageMarginBottom` | string | `"15px"` |
| `thumbnailWidth` | string | `"70px"` |
| `thumbnailHeight` | string | `"70px"` |
| `thumbnailBorderRadius` | string | `"6px"` |
| `thumbnailGap` | string | `"8px"` |
| `thumbnailBorderColor` | string | `"transparent"` |
| `thumbnailActiveBorderColor` | string | `"#007cba"` |
| `thumbnailHoverScale` | string | `"1.05"` |
| `containerPosition` | string | `"sticky"` |
| `stickyTopOffset` | string | `"20px"` |
| `thumbnailAlignment` | string | `"center"` |
| `mobileThumbWidth` | string | `"50px"` |
| `mobileThumbHeight` | string | `"50px"` |
| `fallbackText` | string | `"Product gallery will appear here"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/add-to-cart

Résultat attendu: Un contrôle d’ajout au panier; son rendu seul ne prouve pas une requête panier.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/AddToCart.php).

```html
<!-- wp:shopipress/add-to-cart /-->
```

Trace de l’essai local: 916 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `buttonText` | string | `"Add to Cart"` |
| `showQuantity` | boolean | `true` |
| `quantityLabel` | string | `"Quantity:"` |
| `showPrice` | boolean | `false` |
| `unavailableText` | string | `"Unavailable"` |
| `fallbackText` | string | `"Add to cart button will appear here"` |
| `buttonSize` | string | `"medium"` |
| `buttonWidth` | string | `"full"` |
| `customWidth` | string | `""` |
| `alignment` | string | `"left"` |
| `backgroundColor` | string | `"#000000"` |
| `textColor` | string | `"#ffffff"` |
| `hoverBackgroundColor` | string | `"#333333"` |
| `hoverTextColor` | string | `"#ffffff"` |
| `fontSize` | string | `"0.9em"` |
| `fontWeight` | string | `"500"` |
| `textTransform` | string | `"uppercase"` |
| `letterSpacing` | string | `"0.05em"` |
| `borderRadius` | string | `"4px"` |
| `border` | string | `"none"` |
| `boxShadow` | string | `""` |
| `customPadding` | string | `"16px 32px"` |
| `customMargin` | string | `""` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "textTransform": true,
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": true,
      "fontWeight": true,
      "textTransform": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/availability

Résultat attendu: L’indication de disponibilité selon les données produit disponibles.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductAvailability.php).

```html
<!-- wp:shopipress/availability /-->
```

Trace de l’essai local: 478 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `displayType` | string | `"status"` |
| `statusStyle` | string | `"badge"` |
| `showIcon` | boolean | `false` |
| `inStockText` | string | `"In Stock"` |
| `outOfStockText` | string | `"Out of Stock"` |
| `lowStockText` | string | `"Only {quantity} left in stock"` |
| `lowStockThreshold` | number | `5` |
| `showQuantity` | boolean | `true` |
| `inStockColor` | string | `"#27ae60"` |
| `outOfStockColor` | string | `"#e74c3c"` |
| `lowStockColor` | string | `"#f39c12"` |
| `textColor` | string | `"#ffffff"` |
| `fontSize` | string | `"0.9em"` |
| `fontWeight` | string | `"500"` |
| `textTransform` | string | `"uppercase"` |
| `borderRadius` | string | `"4px"` |
| `padding` | string | `"6px 12px"` |
| `margin` | string | `"15px 0"` |
| `fallbackStatus` | string | `"in-stock"` |
| `fallbackQuantity` | number | `15` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": false
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "__experimentalFontFamily": true,
    "__experimentalTextTransform": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/vendor

Résultat attendu: Le nom du fournisseur du produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductVendor.php).

```html
<!-- wp:shopipress/vendor /-->
```

Trace de l’essai local: 202 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `htmlTag` | string | `"div"` |
| `showLabel` | boolean | `true` |
| `labelText` | string | `"BY:"` |
| `prefix` | string | `""` |
| `suffix` | string | `""` |
| `linkToVendor` | boolean | `false` |
| `vendorUrl` | string | `""` |
| `openInNewTab` | boolean | `false` |
| `textAlign` | string | `"left"` |
| `fallbackVendor` | string | `"Sample Brand"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `fontSize` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "link": true,
    "gradients": false
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "textTransform": true,
    "letterSpacing": true,
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/collections

Résultat attendu: Les collections associées au produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductCollections.php).

```html
<!-- wp:shopipress/collections /-->
```

Trace de l’essai local: 465 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `showLabel` | boolean | `true` |
| `labelText` | string | `"Collections:"` |
| `displayStyle` | string | `"inline"` |
| `separator` | string | `", "` |
| `maxCollections` | number | `0` |
| `linkToCollection` | boolean | `true` |
| `hideIfEmpty` | boolean | `true` |
| `textAlign` | string | `"left"` |
| `fontSize` | string | `"14px"` |
| `fontWeight` | string | `"400"` |
| `textDecoration` | string | `"underline"` |
| `linkColor` | string | `"#666666"` |
| `linkHoverColor` | string | `"#000000"` |
| `labelColor` | string | `"#333333"` |
| `labelFontWeight` | string | `"bold"` |
| `backgroundColor` | string | `""` |
| `margin` | string | `"0 0 15px 0"` |
| `padding` | string | `"0"` |
| `fallbackCollections` | array | `["Sample Collection 1","Sample Collection 2"]` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "link": true,
    "gradients": false
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "__experimentalFontFamily": true,
    "__experimentalTextDecoration": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/tags

Résultat attendu: La liste des étiquettes du produit.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductTags.php).

```html
<!-- wp:shopipress/tags /-->
```

Trace de l’essai local: 378 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `showLabel` | boolean | `true` |
| `labelText` | string | `"Tags:"` |
| `displayStyle` | string | `"inline"` |
| `separator` | string | `", "` |
| `showHash` | boolean | `false` |
| `maxTags` | number | `0` |
| `linkToTag` | boolean | `true` |
| `hideIfEmpty` | boolean | `true` |
| `textAlign` | string | `"left"` |
| `fontSize` | string | `"14px"` |
| `fontWeight` | string | `"400"` |
| `textDecoration` | string | `"underline"` |
| `linkColor` | string | `"#666666"` |
| `linkHoverColor` | string | `"#000000"` |
| `hashColor` | string | `"#999999"` |
| `labelColor` | string | `"#333333"` |
| `labelFontWeight` | string | `"bold"` |
| `backgroundColor` | string | `""` |
| `badgeBackgroundColor` | string | `"#f0f0f0"` |
| `badgeTextColor` | string | `"#333333"` |
| `badgePadding` | string | `"4px 8px"` |
| `badgeBorderRadius` | string | `"4px"` |
| `margin` | string | `"0 0 15px 0"` |
| `padding` | string | `"0"` |
| `fallbackTags` | array | `["casual","summer","comfortable"]` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "link": true,
    "gradients": false
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "__experimentalFontFamily": true,
    "__experimentalTextDecoration": true,
    "__experimentalDefaultControls": {
      "fontSize": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/buy-now

Résultat attendu: Un contrôle d’achat direct; le paiement connecté est hors de cette observation locale.

Contexte: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductBuyNow.php).

```html
<!-- wp:shopipress/buy-now /-->
```

Trace de l’essai local: 655 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `buttonText` | string | `"Buy Now"` |
| `linkTarget` | string | `"_blank"` |
| `customUrl` | string | `""` |
| `buttonSize` | string | `"medium"` |
| `buttonWidth` | string | `"full"` |
| `customWidth` | string | `""` |
| `alignment` | string | `"center"` |
| `backgroundColor` | string | `"#ffffff"` |
| `textColor` | string | `"#000000"` |
| `hoverBackgroundColor` | string | `"#f8f8f8"` |
| `hoverTextColor` | string | `"#000000"` |
| `fontSize` | string | `"0.9em"` |
| `fontWeight` | string | `"500"` |
| `textTransform` | string | `"uppercase"` |
| `letterSpacing` | string | `"0.05em"` |
| `textDecoration` | string | `"none"` |
| `borderRadius` | string | `"4px"` |
| `border` | string | `"1px solid #e1e1e1"` |
| `boxShadow` | string | `""` |
| `customPadding` | string | `"16px 32px"` |
| `customMargin` | string | `""` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "fontWeight": true,
    "textTransform": true,
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": true,
      "fontWeight": true,
      "textTransform": true
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/collection-title

Résultat attendu: Le titre de la collection courante.

Contexte: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionTitle.php).

```html
<!-- wp:shopipress/collection-title /-->
```

Trace de l’essai local: 178 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `htmlTag` | string | `"h1"` |
| `prefix` | string | `""` |
| `suffix` | string | `""` |
| `textAlign` | string | `"left"` |
| `textColor` | string | `"#333333"` |
| `fontSize` | string | `"28px"` |
| `backgroundColor` | string | `""` |
| `padding` | string | `"0"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": false,
    "gradients": true
  },
  "typography": {
    "fontSize": false,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true,
    "__experimentalTextTransform": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true,
    "__experimentalDefaultControls": {
      "fontSize": false
    }
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/collection-description

Résultat attendu: La description de la collection courante.

Contexte: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionDescription.php).

```html
<!-- wp:shopipress/collection-description /-->
```

Trace de l’essai local: 274 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `wrapper` | string | `"div"` |
| `hideIfEmpty` | boolean | `true` |
| `textAlign` | string | `"left"` |
| `textColor` | string | `"#666666"` |
| `fontSize` | string | `"16px"` |
| `backgroundColor` | string | `""` |
| `padding` | string | `"0"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": false,
    "gradients": true
  },
  "typography": {
    "fontSize": false,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true,
    "__experimentalTextDecoration": true,
    "__experimentalLetterSpacing": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/products-loop

Résultat attendu: Une grille de produits selon la limite, les colonnes et la collection configurées.

Contexte: `anywhere`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductsLoop.php).

```html
<!-- wp:shopipress/products-loop /-->
```

Trace de l’essai local: 3234 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `limit` | number | `12` |
| `columns` | number | `4` |
| `collection` | string | `""` |
| `showPagination` | boolean | `true` |
| `gap` | number | `20` |
| `showImage` | boolean | `true` |
| `showTitle` | boolean | `true` |
| `showPrice` | boolean | `true` |
| `showCartButton` | boolean | `true` |
| `cardBackgroundColor` | string | `"#ffffff"` |
| `cardBorderColor` | string | `"#eeeeee"` |
| `cardBorderWidth` | number | `1` |
| `cardBorderRadius` | number | `8` |
| `cardPadding` | number | `15` |
| `cardHoverShadow` | boolean | `true` |
| `cardBoxShadow` | boolean | `true` |
| `cardShadowColor` | string | `"rgba(0, 0, 0, 0.1)"` |
| `cardShadowHorizontal` | number | `0` |
| `cardShadowVertical` | number | `2` |
| `cardShadowBlur` | number | `4` |
| `cardShadowSpread` | number | `0` |
| `imageHeight` | number | `200` |
| `imageBorderRadius` | number | `4` |
| `imageHoverEffect` | boolean | `true` |
| `titleFontSize` | number | `16` |
| `titleFontWeight` | string | `"600"` |
| `titleColor` | string | `"#333333"` |
| `titleHoverColor` | string | `"#007cba"` |
| `titleMarginTop` | number | `10` |
| `titleMarginBottom` | number | `8` |
| `priceFontSize` | number | `16` |
| `priceFontWeight` | string | `"600"` |
| `priceColor` | string | `"#333333"` |
| `priceMarginBottom` | number | `8` |
| `buttonFontSize` | number | `14` |
| `buttonBackgroundColor` | string | `"#3498db"` |
| `buttonTextColor` | string | `"#ffffff"` |
| `buttonHoverBackgroundColor` | string | `"#2980b9"` |
| `buttonHoverTextColor` | string | `"#ffffff"` |
| `buttonBorderRadius` | number | `4` |
| `buttonPaddingVertical` | number | `8` |
| `buttonPaddingHorizontal` | number | `16` |
| `buttonMarginTop` | number | `8` |
| `buttonDisabledBackgroundColor` | string | `"#95a5a6"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/collection-sort

Résultat attendu: Un contrôle de tri des résultats produit de la collection.

Contexte: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionSort.php).

```html
<!-- wp:shopipress/collection-sort /-->
```

Trace de l’essai local: 668 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `label` | string | `"Sort by:"` |
| `showLabel` | boolean | `true` |
| `defaultOption` | string | `"Sort by..."` |
| `wrapper` | string | `"div"` |
| `alignment` | string | `"left"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontSize` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

## shopipress/collection-products-per-page

Résultat attendu: Un contrôle du nombre de produits affichés par page de collection.

Contexte: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionProductsPerPage.php).

```html
<!-- wp:shopipress/collection-products-per-page /-->
```

Trace de l’essai local: 493 octets retournés, 0 octets imprimés hors retour. HTML retourné.

| Attribut | Type | Défaut / contrat |
| --- | --- | --- |
| `options` | string | `"12,24,48,96"` |
| `defaultValue` | string | `"12"` |
| `label` | string | `"Products per page:"` |
| `showLabel` | boolean | `true` |
| `wrapper` | string | `"div"` |
| `alignment` | string | `"left"` |
| `className` | string | `""` |
| `anchor` | string | `""` |
| `lock` | object | `{"default_not_declared":true}` |
| `metadata` | object | `{"default_not_declared":true}` |
| `align` | string | `{"default_not_declared":true}` |
| `style` | object | `{"default_not_declared":true}` |
| `backgroundColor` | string | `{"default_not_declared":true}` |
| `textColor` | string | `{"default_not_declared":true}` |
| `gradient` | string | `{"default_not_declared":true}` |
| `fontSize` | string | `{"default_not_declared":true}` |
| `fontFamily` | string | `{"default_not_declared":true}` |
| `borderColor` | string | `{"default_not_declared":true}` |

Supports inscrits:

```json
{
  "html": false,
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "alignWide": true,
  "anchor": true,
  "className": true,
  "color": {
    "background": true,
    "text": true,
    "gradients": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true,
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalFontStyle": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  }
}
```

Limite : un retour HTML local ne qualifie ni interactions navigateur, ni thème, ni paiement connecté. Vérifier le rendu dans le contexte annoncé; une donnée absente peut produire un remplacement ou aucune sortie.

[Observation](../../sources/developer-observation.json) · [Package](../../artefacts/release-reference.json).
