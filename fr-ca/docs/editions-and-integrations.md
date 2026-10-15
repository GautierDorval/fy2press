# Choisir une édition

[English](../../docs/editions-and-integrations.md) · [Accueil](../README.md)

Commencer par la tâche. FREE convient à un catalogue WordPress natif, à la composition Gutenberg, aux codes courts, à la synchronisation manuelle et à un design de base produit/collection. PRO devient pertinent pour plusieurs modèles, davantage de réglages de design ou des composants Elementor/WPBakery natifs.

Le tableau est généré depuis la projection relue de l’éditeur. « Livré » décrit son observation d’implémentation, pas un essai connecté réalisé ici. « Partiel » conserve une limite précise. [Sources et version](../../artefacts/source-lock.json).

<!-- generated:claims -->
| Usage | Édition | État de l’éditeur | Limite |
| --- | --- | --- | --- |
| Connecter une boutique Shopify | FREE | livré | Exige un jeton Storefront public ; aucune gestion multiboutique. |
| Publier des fiches de catalogue natives | FREE | livré | Shopify gère les données commerciales ; les fiches natives ne rendent pas le commerce hors ligne. |
| Synchroniser manuellement le catalogue | FREE | partiel | Statut partiel de l’éditeur ; découverte, écriture et reprise exigent des vérifications distinctes. Aucun essai connecté de reprise ici. |
| Utiliser les modèles de catalogue inclus | FREE | livré | Vérifier le thème réel et le contexte de page. |
| Composer avec les codes courts publics | FREE | livré | 27 noms canoniques et leurs alias observés ; les alias ne sont pas des fonctions supplémentaires. |
| Composer avec les blocs Gutenberg | FREE | livré | 17 inscriptions natives observées ; les contextes produit et collection diffèrent. |
| Rechercher, filtrer, trier et paginer | FREE | livré | Navigation de base, sans règles avancées de présentation sauvegardées. |
| Configurer un design de base produit et collection | FREE | livré | Un design de chaque type dans FREE. |
| Présenter le panier et poursuivre dans Shopify | FREE | livré | Paiement Shopify ; aucune transaction terminée testée ici. |
| Fonctionner sans WooCommerce | FREE | livré | Les services Shopify et WordPress restent nécessaires. |
| Régler l’indexation et la préférence d’URL produit | FREE | partiel | Canonique produit et indexation des taxonomies sont distinctes ; aucun classement garanti. |
| Conserver FREE après un retour de PRO | FREE | partiel | Portée partielle ; vérifier le remplacement des designs premium et l’option de désinstallation. |
| Utiliser les composants Elementor natifs | PRO | livré | PRO et constructeur sous licence distincte ; combinaison exacte sous licence non testée ici. |
| Utiliser les composants WPBakery natifs | PRO | livré | PRO et constructeur sous licence distincte ; combinaison exacte sous licence non testée ici. |
| Utiliser les réglages de design avancés | PRO | livré | Observation PRO de l’éditeur ; aucun essai runtime PRO sous licence ici. |
| Personnaliser les composants | PRO | livré | Observation PRO de l’éditeur ; valider composant et thème choisis. |
| Ajuster la présentation selon l’appareil | PRO | livré | Observation PRO de l’éditeur ; inspecter le rendu mobile et ordinateur réel. |
| Entretenir plusieurs modèles | PRO | livré | Observation PRO de l’éditeur ; consigner les affectations et le retour à FREE. |
| Ajouter du CSS personnalisé | PRO | livré | Observation PRO de l’éditeur ; vérifier accessibilité et mobile du style ajouté. |
| Planifier la synchronisation du catalogue | PRO | partiel | Licence PRO active et cron WordPress ; non instantané. La qualification en boutique réelle n’est pas établie par cette référence. |
<!-- /generated:claims -->

## Prérequis d’intégration

Il faut un hébergement WordPress, un abonnement Shopify existant et un jeton Storefront API public. Ne jamais lui substituer un jeton Storefront privé ou Admin API. Les composants natifs Elementor/WPBakery exigent PRO et le constructeur concerné ; ces produits ont leurs propres licences et exigences de version. Insérer un code court dans un éditeur ne constitue pas une intégration native.

La synchronisation PRO planifiée dépend d’une licence active et de cron WordPress. Elle n’est pas instantanée ; la qualification en boutique réelle reste distincte. Ce travail n’a testé aucune licence commerciale ni téléchargé de paquet PRO fournisseur actuel. Une licence multisite ne prouve pas une fonction de gestion multiboutique.

[Offre et prix actuels](https://fy2press.com/fr-ca/product/). Les prix ne sont pas recopiés ici. Utiliser les [guides de configuration](https://fy2press.com/fr-ca/docs/).
