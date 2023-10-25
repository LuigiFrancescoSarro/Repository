import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    # Creazione del blocco genesi
    return Block(0, time.time(), "Genesis Block", "0")

# Creazione di una lista per conservare i blocchi
blockchain = [create_genesis_block()]

# Funzione per aggiungere nuovi blocchi
def add_block(data):
    previous_block = blockchain[-1]
    new_index = previous_block.index + 1
    new_timestamp = time.time()
    new_block = Block(new_index, new_timestamp, data, previous_block.hash)
    blockchain.append(new_block)

# Creazione di 3 nuovi blocchi
add_block("Dati del Blocco 1")
add_block("Dati del Blocco 2")
add_block("Dati del Blocco 3")

# Stampa dei blocchi
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("\n")
