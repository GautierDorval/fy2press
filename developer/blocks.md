# Gutenberg blocks

[Français canadien](../fr-ca/developer/blocks.md) · [Index](README.md)

Generated from the native WordPress registry of FREE 1.0.0, SVN 3744276. Results below use fictional local data without Shopify requests. Defaults reflect the English lab locale; translatable strings can vary by locale.

Examples with `id="123"` require the real WordPress post ID. Product blocks normally need a product page; collection blocks need a collection archive. A products loop can be placed on an ordinary page.

## shopipress/title

Expected result: The product title.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductTitle.php).

```html
<!-- wp:shopipress/title /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 160 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/price

Expected result: The formatted product price from the available product data.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductPrice.php).

```html
<!-- wp:shopipress/price /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 101 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/description

Expected result: The product description in the current product context.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductDescription.php).

```html
<!-- wp:shopipress/description /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 248 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/image

Expected result: The main product image.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductImage.php).

```html
<!-- wp:shopipress/image /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 313 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/variants

Expected result: Variant-selection controls in a product context.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductVariants.php).

```html
<!-- wp:shopipress/variants /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 814 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/gallery

Expected result: The product image gallery.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductGallery.php).

```html
<!-- wp:shopipress/gallery /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 309 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/add-to-cart

Expected result: An add-to-cart control; a returned control alone does not prove a cart request.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/AddToCart.php).

```html
<!-- wp:shopipress/add-to-cart /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 916 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/availability

Expected result: The availability label from the available product data.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductAvailability.php).

```html
<!-- wp:shopipress/availability /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 478 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/vendor

Expected result: The product vendor label.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductVendor.php).

```html
<!-- wp:shopipress/vendor /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 202 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/collections

Expected result: The collections associated with the product.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductCollections.php).

```html
<!-- wp:shopipress/collections /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 465 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/tags

Expected result: The product’s tag list.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductTags.php).

```html
<!-- wp:shopipress/tags /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 378 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/buy-now

Expected result: A direct-purchase control; connected checkout is outside this local observation.

Context: `product`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductBuyNow.php).

```html
<!-- wp:shopipress/buy-now /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 655 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/collection-title

Expected result: The current collection title.

Context: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionTitle.php).

```html
<!-- wp:shopipress/collection-title /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 178 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/collection-description

Expected result: The current collection description.

Context: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionDescription.php).

```html
<!-- wp:shopipress/collection-description /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 274 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/products-loop

Expected result: A product grid with the configured limit, columns and collection.

Context: `anywhere`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/ProductsLoop.php).

```html
<!-- wp:shopipress/products-loop /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 3234 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/collection-sort

Expected result: A sorting control for the collection’s product results.

Context: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionSort.php).

```html
<!-- wp:shopipress/collection-sort /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 668 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

## shopipress/collection-products-per-page

Expected result: A control for the number of products displayed per collection page.

Context: `collection`. FREE 1.0.0. [Source](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/gutenberg/blocks/CollectionProductsPerPage.php).

```html
<!-- wp:shopipress/collection-products-per-page /-->
```

<details>
<summary>Local test details</summary>

Local test trace: 493 returned bytes, 0 bytes echoed outside the return. Returned HTML.

</details>

| Attribute | Type | Default / contract |
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

Registered supports:

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

Limit: local returned HTML does not qualify browser interactions, theme compatibility or connected checkout. Verify the declared context; missing data can produce a fallback or empty output.

[Observation](../sources/developer-observation.json) · [Package](../artefacts/release-reference.json).
