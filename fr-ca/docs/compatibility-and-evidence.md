# Compatibilité et preuves

[English](../../docs/compatibility-and-evidence.md) · [Accueil](../README.md)

Fy2Press a été testé avec une boutique Shopify réelle. Gautier Dorval a confirmé les essais de lancement nécessaires et le bon fonctionnement le 15 octobre 2026. Cette confirmation de l’éditeur décrit l’état courant des essais du produit; les observations locales datées ci-dessous gardent leur propre portée. Elle ne constitue pas une affirmation de compatibilité avec tous les thèmes ou toutes les versions.

## Ce qui a été vérifié

PAGUP maintient ce bilan. Les outils et méthodes utilisés figurent dans la [provenance éditoriale](../../THIRD-PARTY-NOTICES.md) et les [résultats détaillés](../../sources/developer-observation.json).

| Vérification | Version et environnement | Date | Ce que le résultat établit |
| --- | --- | --- | --- |
| Téléchargement officiel | FREE 1.0.0 ; 488 fichiers ; SVN 3744276 | 2026-10-14 | Le paquet téléchargé est identifié par son empreinte complète dans la référence de version. |
| Activation de l’extension | WordPress 7.1 / PHP 8.4, WordPress Docker jetable | 2026-10-14 | Activation locale sans réseau externe. |
| Registre des composants | 17 blocs, 27 codes courts canoniques et 27 alias de compatibilité | 2026-10-14 | Composants inscrits dans WordPress. Les alias ne sont pas des fonctions supplémentaires. |
| Contenu des composants | do_blocks/do_shortcode natifs avec des produits et une collection fictifs | 2026-10-14 | Le contenu retourné et le contexte sont consignés par composant. Aucune boutique connectée. |
| Code court d’URL produit | URL scalaire et lien HTML | 2026-10-14 | Les deux modes ont retourné la forme attendue en contexte produit local. |
| Descriptions PRO | Documentation publiée de la version 1.0.0 | Dates du [registre de sources](../../artefacts/source-lock.json) | Descriptions seulement ; ni l’exécution PRO sous licence ni le paquet PRO courant n’ont été revérifiés. |
| Confirmation de l’éditeur | Essais de lancement nécessaires avec une boutique Shopify réelle; fonctionnement confirmé | Confirmation du 2026-10-15 | Confirmation actuelle de l’éditeur. Les dates d’exécution, environnements détaillés et identité marchande ne sont ni fournis ni inventés. |

## Paquet et portée de compatibilité

Entre les révisions SVN 3742640 et 3744276, seul `readme.txt` a changé. Les deux paquets portent la version 1.0.0, mais leurs empreintes ZIP diffèrent. Chaque observation reste liée au paquet réellement examiné.

L’API WordPress.org et le readme du paquet déclarent des versions WordPress testées différentes. Ces déclarations ne constituent pas des essais de compatibilité. L’environnement réellement utilisé figure ci-dessus. [Détails des versions](../../artefacts/release-reference.json).

## Limite du code court de type de produit

`fy2press_product_type` est inscrit, mais n’a retourné aucun texte dans l’essai local, même si le produit fictif comportait un type. La lecture du même paquet FREE révèle une incohérence de nom de champ : [ShopifyService.php](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/ShopifyService.php) transforme `productType` en `product_type`, alors que [ProductType.php](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/page-builders/shortcodes/product/ProductType.php) lit `productType`.

Considérez l’affichage du type de produit comme une limite connue du parcours examiné. Le résultat vide est conservé par souci d’exactitude ; ce n’est pas un exemple rempli réussi. Un correctif local lit maintenant le champ normalisé et a réussi les vérifications WordPress synthétiques des deux noms du code court. Il n’a pas été distribué dans une nouvelle version du plugin; l’observation ci-dessus reste liée au parcours FREE 1.0.0 publié.

Pour les autres composants, un retour HTML ne vérifie pas à lui seul les interactions navigateur. Testez les versions précises du thème, de l’extension SEO et du constructeur avant l’acceptation client.

[Référence développeur](../developer/README.md) · [Actualisation des données](data-ownership-and-freshness.md).
