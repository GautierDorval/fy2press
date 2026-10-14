# Documented extension point

[Français canadien](../fr-ca/developer/extension-points.md) · [Start here](../README.md)

## Trusted reverse proxies

The distributed readme documents `shopipress_rate_limit_trusted_proxies`. The inspected `PublicAjaxRateLimiter` applies this filter to an empty array. It lets an operator name trusted proxy addresses before accepting forwarded visitor-address headers. This is a security-sensitive deployment choice.

```php
add_filter('shopipress_rate_limit_trusted_proxies', static function (array $proxies): array {
    // Example address only. Replace with a verified proxy you operate or trust.
    $proxies[] = '203.0.113.10';
    return $proxies;
});
```

Expected result: the returned array is considered when resolving trusted forwarded headers. This example is an original integration illustration, not a tested network deployment. Do not trust arbitrary forwarded headers or copy the example address into production. No wildcard or CIDR support is asserted here.

Observed contract: FREE 1.0.0, SVN 3744276. [Public implementation reference](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/PublicAjaxRateLimiter.php). Its presence in the public readme establishes a documented integration point for this version, not an indefinite compatibility promise.

## Internal hooks

Registration hooks, internal actions and builder adapters are not automatically public extension APIs. This reference deliberately omits their signatures. No PRO runtime is included or inferred from a function name.
