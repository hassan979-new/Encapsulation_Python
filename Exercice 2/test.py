from compte_bancaire import CompteBancaire,Client

cli = Client("Yassir")
compte1=CompteBancaire()
compte2 = CompteBancaire()
compte3 = CompteBancaire()
compte1.deposer(3300)
compte2.deposer(50)
cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)
cli.ajouter_compte(compte3)
cli.afficher()