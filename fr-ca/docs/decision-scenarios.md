# Huit décisions de projet

[English](../../docs/decision-scenarios.md) · [Accueil](../README.md)

Choisir la plus petite architecture qui répond au projet. Chaque scénario mène à une vérification.

## 1. Blogue existant

**Point de départ** Un éditeur possède des articles utiles et un catalogue Shopify.

**Décision** Quelques produits dans les articles ou des pages de catalogue natives ?

**Rôle et édition** Utiliser les blocs ou shortcodes FREE autour du texte. Séparer les articles des champs synchronisés.

**Contre-exemple** Un seul bouton intégré peut suffire pour un produit; un catalogue complet ajoute alors de l’entretien sans objectif clair.

**Vérification** Publier un article en préproduction. Vérifier contexte produit, liens et canonique propre à l’article.

## 2. Marque éditoriale

**Point de départ** Une marque combine un magazine et des collections commerciales.

**Décision** Qui gère les descriptions, les conseils et les prix ?

**Rôle et édition** Utiliser WordPress pour les guides originaux et Shopify pour les données produit. Commencer avec FREE; envisager PRO pour plusieurs designs ou les constructeurs natifs.

**Contre-exemple** Un guide contenant des liens produit n’est pas automatiquement équivalent à une fiche produit.

**Vérification** Modifier un titre source dans une boutique d’essai autorisée et synchroniser la préproduction. Vérifier le titre modifié et la conservation du guide.

## 3. Campagne saisonnière

**Point de départ** Une sélection saisonnière possède son introduction et sa navigation.

**Décision** La page restera-t-elle utile après l’événement ?

**Rôle et édition** Composer une collection et une page éditoriale dans FREE. Choisir PRO pour un besoin premium de présentation documenté.

**Contre-exemple** Ne pas supposer que l’extension archive les campagnes ou redirige les URL expirées.

**Vérification** Consigner la date de fin, le responsable et la décision de conserver, actualiser ou retirer la page; revérifier ensuite les liens.

## 4. Agence utilisant les blocs

**Point de départ** Une agence utilise l’éditeur natif WordPress.

**Décision** Le client peut-il entretenir la composition ?

**Rôle et édition** Commencer avec les blocs Gutenberg FREE. Distinguer les modèles produit des pages ordinaires contenant une boucle.

**Contre-exemple** Un bloc exigeant un contexte produit peut afficher un remplacement sur une page ordinaire.

**Vérification** Tester un modèle produit et une page ordinaire sur mobile. Inscrire les exigences de contexte dans la passation.

## 5. Agence utilisant un constructeur

**Point de départ** Un projet utilise Elementor ou WPBakery.

**Décision** Faut-il des contrôles natifs ou un shortcode suffit-il ?

**Rôle et édition** Les composants natifs appartiennent à PRO. L’insertion de shortcodes est une voie distincte. Les licences des constructeurs restent séparées.

**Contre-exemple** Ne pas promettre les contrôles Elementor natifs dans FREE ou la compatibilité avec toutes les versions.

**Vérification** Tester le thème, le constructeur et le modèle précis sous licence active autorisée. Vérifier le retour à FREE requis.

## 6. Catalogue à forte rotation

**Point de départ** Prix et inventaire changent plus vite que le contenu éditorial.

**Décision** Quel délai est acceptable pour chaque valeur affichée ?

**Rôle et édition** Définir les délais par chemin de données. FREE se synchronise manuellement; la planification PRO utilise cron WordPress et exige une qualification connectée bornée.

**Contre-exemple** Une requête produit au rendu n’actualise pas toutes les grilles, taxonomies, URL ou pages en cache.

**Vérification** Dans une boutique d’essai autorisée, modifier séparément prix, disponibilité de variante et titre. Mesurer grille, fiche et paiement; consigner le chemin le plus lent.

## 7. Plusieurs langues

**Point de départ** Une entreprise publie des guides dans plusieurs langues.

**Décision** Interface, pages éditoriales ou traductions du catalogue synchronisé ?

**Rôle et édition** Localiser les pages éditoriales avec les outils du site. Ni FREE ni la portée PRO documentée n’établissent la synchronisation multilingue du catalogue.

**Contre-exemple** Les traductions de l’administration ou les neuf langues du site ne prouvent pas un catalogue Shopify traduit.

**Vérification** Suivre un produit et un guide dans chaque langue, incluant URL et liens linguistiques. Garder explicites les besoins de traduction du catalogue non satisfaits.

## 8. Deux surfaces produit

**Point de départ** Des pages produit similaires existent dans Shopify et WordPress.

**Décision** Quelle URL sert le mieux la recherche et le parcours d’achat souhaités ?

**Rôle et édition** Évaluer l’équivalence et choisir une préférence par famille. FREE offre des contrôles de canonique produit et d’indexation; les taxonomies sont distinctes.

**Contre-exemple** Un réglage WordPress ne réécrit pas les canoniques Shopify et ne garantit pas le choix du moteur.

**Vérification** Comparer canoniques rendues, directives robots, sitemaps et liens sur les deux plateformes; consigner le choix du moteur lorsqu’il est disponible.

Suite : [installation](https://fy2press.com/fr-ca/docs/installation/), [connexion](https://fy2press.com/fr-ca/docs/connect-shopify/), [matrice SEO](seo-decision-matrix.md) et [passation](../reusable/agency-handover.md). Les devis B2B, le mapping ACF et la gestion multiboutique ne sont pas des capacités établies.
