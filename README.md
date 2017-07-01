# Package-Twitter-pour-Constellation
Le package Twitter vous permet de récupérer les informations basiques de votre compte Twitter comme le nombre d’abonnés, le dernier tweet publié et autre.

Le package a été développé dans le cadre de la construction d'un réveil domotique.

## Installation
### Gestion des dépendances :
Le package tourne sous la version 2.7 de python qui doit être préalablement installé sur la machine cible.

Installation de python 2.7 : https://developer.myconstellation.io/getting-started/creez-votre-premier-package-constellation-en-python/#Installer_Python_sur_Windows

Il est ensuite nécessaire d’installation la bibliothèque python-twitter (https://github.com/bear/python-twitter) à l’aide de pip :

`$ sudo pip2 install python-twitter`

### Création de clés pour l'API Twitter
Le paquet demande des clés d'authentification de l'API Twitter pour fonctionner qu’il est possible de facilement récupérer sur le site suivant : https://apps.twitter.com/ 
Créez une nouvelle application puis dans la section « Keys and access tokens », générez une clé pour votre compte « Your access token ». Gardez bien ces deux numéros, ils vous seront utiles pour l’installation sur Constellation.

### Sur le serveur Constellation
Il vous suffit de récupérer le fichier Twitter.zip à la base du projet github et de le glisser dans votre console, dans la rubrique Package Repository / Upload Package.

Une fois le paquet installé, cliquez sur Depoloy Package sur la Sentinelle que vous souhaitez puis suivez les instructions, inutile de changer les paramètres par défaut.

### Avertissement :
L'API Twitter vous permet de faire jusqu'à 75 appels par tranche de 15 minutes avec les clés que vous avez donné à l'étape précédente. Si vous déployez plus de deux fois consécutive le paquet avec les mêmes identifiants, vous risquez de vous faire banir.

## Détails du package
### Les StateObjects
Vous retrouverez un seul StateObject, actualisé toutes les 30 secondes, avec les informations de votre compte sous forme d'un json. 

### Quelques exemples
* Récupérer le nombre d'abonnés de votre compte
* Récupérer toutes les informations liées à votre dernier Tweet
