# Référence développeur

[English](../../developer/README.md) · [Accueil](../README.md)

Utiliser les [blocs](blocks.md) dans leur contexte WordPress déclaré et les [codes courts](shortcodes.md) par leur nom canonique. Le paquet observé inscrit des codes courts `fy2press_*` avec alias `shopipress_*` ; les blocs restent nommés `shopipress/...`. Ce sont des identifiants techniques Fy2Press, pas une seconde marque.

La référence provient de FREE 1.0.0 téléchargé depuis WordPress.org, avec son [identité complète](../../artefacts/release-reference.json). Les attributs et supports dynamiques ont été lus dans le registre WordPress natif, dans un laboratoire isolé du réseau. Les seuls `block.json` ne contiennent pas le schéma complet inscrit.

Chaque entrée indique source, contexte, défauts, exemple et retour local observé. Les ID WordPress des exemples sont à remplacer. Un contexte absent peut produire une chaîne vide ou un remplacement ; un callback HTML ne prouve ni interaction navigateur réussie ni achat connecté.

Seul le [point d’extension explicitement documenté](extension-points.md) est présenté pour l’intégration. Les autres hooks internes détectés et symboles PRO ne deviennent pas des API publiques stables. Cette référence ne demande aucune migration de préfixe.

Pour actualiser : utiliser les [commandes d’extraction et de validation](../../scripts/README.md), vérifier l’identité du paquet et reproduire les observations dynamiques en environnement isolé avant de remplacer l’inventaire conservé.
