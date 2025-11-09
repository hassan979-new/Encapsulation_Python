
# 🧮 Patrons de conception

## 📘 Description

Cette série de projets met en œuvre les principes fondamentaux de la programmation orientée objet, à travers des cas concrets de gestion bancaire :

- Encapsulation stricte des données sensibles (solde, identifiant, historique)

- Héritage entre classes pour spécialiser les comportements (ex. compte avec intérêts)

- Agrégation d’objets : un client peut posséder plusieurs comptes

- Méthodes spéciales (__str__, __setattr__) pour contrôler l’accès et l’affichage

- Attributs de classe pour la numérotation automatique des comptes

- Validation des opérations : dépôts, retraits, et protection contre les modifications non autorisées

## 📂 Project Structure
````
projets/
├── Exercice 1/
│   ├── compte_bancaire.py
│   ├── compte_emprange.py
│   └── test.py
├── Exercice 2/
│   ├── compte_bancaire.py
│   └── test.py
└── README.md
````


## ⚙️ Features

### **1.** . Banque – Gestion de compte avec historique et protection 
Classe CompteBancaire

- Attributs d’instance : _titulaire, __solde, __operation

Méthodes :

- deposer(montant) : ajoute un montant au solde et enregistre l’opération

- retirer(montant) : retire un montant si le solde est suffisant

- solde : propriété en lecture seule du solde

- __str__() : retourne une représentation textuelle du compte

- histoire() : affiche l’historique des opérations

- __setattr__() : empêche la modification directe du solde

Classe CompteEmprange

- Attribut d’instance : __taux

Méthode :

- calculer_interet() : retourne le montant des intérêts selon le solde et le taux

### **2.** MultiClient – Gestion multi-comptes avec identifiants automatiques 
Classe CompteBancaire

- Attribut de classe : COMPTEUR (compteur global)

- Attributs privés : __solde, __id

Méthodes :

- deposer(montant) : ajoute un montant au solde

- retirer(montant) : retire un montant si le solde est suffisant

- get_solde() : retourne le solde

- get_id() : retourne l’identifiant unique du compte

Classe Client

- Attributs : nom, comptes (liste de comptes)

Méthodes :

- ajouter_compte(compte) : ajoute un compte à la liste

- afficher() : affiche le nom du client et les informations de ses comptes
## 🖥️ Example Execution


### Séparer proprement une classe unique :

### Mini-bibliothèque géométrique : 

### Création d’une librairie statique (.a) ou partagée (.so) :

### Classe template et fichier d’en-tête uniquement :


## 💡 Concepts Practiced

- Différencier les attributs de classe et d’instance

- Protéger les données sensibles avec l’encapsulation

- Spécialiser les comportements via l’héritage

- Contrôler l’accès aux attributs avec des propriétés et méthodes spéciales

- Organiser les projets avec une structure modulaire

- Appliquer des règles métier dans les méthodes
## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : Python
- 🎓 Instructor	Mr.LACHGAR
- 📅 09	novembre 2025
