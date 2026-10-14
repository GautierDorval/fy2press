# Morrowfield : collection, produit et guide

[English](../../examples/morrowfield.md) · [Accueil](../README.md)

## Composition visée

Un site éditorial fictif Morrowfield comporte trois rôles de page :

1. **Collection :** expliquer la sélection, puis afficher une boucle de produits pour le handle de collection.
2. **Produit :** présenter un produit synchronisé dans le bon contexte, son prix observé et son contrôle d’achat.
3. **Guide :** expliquer comment choisir. Conserver le texte original et l’URL propre du guide; relier les produits utiles.

## Composer la collection

Dans un bloc Shortcode WordPress, utiliser le nom public canonique :

```text
[fy2press_products_loop collection="morrowfield" limit="12" columns="3"]
```

Remplacer `morrowfield` par un handle de collection réellement synchronisée en préproduction. La boucle et ses filtres exigent un contexte compatible. Le prix de grille ne prouve pas un prix de paiement distant actuel.

Pour un produit sur une page ordinaire :

```text
[fy2press_product id="123"]
```

Remplacer `123` par l’**ID de fiche produit WordPress**, pas par un ID produit ou variante Shopify. Le composant complet peut différer d’un bloc Gutenberg exigeant un contexte produit. Consulter les [contrats des composants](../developer/README.md).

## Garder le travail éditorial explicite

Rédiger le guide comme contenu WordPress ordinaire : présenter les critères, expliquer deux usages et relier les fiches produit. Un guide n’est pas équivalent à un produit simplement parce qu’il le mentionne. Appliquer la [matrice SEO](../docs/seo-decision-matrix.md), décision SEO-03.

## Portée de la preuve

Le laboratoire documentaire utilisait deux fiches fictives et une collection. Les exemples de composants natifs ont été exécutés sans accès réseau Shopify. Cette page annotée les assemble dans une proposition éditoriale; aucun parcours navigateur de cette composition exacte de trois pages n’a été exécuté. Elle ne prouve ni synchronisation connectée, ni inventaire réel, ni paiement terminé.

Avant un usage client : synchroniser un catalogue d’essai autorisé, remplacer les ID, inspecter chaque page, tester la navigation mobile et vérifier le parcours panier/paiement selon son autorisation propre.
