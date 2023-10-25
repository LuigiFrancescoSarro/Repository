import hashlib
import time

class Blocco:
    def __init__(self, indice, timestamp, dati, hash_precedente):
        self.indice = indice
        self.timestamp = timestamp
        self.dati = dati
        self.hash_precedente = hash_precedente
        self.hash = self.calcola_hash()

    def calcola_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.indice).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.dati).encode('utf-8') +
                   str(self.hash_precedente).encode('utf-8'))
        return sha.hexdigest()

def crea_primo_blocco():
    # Creazione del blocco genesi
    return Blocco(0, time.time(), "Inizio della produzione del Parmigiano Reggiano", "0")

# Creazione di una lista per conservare i blocchi
blockchain = [crea_primo_blocco()]

# Funzione per aggiungere nuovi blocchi alla catena
def aggiungi_blocco(dati):
    blocco_precedente = blockchain[-1]
    nuovo_indice = blocco_precedente.indice + 1
    nuovo_timestamp = time.time()
    nuovo_blocco = Blocco(nuovo_indice, nuovo_timestamp, dati, blocco_precedente.hash)
    blockchain.append(nuovo_blocco)

# Simulazione della filiera della produzione del Parmigiano Reggiano
mucca1 = "Mucca 1"
mucca2 = "Mucca 2"
latte = "Latte da mucche " + mucca1 + " e " + mucca2
aggiungi_blocco(latte)

caseificio = "Trasformazione del latte in formaggio Parmigiano Reggiano"
aggiungi_blocco(caseificio)

distribuzione = "Distribuzione del formaggio ai negozi"
aggiungi_blocco(distribuzione)

consumatore_finale = "Acquisto del Parmigiano Reggiano da un negozio"
aggiungi_blocco(consumatore_finale)

# Stampa dei blocchi
for blocco in blockchain:
    print(f"Indice: {blocco.indice}")
    print(f"Timestamp: {blocco.timestamp}")
    print(f"Dati: {blocco.dati}")
    print(f"Hash del Blocco Precedente: {blocco.hash_precedente}")
    print(f"Hash del Blocco: {blocco.hash}")
    print("\n")
