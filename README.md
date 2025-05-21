# 🏦 Bank Account - Simulation d’un compte bancaire en Python

Ce projet est une simulation simple des opérations bancaires de base à l’aide de la programmation orientée objet en Python.

## 🚀 Fonctionnalités

- Dépôt d'argent sur le compte
- Retrait d'argent avec vérification du solde disponible
- Consultation du solde actuel

## 📌 Structure de la classe

```python
class Compte:
    def __init__(self, numero_compte, titulaire, solde)
    def depot(self, montant)
    def retirer(self, montant)
    def verifier_balance(self)
```

## 🔧 Exemple d'utilisation

```python
mon_compte = Compte("123ABC", "Cheikh Niang", 100.0)
mon_compte.depot(50.0)
mon_compte.retirer(30.0)
mon_compte.verifier_balance()
```

## 📁 Fichier principal

- `bank_account.py` : script principal contenant la classe et les exemples d'utilisation.

## 👨‍💻 Auteur

- Cheikh Niang

## 📜 Licence

Ce projet est open-source, sous licence MIT.
