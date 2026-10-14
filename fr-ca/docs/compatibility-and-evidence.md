# Compatibilité et preuves

[English](../../docs/compatibility-and-evidence.md) · [Accueil](../README.md)

Utiliser une preuve pour la question à laquelle elle répond. Un essai local de callback démontre un contrat de rendu local, pas un paiement Shopify complet ou une compatibilité universelle avec les thèmes.

| Observation | Artefact et environnement | Producteur/date | Portée |
| --- | --- | --- | --- |
| Téléchargement officiel identifié | FREE 1.0.0; 488 fichiers; SVN 3744276; hash ZIP complet dans la référence de version | Codex, 2026-10-14 | Octets fournisseur collectés; aucune reconstruction depuis une autre révision. |
| Activation | WordPress 7.1 / PHP 8.4, WordPress Docker jetable | Codex, 2026-10-14 | Activation locale sans réseau externe. |
| Registre natif | 17 blocs, 27 shortcodes canoniques et 27 alias | Codex, 2026-10-14 | Inscriptions WordPress réelles; les alias ne sont pas comptés comme fonctions supplémentaires. |
| Exemples de composants | do_blocks/do_shortcode natifs, données fictives | Codex, 2026-10-14 | Sortie, contexte et limites par entrée; aucune boutique connectée. |
| Modes du shortcode URL | URL scalaire et lien HTML | Codex, 2026-10-14 | Deux modes observés en contexte produit local. |
| Descriptions PRO | Observations de l’éditeur, version 1.0.0 | Dates conservées dans le registre de sources | Ni runtime PRO sous licence ni identité du paquet courant revérifiés ici. |
| Paiement ou planification connectés | Aucune boutique réelle, transaction ou licence activée | Non exécuté | Ni défaut établi ni parcours commercial réussi. |

Le ZIP WordPress courant diffère du reçu précédent de l’éditeur. La comparaison SVN de 3742640 à 3744276 indique uniquement `readme.txt`; la version reste 1.0.0. L’ancien reçu n’est pas réécrit comme s’il avait observé les octets actuels.

La déclaration de version testée de l’API diffère de celle du readme. Aucune n’est un essai de compatibilité. L’environnement WordPress/PHP réellement utilisé demeure explicite. [Versions et divergences](../../artefacts/release-reference.json).

Le shortcode de type produit a retourné une chaîne vide avec la fixture locale normalisée. Son exemple demeure une sortie vide observée, pas la démonstration d’un type produit rempli. Les autres callbacks HTML ne prouvent pas les interactions navigateur. Tester les versions précises des thèmes, extensions SEO et constructeurs avant acceptation client.

[Observation détaillée](../../sources/developer-observation.json) · [Référence développeur](../developer/README.md) · [Actualisation des données](data-ownership-and-freshness.md).
