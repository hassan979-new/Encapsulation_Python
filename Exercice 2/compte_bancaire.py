class CompteBancaire:
    COMPTEUR = 0
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        CompteBancaire.COMPTEUR += 1
        self.__id = CompteBancaire.COMPTEUR

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant

    def get_solde(self):
        return self.__solde
    
    def get_id(self):
        return self.__id

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, compte:CompteBancaire) :
        if compte :
            self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for c in self.comptes :
            print(f"Compte numero {c.get_id()}, Solde : {c.get_solde()} euro")