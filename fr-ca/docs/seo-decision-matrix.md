# Matrice de décisions SEO

[English](../../docs/seo-decision-matrix.md) · [Accueil](../README.md)

Distinguer le lieu de gestion des données commerciales de l’URL qui devrait représenter une page dans la recherche. Les douze fiches suivantes forment une matrice de décision éditoriale; la ligne de contrôle Fy2Press indique la frontière d’implémentation. Les recommandations ne sont pas des résultats de classement mesurés.

Une canonique exprime une préférence pour des contenus identiques ou très similaires; elle ne garantit pas le choix du moteur. Ne pas utiliser robots.txt pour l’imposer ou combiner noindex et canonique comme recette automatique. [Consignes Google](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls). Un guide d’achat original conserve généralement sa propre URL.

## Choisir un cas

| Cas | Situation |
| --- | --- |
| [SEO-01](#seo-01--produit-similaire-shopify-prioritaire) | Produit similaire, Shopify prioritaire |
| [SEO-02](#seo-02--produit-wordpress-enrichi) | Produit WordPress enrichi |
| [SEO-03](#seo-03--guide-dachat-original) | Guide d’achat original |
| [SEO-04](#seo-04--collection-wordpress-utile) | Collection WordPress utile |
| [SEO-05](#seo-05--collections-concurrentes) | Collections concurrentes |
| [SEO-06](#seo-06--sélection-saisonnière) | Sélection saisonnière |
| [SEO-07](#seo-07--étiquettes-pauvres) | Étiquettes pauvres |
| [SEO-08](#seo-08--étiquettes-éditorialisées) | Étiquettes éditorialisées |
| [SEO-09](#seo-09--filtres-et-tri) | Filtres et tri |
| [SEO-10](#seo-10--variantes-sélectionnées) | Variantes sélectionnées |
| [SEO-11](#seo-11--indisponible-retiré-ou-renommé) | Indisponible, retiré ou renommé |
| [SEO-12](#seo-12--plusieurs-langues) | Plusieurs langues |

## SEO-01 · Produit similaire, Shopify prioritaire

| Critère | Décision |
| --- | --- |
| Objet | Produit |
| Contexte | Même offre et textes très similaires sur les deux plateformes. |
| Objectif du lecteur | Atteindre la page commerciale prioritaire. |
| Source commerciale | Shopify |
| Valeur éditoriale | Faible ajout éditorial WordPress. |
| Équivalence éventuelle | Vérifier la similarité; un même SKU ne suffit pas. |
| Préférence d’URL | URL produit Shopify si l’équivalence est justifiée. |
| Action WordPress | Activer l’indexation produit et choisir Shopify comme source de canonique produit; inspecter le rendu. |
| Action Shopify | Garder le produit prioritaire accessible et vérifier sa canonique, son sitemap et ses liens. |
| Contrôle Fy2Press | Source canonique produit FREE; ce n’est pas un réglage de collection. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Liens contradictoires ou destination Shopify indisponible. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-02 · Produit WordPress enrichi

| Critère | Décision |
| --- | --- |
| Objet | Produit |
| Contexte | WordPress ajoute des conseils substantiels propres au produit. |
| Objectif du lecteur | Lire une information d’achat plus riche. |
| Source commerciale | Shopify |
| Valeur éditoriale | Comparaison, usage ou conseils originaux. |
| Équivalence éventuelle | Évaluer le chevauchement; l’enrichissement peut changer l’intention. |
| Préférence d’URL | WordPress s’il s’agit de la page représentative souhaitée. |
| Action WordPress | Conserver WordPress comme source produit; vérifier la canonique propre avec l’extension SEO. |
| Action Shopify | Réviser Shopify séparément; Fy2Press n’en modifie pas la canonique. |
| Contrôle Fy2Press | Préférence produit FREE; modifications Shopify hors extension. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Supposer qu’une option locale consolide les deux sites. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-03 · Guide d’achat original

| Critère | Décision |
| --- | --- |
| Objet | Page éditoriale |
| Contexte | Un guide explique un choix entre plusieurs produits. |
| Objectif du lecteur | Comprendre un choix, puis visiter un produit. |
| Source commerciale | Shopify |
| Valeur éditoriale | Le guide lui-même constitue la valeur. |
| Équivalence éventuelle | Non équivalent à l’une de ses fiches produit liées. |
| Préférence d’URL | L’URL propre du guide. |
| Action WordPress | Utiliser les contrôles de page WordPress/SEO et relier les produits pertinents. |
| Action Shopify | Entretenir les destinations produit; les liens seuls n’exigent pas une canonique croisée. |
| Contrôle Fy2Press | Le réglage produit ne transforme pas un guide original en fiche produit. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Canonicaliser un guide utile vers un produit non équivalent. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-04 · Collection WordPress utile

| Critère | Décision |
| --- | --- |
| Objet | Archive de collection |
| Contexte | Un blogue exige une sélection navigable avec une introduction utile. |
| Objectif du lecteur | Explorer un ensemble pertinent. |
| Source commerciale | Shopify |
| Valeur éditoriale | Justification de la sélection et liens internes. |
| Équivalence éventuelle | Évaluer l’ensemble de la sélection et l’introduction. |
| Préférence d’URL | URL de collection WordPress distincte et utile. |
| Action WordPress | Vérifier l’indexation des collections et la canonique de taxonomie émise par l’extension SEO. |
| Action Shopify | Réviser séparément la collection Shopify correspondante. |
| Contrôle Fy2Press | Indexation de collection FREE; aucun sélecteur de canonique de collection Shopify trouvé dans le service inspecté. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Appliquer le réglage de canonique produit aux taxonomies. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-05 · Collections concurrentes

| Critère | Décision |
| --- | --- |
| Objet | Archives de collection |
| Contexte | Deux pages ont le même nom, mais leurs produits ou introductions peuvent différer. |
| Objectif du lecteur | Trouver la sélection souhaitée. |
| Source commerciale | Shopify |
| Valeur éditoriale | Comparer portée, textes et objectifs de présentation. |
| Équivalence éventuelle | Un même nom ne prouve pas l’équivalence. |
| Préférence d’URL | Choisir après comparaison, pas selon une plateforme par défaut. |
| Action WordPress | Utiliser les contrôles de taxonomie vérifiés ou une implémentation canonique distincte si justifiée. |
| Action Shopify | Coordonner la collection correspondante et les liens avec son responsable. |
| Contrôle Fy2Press | L’indexation est disponible; la correspondance canonique automatique des collections n’est pas établie. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Consolider des pages d’intentions différentes. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-06 · Sélection saisonnière

| Critère | Décision |
| --- | --- |
| Objet | Page de campagne |
| Contexte | Un contenu et une navigation temporaires soutiennent une offre saisonnière. |
| Objectif du lecteur | Choisir selon l’occasion. |
| Source commerciale | Shopify |
| Valeur éditoriale | Contexte de campagne et sélection expliquée. |
| Équivalence éventuelle | Une campagne peut différer d’une collection permanente. |
| Préférence d’URL | URL de campagne tant qu’elle reste utile; consigner son cycle ultérieur. |
| Action WordPress | Publier un texte original et une boucle; planifier maintien, actualisation ou redirection justifiée. |
| Action Shopify | Entretenir disponibilité et offres produit. |
| Contrôle Fy2Press | Composition FREE; aucun contrat d’expiration automatique de campagne. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Pages saisonnières orphelines et offres périmées. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-07 · Étiquettes pauvres

| Critère | Décision |
| --- | --- |
| Objet | Archive d’étiquette |
| Contexte | Une étiquette automatique ajoute peu de navigation ou de contenu. |
| Objectif du lecteur | Éviter des destinations vides ou répétitives. |
| Source commerciale | Shopify |
| Valeur éditoriale | Faible valeur distincte. |
| Équivalence éventuelle | Ne pas choisir de canonique selon le seul libellé. |
| Préférence d’URL | Aucune URL cible de recherche avant d’établir son utilité. |
| Action WordPress | Vérifier l’indexation des étiquettes; le défaut observé est faux. Laisser explorer le noindex lorsque le retrait des résultats est souhaité. |
| Action Shopify | Réviser les étiquettes Shopify séparément; aucune politique de taxonomie n’y est envoyée. |
| Contrôle Fy2Press | Indexation des étiquettes FREE, distincte des produits et collections. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Employer robots.txt comme contrôle canonique. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-08 · Étiquettes éditorialisées

| Critère | Décision |
| --- | --- |
| Objet | Archive d’étiquette |
| Contexte | Une étiquette soutient un sujet réel avec contenu et navigation utiles. |
| Objectif du lecteur | Parcourir un sujet pertinent. |
| Source commerciale | Shopify |
| Valeur éditoriale | Explication originale du sujet et liens choisis. |
| Équivalence éventuelle | Vérifier le chevauchement avec collections et guides. |
| Préférence d’URL | URL d’étiquette utile, si la stratégie de taxonomie le justifie. |
| Action WordPress | Évaluer les conséquences avant d’activer l’option globale; inspecter toutes les archives touchées. |
| Action Shopify | Aucune action Shopify correspondante n’est implicite. |
| Contrôle Fy2Press | Réglage global FREE; exceptions par étiquette non établies ici. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Rendre toutes les étiquettes pauvres indexables pour un seul sujet utile. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-09 · Filtres et tri

| Critère | Décision |
| --- | --- |
| Objet | Résultats avec paramètres |
| Contexte | Les visiteurs filtrent prix, disponibilité ou recherche produit. |
| Objectif du lecteur | Trouver efficacement un produit. |
| Source commerciale | Shopify |
| Valeur éditoriale | Souvent un état de navigation, parfois une page conçue à cette fin. |
| Équivalence éventuelle | Le tri peut répéter un ensemble; les filtres peuvent le modifier. |
| Préférence d’URL | Décider séparément pour pages stables et résultats transitoires. |
| Action WordPress | Inspecter les URL à paramètres et leur rendu SEO; créer des pages utiles dédiées si justifié. |
| Action Shopify | Réviser séparément tout filtrage Shopify correspondant. |
| Contrôle Fy2Press | Les contrôles de navigation FREE n’établissent pas une politique canonique universelle des paramètres. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Indexer des combinaisons arbitraires ou masquer toutes les sélections utiles. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-10 · Variantes sélectionnées

| Critère | Décision |
| --- | --- |
| Objet | État de variante produit |
| Contexte | Une personne sélectionne une option dans un produit. |
| Objectif du lecteur | Voir le prix et la disponibilité correspondants. |
| Source commerciale | Shopify |
| Valeur éditoriale | Détails de variante, sans constituer nécessairement un document distinct. |
| Équivalence éventuelle | Vérifier si URL et contenu diffèrent réellement. |
| Préférence d’URL | Ne pas inventer de pages variantes natives. |
| Action WordPress | Vérifier ensemble sélection, prix visible, offre structurée et URL retournée. |
| Action Shopify | Confirmer la marchandise choisie et le contexte de paiement. |
| Contrôle Fy2Press | Les contrôles de variante existent; des routes natives de pages variantes distinctes ne sont pas établies. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Publier une offre incohérente avec la sélection visible. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-11 · Indisponible, retiré ou renommé

| Critère | Décision |
| --- | --- |
| Objet | Cycle de vie produit |
| Contexte | Rupture de stock, absence d’un catalogue complet ou modification du handle. |
| Objectif du lecteur | Comprendre si un article peut encore être acheté. |
| Source commerciale | Shopify |
| Valeur éditoriale | Des conseils de remplacement peuvent rester utiles. |
| Équivalence éventuelle | Indisponibilité, retrait et renommage sont des événements distincts. |
| Préférence d’URL | Évaluer l’URL utile conservée et les redirections au cas par cas. |
| Action WordPress | Vérifier statut et liens après synchronisation. Le code retire logiquement les absents, brouillon par défaut; ce n’est pas une suppression définitive. |
| Action Shopify | Confirmer l’événement source et les redirections marchandes. |
| Contrôle Fy2Press | Code de réconciliation FREE observé statiquement; cycle connecté non retesté ici. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Confondre rupture de stock et disparition ou supposer des redirections automatiques. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

## SEO-12 · Plusieurs langues

| Critère | Décision |
| --- | --- |
| Objet | Contenu et catalogue localisés |
| Contexte | Un guide et ses produits liés ciblent plusieurs langues. |
| Objectif du lecteur | Lire un contenu pertinent dans la langue souhaitée. |
| Source commerciale | Shopify |
| Valeur éditoriale | Travail éditorial original localisé. |
| Équivalence éventuelle | Une traduction n’est pas une duplication dans une même langue. |
| Préférence d’URL | URL et relations adaptées à chaque langue. |
| Action WordPress | Vérifier liens linguistiques et canoniques avec les outils de localisation. |
| Action Shopify | Vérifier séparément les langues et marchés de la boutique. |
| Contrôle Fy2Press | Traduction d’interface distincte de la synchronisation multilingue du catalogue, non disponible dans la portée annoncée. |
| Extension SEO | Inspecter l’extension SEO installée et sa version; des hooks enregistrés ne prouvent pas la compatibilité de toutes les versions. |
| Risques | Supposer qu’une interface traduite prouve la traduction des produits synchronisés. |
| Vérification | Inspecter canonique rendue, directives robots, présence au sitemap et liens internes; observer ensuite l’URL choisie par le moteur lorsque disponible. |
| Version | FREE 1.0.0 / SVN 3744276 |

Source des contrôles : [SEOIndexingService.php at SVN 3744276](https://plugins.svn.wordpress.org/!svn/bc/3744276/fy2press/tags/1.0.0/admin/services/SEOIndexingService.php). Statuts : [release reference](../../artefacts/release-reference.json).

[Remplir une décision SEO](../reusable/seo-decision-record.md).
