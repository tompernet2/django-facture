# 🧾 Application Django de gestion de factures

Cette application web permet de gérer des produits et de créer des factures à partir d’une sélection de produits. 
Elle a été développée avec Django.

---------------------

Objectif : 
- Une interface claire pour créer/mettre à jour/supprimer des produits.
- Les produits ont une id,un nom, un prix et une date de péremption.
- Un système de facturation : il faut pouvoir sélectionner des produis qui formerons unefacture, prévoir une page avec les détail de la facture (nombre de produits, total à payer...)
- Un système de pagination pour naviguer dans les listes de produits et de facture

---------------------

## 🚀 Fonctionnalités principales

- 🛒 CRUD complet sur les produits (ajout, modification, suppression, affichage)
- 📄 Création de factures à partir de produits sélectionnés
- 📋 Liste des factures avec pagination
- 🧾 Détail d’une facture avec tous les produits inclus
- ✅ Vérification de la sélection d’au moins un produit avant création de facture
- ⚠️ Affichage de messages d’erreur et de succès avec Django messages
- 🧠 Interface utilisateur propre avec Tailwind CSS

---------------------

## 🧰 Technologies utilisées

- **Backend :** Django 
- **Frontend :** HTML5, Tailwind CSS
- **Base de données :** SQLite (par défaut)
- **Autres :**
  - Django messages framework
  - Pagination Django intégrée
