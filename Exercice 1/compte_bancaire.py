class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self.__operation = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.__operation.append(f"deposer {montant}")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self.__operation.append(f"retier {montant}")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
    
    def histoire(self) :
        for h in self.__operation :
            print(h)
    
    def __setattr__(self, name, value):
        if name == "solde" :
            raise AttributeError("vous n'avez pas le droit de modifier le solde!")
        super().__setattr__(name, value)
    
