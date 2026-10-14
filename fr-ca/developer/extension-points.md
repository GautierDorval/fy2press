# Point d’extension documenté

[English](../../developer/extension-points.md) · [Accueil](../README.md)

## Mandataires inverses de confiance

Le readme distribué documente `shopipress_rate_limit_trusted_proxies`. Le service `PublicAjaxRateLimiter` inspecté applique ce filtre à un tableau vide. Il permet à l’exploitant de nommer les adresses des mandataires de confiance avant d’accepter les en-têtes d’adresse visiteur transmis. Ce choix touche la sécurité du déploiement.

```php
add_filter('shopipress_rate_limit_trusted_proxies', static function (array $proxies): array {
    // Adresse illustrative. Remplacer par un mandataire vérifié et de confiance.
    $proxies[] = '203.0.113.10';
    return $proxies;
});
```

Résultat attendu : le tableau retourné intervient dans la résolution des en-têtes transmis de confiance. Cet exemple original illustre l’intégration; ce n’est pas un déploiement réseau testé. Ne pas faire confiance aux en-têtes arbitraires ou copier cette adresse en production. Aucun support de joker ou de CIDR n’est affirmé ici.

Contrat observé : FREE 1.0.0, SVN 3744276. [Implémentation publique](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/PublicAjaxRateLimiter.php). Sa présence dans le readme établit un point documenté pour cette version, pas une promesse de compatibilité indéfinie.

## Hooks internes

Les hooks d’inscription, actions internes et adaptateurs de constructeurs ne deviennent pas automatiquement des API publiques. Cette référence omet leurs signatures. Aucun runtime PRO n’est inclus ou déduit d’un nom de fonction.
