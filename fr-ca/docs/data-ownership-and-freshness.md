# Propriété et actualisation des données

[English](../../docs/data-ownership-and-freshness.md) · [Accueil](../README.md)

Gérez les informations commerciales dans Shopify et rédigez les guides et contenus éditoriaux dans WordPress. Après un changement Shopify, synchronisez le catalogue enregistré et actualisez le cache de page concerné au besoin. Le tableau indique qui gère chaque valeur et comment elle atteint la page; données enregistrées, requêtes des composants et caches HTML peuvent être actualisés séparément.

| Donnée | Source de gestion et stockage | Lecteur au rendu | Actualisation et effet de synchronisation |
| --- | --- | --- | --- |
| Titre | Shopify ; titre de fiche et observation produit sauvegardés. | Les listes WordPress peuvent lire le titre sauvegardé ; les composants produit peuvent lire le cache. | La synchronisation peut réappliquer le titre. Une lecture produit ne prouve pas l’actualisation de tous les titres. |
| Slug / handle | Handle Shopify ; post_name WordPress et métadonnées produit. | Routes WordPress et génération d’URL produit. | La synchronisation peut le réappliquer. WordPress peut conserver les anciens slugs; les redirections dépendent du type de page et de la configuration. Vérifiez les liens existants importants. |
| Description source | Description Shopify ; cache et métadonnées produit. | TemplateDataProvider et composant de description choisi. | Une lecture produit peut actualiser son observation. Ne pas la confondre avec le texte éditorial WordPress conservé. |
| Contenu éditorial WordPress | Éditeur WordPress ; post_content, pages et articles. | Le modèle choisi doit effectivement rendre ce contenu. | Le post_content existant est conservé par les mises à jour inspectées ; le thème et les composants déterminent sa visibilité. |
| Images | URL Shopify conservées dans les observations ; remplacement WordPress possible. | Le navigateur demande l’URL émise par le composant. | Aucun miroir local des médias n’est établi. HTML en cache et service d’image distant ont des durées distinctes. |
| Prix de grille | Observation Shopify sauvegardée dans l’instantané de synchronisation et les métadonnées. | Carte produit et requêtes locales du catalogue. | Actualiser le chemin de synchronisation pertinent ; une requête de fiche ne prouve pas une grille actuelle. |
| Prix de variante | Variantes Shopify ; cache produit complet et observations d’offre synchronisées. | Les composants choisissent un prix observé ; le paiement constitue une observation Shopify distincte. | Le contexte et l’âge d’acquisition comptent. Changer un libellé de devise n’établit pas des prix par marché. |
| Disponibilité | Disponibilité des produits et variantes Shopify ; observations locales. | Cartes, contrôles de variantes et admissibilité au panier peuvent lire différentes observations. | Une donnée inconnue ou périmée ne prouve pas qu’une variante peut être achetée. L’acceptation au panier se vérifie séparément. |
| Collections | Relations Shopify ; termes et relations shopipress_collections. | Requêtes de taxonomie WordPress et composants de collection. | La synchronisation réconcilie l’appartenance. Vérifier les textes de termes modifiés localement en préproduction. |
| Étiquettes | Étiquettes Shopify ; termes et relations shopipress_tags. | Requêtes WordPress et filtres ; la politique d’indexation est distincte. | Une synchronisation peut modifier les relations ; un rendu produit ne prouve pas la réconciliation des taxonomies. |
| Panier | Service de panier Shopify ; références de session et interface locales. | Requêtes et réponses de panier, puis paiement Shopify. | La synchronisation du catalogue n’importe pas les commandes dans WordPress et ne certifie pas une transaction. |
| Données structurées produit | Identité produit locale et observation commerciale sélectionnée. | ProductSchemaService coordonne l’offre produit émise. | Comparer JSON-LD, prix visible, devise et disponibilité. Un JSON valide ne prouve ni inventaire actuel ni résultat enrichi. |

## Cache, interruptions et vérifications

Ces règles complètent chaque ligne du tableau :

- **Cache :** `CacheService` utilise un âge d’acquisition et un contexte. Le délai configuré observé par défaut est de 1 800 secondes ; ce n’est pas un retard fixe de trente minutes pour toutes les pages. Une page HTML ou un cache externe peut conserver d’autres valeurs. Restaurer un cache évincé ne rajeunit pas son observation.
- **Déclencheur :** les champs synchronisés changent pendant une synchronisation ; certains composants produit peuvent relire Shopify entre deux synchronisations. Les textes WordPress changent à l’enregistrement de l’éditeur ; le panier suit ses propres requêtes.
- **Interruption :** une découverte incomplète, une écriture interrompue et une erreur de lecture au rendu sont trois cas. Les composants peuvent conserver des données d’affichage anciennes sans les accepter comme preuve de variante achetable. Ne pas annoncer une reprise d’écriture à partir du seul mot « lots ».
- **Observations :** l’éditeur a confirmé les essais de lancement en boutique réelle le 15 octobre 2026. Le registre natif et les exemples locaux restent des observations datées du paquet identifié. L’attribution des sources ci-dessus décrit les services publics inspectés; aucun de ces relevés n’établit un délai universel d’actualisation.
- **Limite :** pour chaque ligne, relever sa valeur avant modification, l’heure de modification Shopify, la prochaine synchronisation, l’état du cache et la valeur réellement affichée. Une seule mesure sur une fiche ne qualifie pas la grille.

## Contrats de synchronisation distincts

La découverte parcourt les pages Shopify et prépare une observation du catalogue. L’écriture réconcilie les fiches WordPress, leurs états et leurs relations. La reprise d’une découverte n’établit pas celle d’une écriture. Le paquet courant contient des chemins de traitement en lots ; leur présence statique ne constitue pas un essai d’interruption.

FREE exige le lancement manuel. PRO permet une synchronisation chaque heure, deux fois par jour ou chaque jour avec WP-Cron et une licence active. WordPress doit exécuter les événements planifiés, par le trafic du site ou un ordonnanceur configuré. Ce n’est pas un service de webhooks en temps réel. Les files de webhooks et la synchronisation multilingue ne sont pas établies comme disponibles dans la portée de l’éditeur.

Pour accepter un catalogue à forte rotation, fixer un délai maximal par ligne et tester les changements séparément. Prévoir une vérification après purge de cache et après erreur réseau dans un environnement autorisé.

Sources inspectées : [SyncController](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/controllers/SyncController.php), [CacheService](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/CacheService.php), [TemplateDataProvider](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/TemplateDataProvider.php), [ProductSchemaService](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/ProductSchemaService.php). FREE 1.0.0, SVN 3744276.

[Modèle de passation](../reusable/agency-handover.md).
