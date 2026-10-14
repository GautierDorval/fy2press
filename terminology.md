# Terminology

[Français canadien](fr-ca/terminology.md) · [Start here](README.md)

## Native catalog

WordPress posts and taxonomies can be queried and edited. Images may remain remote and components may still request Shopify.

## Manual synchronization

An administrator starts a catalog update. A cached runtime request is a different operation.

## Discovery

Paginated reading of the remote catalog before reconciliation. A complete accepted snapshot differs from an incomplete attempt.

## Writing and resumption

Writing changes WordPress records. Discovery resumption and batched writes are separate contracts. Test the interrupted phase before claiming resumable writes.

## Scheduled

A PRO cron-triggered update depends on licence and scheduling conditions. It is not an instant webhook or live-store qualification.

## Cache

An observation retained for a duration and context, not proof that all catalog values are current.

## Canonical URL

A preferred URL for equivalent or very similar content. This SEO meaning differs from a reference source in documentation.

## Canonical shortcode and alias

In the observed public package, fy2press_* is canonical and shopipress_* remains a compatibility alias. Block IDs still use shopipress/. They do not name another product.

## Published, tested, proposed

A provider can publish a package while a policy remains proposed and a connected test remains not run. Keep these facts separate.
