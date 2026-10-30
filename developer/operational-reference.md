# Operational reference

[Français canadien](../fr-ca/developer/operational-reference.md) · [Developer reference](README.md)

This page describes Fy2Press 1.1.0 as published in the FREE package on WordPress.org at [SVN revision 3774245](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/). It gathers the integration details that the WordPress.org listing links to. The PRO package of the same version is built from the same shared code. Source links point to that public revision.

These details describe the implementation, not a compatibility result for a particular site. The rest of this reference keeps its own scope: the block and shortcode inventory describes FREE 1.0.0.

## Catalog data and page caches

The main catalog and its filters, tag pages, tag filters and search use the synchronized WordPress catalog, including saved price and availability values, as do collection pages without a Storefront token.

Stored catalog records, component requests and page caches have separate refresh paths. After editing Shopify data, synchronize the saved records and refresh the relevant page cache when needed.

Synchronization can reapply Shopify-managed fields such as product titles and slugs. Existing WordPress post content is preserved by the documented synchronization behaviour, but the selected template must display it. New product pages are published directly rather than saved automatically as drafts: prepare the site's visibility before the first synchronization.

Sources: [catalog router](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/page-builders/shortcodes/collection/ProductsLoop.php), [product creation](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/controllers/SyncController.php).

## Trusted proxies

Public catalog and cart requests are rate-limited per client: by account for a logged-in user, otherwise by IP address. Behind a proxy or CDN, list trusted addresses with the `shopipress_rate_limit_trusted_proxies` filter; only they may supply `CF-Connecting-IP` or `X-Real-IP`, never `X-Forwarded-For`.

The filter returns an empty list by default, so no proxy is trusted automatically, including Cloudflare. Each entry is an exact IPv4 or IPv6 address or a CIDR range of the immediate proxy. A forwarded value that is not a valid IP address is ignored.

```php
add_filter('shopipress_rate_limit_trusted_proxies', static function (array $proxies): array {
    $proxies[] = '203.0.113.10';    // Example address: replace with your proxy.
    $proxies[] = '2001:db8::/32';   // Example range: replace with your proxy range.
    return $proxies;
});
```

Source: [rate limiter](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/PublicAjaxRateLimiter.php). The [documented extension point](extension-points.md) records the same filter as observed in FREE 1.0.0.

## Themes and templates

Theme titles (`.entry-title`, `.post-title`, `.page-title`, `.wp-block-post-title`) and featured images (`.post-thumbnail`, `img.wp-post-image`, `.wp-block-post-featured-image`) are hidden outside `.shopipress-template-content`; other classes need scoped CSS and mobile tests. Post title, image and date data stay intact.

In block themes, a template for Fy2Press content with Fy2Press blocks or shortcodes, even through a template part other than the header or footer, or blocks through a pattern, renders unchanged; otherwise the Fy2Press view fills its main region. Without one, pages use the theme's header and footer parts, not the template's own header or a sidebar.

Shortcodes expand in Shortcode, Paragraph, Heading and Classic blocks, nested ones too, not in dynamic output or data bindings; for lists, quotes, tables or other blocks, use a Shortcode block.

Check the site's actual theme, templates and mobile display before launch.

Source: [block-theme templates](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/BlockThemeTemplate.php).

## Uninstalling with WP-CLI

With **Delete Settings on Uninstall** enabled, settings and caches, not synchronized content, are removed only if an administrator deactivates, then deletes the plugin.

The documented WP-CLI command is `wp plugin uninstall fy2press --deactivate --user=<administrator>`. Replace `<administrator>` with an administrator account. The command removes those settings and caches permanently: run it only for a deliberate uninstall.

The cleanup runs from the Freemius SDK `after_uninstall` hook, and the package ships no `uninstall.php`. The bundled SDK registers that hook only when an administrator deactivates the plugin and runs it only for a user allowed to activate plugins. The command therefore deactivates and uninstalls in one step, with `--user`.

Sources: [plugin bootstrap](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/fy2press.php), [cleanup](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/bootstrap/Uninstall.php).

## Availability and cart checks

FREE and PRO check variant availability when components appear, when a variant is selected, after cart operations and when a visible tab returns after its observation expires. Results use a 45-second cache; there is no continuous polling or stock reservation. Out-of-stock sales allowed by Shopify and unknown quantities remain distinct.

Cart additions and updates display Shopify-confirmed quantities and restrictions. A retained line at quantity zero stays readable and removable; checkout is disabled when the cart's total quantity is zero. If a cart response is lost, Fy2Press reads the cart again without automatically repeating the mutation.

These checks update availability and cart feedback, not saved titles, prices, descriptions, collections or product structured data. Full synchronization and page-cache refresh remain separate. The 45-second cache is not a synchronization frequency.

Source: [availability store](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/AvailabilityStore.php).
