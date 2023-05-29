# NLP_airline
NLP Project on Airline comments 
# Projet Python - Readme

Ce Readme fournit des informations sur un projet Python composé de trois exécutables : `scraping.py`, `pre_traitement.py` et `training_model.py`. Chaque exécutable joue un rôle spécifique dans le processus global du projet. Ce document est divisé en plusieurs parties conformément au format standard. Voici une description détaillée de chaque partie :

## 1. Introduction

Dans cette section, nous présentons une introduction générale au projet Python. Nous expliquons brièvement l'objectif global du projet et les principales fonctionnalités des exécutables.

## 2. Prérequis

Dans cette partie, nous décrivons les prérequis nécessaires pour exécuter le projet Python avec succès. Cela peut inclure les dépendances logicielles requises, les versions de Python compatibles, les bibliothèques externes nécessaires, etc.

## 3. Installation

Dans cette section, nous fournissons des instructions détaillées sur la procédure d'installation du projet Python. Cela peut inclure les étapes pour cloner le dépôt, installer les dépendances, configurer l'environnement, etc.

## 4. Utilisation

Dans cette partie, nous expliquons comment utiliser chaque exécutable du projet Python. Nous fournissons des instructions étape par étape sur la façon d'exécuter les fichiers et d'interagir avec eux. 

### 4.1. scraping.py

`scraping.py` est le premier fichier exécutable du projet. Son rôle principal est de collecter des données à partir de sources en ligne et de les stocker dans un fichier Excel. Ce fichier Excel servira ensuite de base pour étiqueter les données.

Pour exécuter `scraping.py`, suivez les étapes suivantes :

1. Assurez-vous d'avoir les prérequis nécessaires (voir section 2).
2. Exécutez la commande suivante dans votre terminal : `python scraping.py`.
3. Le script se connectera aux sources en ligne et collectera les données.
4. Une fois le processus terminé, un fichier Excel contenant les données sera généré.

### 4.2. pre_traitement.py

`pre_traitement.py` est le deuxième fichier exécutable du projet. Il effectue plusieurs étapes de prétraitement du texte sur les données labellisées extraites à partir du fichier Excel généré par `scraping.py`. Le prétraitement du texte comprend généralement des opérations telles que le nettoyage des données, la tokenization, la suppression des stopwords, etc. Ces étapes préparent les données pour l'entraînement du modèle.

Pour exécuter `pre_traitement.py`, suivez les étapes suivantes :

1. Assurez-vous d'avoir les prérequis nécessaires (voir section 2).
2. Placez le fichier Excel contenant les données labellisées dans le même répertoire que `pre_traitement.py`.
3. Exécutez la commande suivante dans votre terminal : `python pre_traitement.py`.
4. Le script effectuera les différentes étapes de prétraitement du texte sur les données.
5. Une fois le processus terminé, un fichier Excel contenant les données prétraitées sera généré.

### 4.3. training_model.py

`training_model.py` est le troisième et dernier fichier exécutable du projet. Il prend en entrée le fichier Excel contenant les données prétraitées et labellisées, puis entraîne un modèle utilisant l'algorithme KNN Classifier. Les prédictions du modèle sont ensuite renvoyées dans un autre fichier Excel.

Pour exécuter `training_model.py`, suivez les étapes suivantes :

1. Assurez-vous d'avoir les prérequis nécessaires (voir section 2).
2. Placez le fichier Excel contenant les données prétraitées et labellisées dans le même répertoire que `training_model.py`.
3. Exécutez la commande suivante dans votre terminal : `python training_model.py`.
4. Le script effectuera l'entraînement du modèle en utilisant l'algorithme KNN Classifier.
5. Une fois le processus terminé, un fichier Excel contenant les prédictions du modèle sera généré.

## 5. Contributions

Dans cette partie, nous expliquons comment les contributions au projet Python peuvent être effectuées. Cela peut inclure des informations sur le processus de pull request, les directives de style de codage, les tests unitaires, etc.

## 6. Problèmes connus

Dans cette section, nous répertorions les problèmes connus du projet Python. Cela peut inclure des bogues, des limitations, des erreurs courantes, etc. Nous fournissons également des solutions ou des contournements possibles si disponibles.

## 7. Licence

Dans cette partie, nous précisons la licence sous laquelle le projet Python est distribué. Cela peut inclure des informations sur les droits d'auteur, les autorisations, les clauses de non-responsabilité, etc.

## 8. Contact

Dans cette section, nous fournissons des informations de contact pour les développeurs ou les personnes responsables du projet Python. Cela peut inclure des adresses e-mail, des liens vers des profils GitHub, etc.

## 9. Remerciements

Dans cette partie, nous exprimons notre reconnaissance envers les personnes ou les organisations qui ont contribué au projet Python d'une manière ou d'une autre. Nous les remercions pour leur soutien, leurs conseils ou leurs contributions directes.

Ceci conclut le Readme pour le projet Python. Pour toute question ou assistance supplémentaire, veuillez vous référer à la section de contact.
