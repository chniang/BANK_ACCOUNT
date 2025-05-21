class Compte_Bancaire:
    def __init__(self,numero_compte:str,titulaire:str,solde:float = 0.0):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = solde
        
    def depot(self,montant:float):
        if montant > 0:
            self.solde += montant
            print(f"depot de {montant}Fcfa effectue avec succes.");
        else:
            print("le montant du depot doit etre superieur a 0.");
        
    def retirer(self,montant:float):
        if montant <= 0:
            print(f"le montant retire doit etre superieur a 0.");
        elif montant <= self.solde:
            self.solde -= montant
            print(f"retrait de {montant}Fcfa effectue avec succes.");
        else:
            print("fonds insuffisants pour effectuer ce retrait.");
    def verifier_balance(self):
        print(f"le solde actuel de votre compte {self.numero_compte} est de {self.solde} Fcfa")
        return self.solde
    # Exemple d'utilisation du compte

if __name__ == "__main__":
    mon_compte = Compte_Bancaire("123ABC", "Cheikh Niang", 100.0)
    mon_compte.verifier_balance()

    mon_compte.depot(50.0)
    mon_compte.retirer(30.0)
    mon_compte.verifier_balance()

    # Autre exemple avec un nouveau client
    compte_client2 = Compte_Bancaire("456DEF", "Awa Ndiaye", 200.0)
    compte_client2.depot(100.0)
    compte_client2.retirer(500.0)
    compte_client2.verifier_balance()