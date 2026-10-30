# Référence opérationnelle

[English](../../developer/operational-reference.md) · [Référence développeur](README.md)

Cette page décrit Fy2Press 1.1.0 tel que publié dans le paquet FREE sur WordPress.org, à la [révision SVN 3774245](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/). Elle regroupe les précisions d’intégration vers lesquelles renvoie la fiche WordPress.org. Le paquet PRO de la même version est construit à partir du même code partagé. Les liens vers les sources visent cette révision publique.

Ces précisions décrivent l’implémentation ; elles ne constituent pas un résultat de compatibilité pour un site donné. Le reste de cette référence conserve sa propre portée : l’inventaire des blocs et des codes courts décrit FREE 1.0.0.

## Données du catalogue et caches des pages

Le catalogue principal et ses filtres, les pages et les filtres d’étiquettes ainsi que la recherche utilisent le catalogue synchronisé dans WordPress, y compris les prix et les disponibilités enregistrés. Il en va de même pour les pages de collection sans jeton Storefront.

Les enregistrements du catalogue, les requêtes des composants et les caches des pages suivent des mécanismes d’actualisation distincts. Après une modification dans Shopify, synchroniser les enregistrements et actualiser au besoin le cache des pages concernées.

La synchronisation peut réappliquer les champs gérés par Shopify, comme les titres et les slugs des produits. Le contenu WordPress existant des fiches est conservé selon le comportement de synchronisation documenté, mais le modèle choisi doit l’afficher. Les nouvelles fiches produits sont publiées directement, sans être enregistrées automatiquement comme brouillons : préparer la visibilité du site avant la première synchronisation.

Sources : [routeur du catalogue](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/page-builders/shortcodes/collection/ProductsLoop.php), [création des fiches](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/controllers/SyncController.php).

## Serveurs mandataires de confiance

Les requêtes publiques du catalogue et du panier sont limitées par client : par compte pour un utilisateur connecté, sinon par adresse IP. Derrière un serveur mandataire ou un CDN, inscrire les adresses de confiance au moyen du filtre `shopipress_rate_limit_trusted_proxies`. Seules ces adresses peuvent fournir `CF-Connecting-IP` ou `X-Real-IP` ; `X-Forwarded-For` n’est jamais utilisé.

Le filtre retourne une liste vide par défaut : aucun mandataire n’est donc considéré comme fiable automatiquement, Cloudflare compris. Chaque entrée est une adresse IPv4 ou IPv6 exacte, ou une plage CIDR, du mandataire immédiat. Une valeur transmise qui n’est pas une adresse IP valide est ignorée.

```php
add_filter('shopipress_rate_limit_trusted_proxies', static function (array $proxies): array {
    $proxies[] = '203.0.113.10';    // Adresse d’exemple : remplacer par celle du mandataire.
    $proxies[] = '2001:db8::/32';   // Plage d’exemple : remplacer par celle du mandataire.
    return $proxies;
});
```

Source : [limiteur de requêtes](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/PublicAjaxRateLimiter.php). Le [point d’extension documenté](extension-points.md) consigne le même filtre, tel qu’observé dans FREE 1.0.0.

## Thèmes et modèles

Les titres du thème (`.entry-title`, `.post-title`, `.page-title`, `.wp-block-post-title`) et les images à la une (`.post-thumbnail`, `img.wp-post-image`, `.wp-block-post-featured-image`) sont masqués à l’extérieur de `.shopipress-template-content`. Les autres classes exigent des règles CSS ciblées et des essais sur mobile. Les données du titre, de l’image et de la date restent intactes.

Dans un thème à blocs, un modèle de contenu Fy2Press qui contient des blocs ou des codes courts Fy2Press s’affiche sans modification. Les blocs ou codes courts placés dans une partie de modèle autre que l’en-tête ou le pied de page comptent aussi, de même que les blocs provenant d’une composition. Sinon, la vue Fy2Press remplit la zone principale du modèle. Sans un tel modèle, les pages utilisent les parties d’en-tête et de pied de page du thème, et non l’en-tête propre au modèle ou une barre latérale.

Les codes courts sont interprétés dans les blocs Code court, Paragraphe, Titre et Classique, y compris lorsqu’ils sont imbriqués, mais pas dans les sorties dynamiques ni dans les liaisons de données. Pour les listes, les citations, les tableaux et les autres blocs, utiliser un bloc Code court.

Vérifier le thème, les modèles et l’affichage mobile réels du site avant la mise en ligne.

Source : [modèles des thèmes à blocs](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/BlockThemeTemplate.php).

## Désinstallation avec WP-CLI

Lorsque **Supprimer les paramètres à la désinstallation** est activé, les paramètres et les caches sont supprimés seulement si un administrateur désactive puis supprime l’extension. Le contenu synchronisé est conservé.

La commande WP-CLI documentée est `wp plugin uninstall fy2press --deactivate --user=<administrator>`. Remplacer `<administrator>` par un compte administrateur. La commande supprime définitivement ces paramètres et ces caches : ne l’exécuter que pour une désinstallation voulue.

Le nettoyage s’exécute au moyen du hook `after_uninstall` du SDK Freemius, et le paquet ne contient aucun fichier `uninstall.php`. Le SDK inclus n’enregistre ce hook que lorsqu’un administrateur désactive l’extension et ne l’exécute que pour un utilisateur autorisé à activer des extensions. La commande désactive donc et désinstalle en une seule étape, avec `--user`.

Sources : [amorçage de l’extension](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/fy2press.php), [nettoyage](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/bootstrap/Uninstall.php).

## Vérifications de disponibilité et de panier

FREE et PRO vérifient la disponibilité des variantes lorsque les composants apparaissent, lorsqu’une variante est choisie, après les opérations de panier et lorsqu’un onglet redevient visible après l’expiration de son observation. Les résultats utilisent un cache de 45 secondes ; il n’y a ni interrogation continue ni réservation de stock. Les ventes en rupture de stock permises par Shopify et les quantités inconnues restent distinctes.

Les ajouts et les modifications du panier affichent les quantités et les restrictions confirmées par Shopify. Une ligne conservée à quantité nulle reste lisible et peut être retirée ; le passage à la caisse est désactivé lorsque la quantité totale du panier est nulle. Si une réponse du panier est perdue, Fy2Press relit le panier sans répéter automatiquement la modification.

Ces vérifications actualisent la disponibilité et les retours du panier, mais pas les titres, les prix, les descriptions, les collections ni les données structurées enregistrés des produits. La synchronisation complète et l’actualisation du cache des pages demeurent distinctes. Le cache de 45 secondes n’est pas une fréquence de synchronisation.

Source : [registre des disponibilités](https://plugins.svn.wordpress.org/!svn/bc/3774245/fy2press/tags/1.1.0/admin/services/AvailabilityStore.php).
