class Mucca:
    def __init__(self, nome):
        self.nome = nome

    def produce_latte(self):
        print(f"{self.nome} sta producendo latte.")
        return Latte()

class Latte:
    def __init__(self):
        self.ingredienti = ["latte"]

class Caseificio:
    def trasforma_latte_in_formaggio(self, latte):
        print("Il caseificio sta trasformando il latte in formaggio Parmigiano Reggiano.")
        return Formaggio()

class Formaggio:
    def __init__(self):
        self.ingredienti = ["latte", "caglio", "salamoia"]

class Distributore:
    def distribuisci_formaggio(self, formaggio):
        print("Il formaggio Parmigiano Reggiano è pronto per essere distribuito ai negozi.")
        return formaggio

class Cliente:
    def acquista_formaggio(self, formaggio):
        print("Il cliente ha acquistato il formaggio Parmigiano Reggiano.")

# Simulazione della produzione del Parmigiano Reggiano
mucca1 = Mucca("Mucca 1")
latte = mucca1.produce_latte()

caseificio = Caseificio()
formaggio = caseificio.trasforma_latte_in_formaggio(latte)

distributore = Distributore()
formaggio_pronto = distributore.distribuisci_formaggio(formaggio)

cliente = Cliente()
cliente.acquista_formaggio(formaggio_pronto)
