from compte_bancaire import CompteBancaire
from compte_emprange import CompteEmprange
if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("===Histoire des operations :")
    compte.histoire()
    print("Solde accessible (lecture) :", compte.solde)

    try :
        compte.solde = 500  
    except AttributeError as ex :
        print(ex)

    compte2 = CompteEmprange("Hassan", 5000)
    compte2.deposer(200)
    compte2.retirer(150)
    print(compte)
    print("===Histoire des operations :")
    compte2.histoire()
