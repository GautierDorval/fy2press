# Choose an edition

[Français canadien](../fr-ca/docs/editions-and-integrations.md) · [Start here](../README.md)

Start with the task. FREE is useful when you need a native WordPress catalog, Gutenberg composition, shortcodes, manual synchronization and one basic product/collection design. PRO is relevant when you need multiple templates, more design controls or native Elementor/WPBakery components.

The table below is generated from the reviewed publisher projection. “Delivered” describes the publisher’s implementation observation, not a connected test performed here. “Partial” retains a specific scope limit. [Source and version](../artefacts/source-lock.json).

<!-- generated:claims -->
| Use | Edition | Publisher state | Limit |
| --- | --- | --- | --- |
| Connect one Shopify store | FREE | delivered | Requires a public Storefront token; no multi-store management. |
| Publish native catalog records | FREE | delivered | Shopify owns commercial data; native records do not mean offline commerce. |
| Manually synchronize the catalog | FREE | partial | Start synchronization manually in FREE. Discovery resumes in batches; interrupted writes do not automatically resume. |
| Use included catalog templates | FREE | delivered | Verify the actual theme and page context. |
| Compose with public shortcodes | FREE | delivered | 27 canonical names plus compatibility aliases observed; aliases are not extra features. |
| Compose with Gutenberg blocks | FREE | delivered | 17 native registrations observed; product and collection contexts differ. |
| Search, filter, sort and paginate | FREE | delivered | Basic navigation, not saved advanced merchandising rules. |
| Configure a basic product and collection design | FREE | delivered | One design of each kind in FREE. |
| Present cart controls and continue to Shopify | FREE | delivered | Shopify checkout; no completed transaction tested here. |
| Run without WooCommerce | FREE | delivered | Shopify and WordPress services remain required. |
| Control catalog indexing and product URL preference | FREE | partial | Product canonical and taxonomy indexing are different controls; no ranking guarantee. |
| Retain FREE access when returning from PRO | FREE | partial | Partial scope; verify premium layout fallback and the chosen uninstall option. |
| Use native Elementor components | PRO | delivered | PRO and a separately licensed Elementor builder; use the native components included in the edition. |
| Use native WPBakery components | PRO | delivered | PRO and a separately licensed WPBakery builder; use the native components included in the edition. |
| Use advanced design controls | PRO | delivered | Publisher PRO observation; no licensed PRO runtime test here. |
| Customize components | PRO | delivered | Publisher PRO observation; validate the selected component and theme. |
| Adjust device-specific presentation | PRO | delivered | Publisher PRO observation; inspect actual mobile and desktop output. |
| Maintain multiple templates | PRO | delivered | Publisher PRO observation; document template assignments and downgrade behavior. |
| Add custom CSS | PRO | delivered | Publisher PRO observation; custom styling needs its own accessibility and mobile checks. |
| Schedule catalog synchronization | PRO | delivered | Active PRO licence; hourly, twice daily or daily through WP-Cron. WordPress must execute scheduled events; no real-time webhook service. |
<!-- /generated:claims -->

## Integration prerequisites

You need WordPress hosting, an existing Shopify subscription and a public Storefront API token. Never substitute a private Storefront or Admin API token. Native Elementor/WPBakery components require PRO and the relevant builder; those products have their own licences and version requirements. Putting a shortcode in an editor is not the same as a native builder integration.

PRO scheduled synchronization depends on an active licence and WordPress cron. It is not instant; qualification on live stores remains separate. This documentation did not test a commercial licence or download a current supplier PRO package. Multi-site licence allowances do not prove multi-store management features.

[Current offer and pricing](https://fy2press.com/product/). Prices are not duplicated here. For installation use [the setup guides](https://fy2press.com/docs/).
