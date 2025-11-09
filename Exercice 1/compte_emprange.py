from compte_bancaire import CompteBancaire

class CompteEmprange(CompteBancaire) :
    def __init__(self, titulaire, solde_initial=0, taux=0.02):
        super().__init__(titulaire, solde_initial)
        self.__taux = taux

    def calculer_interet(self):
        interet = self.solde * self.__taux
        return interet
    
    
        