def cifrario_di_cesare(parola, chiave):
    parola_cifrata = ""
    for carattere in parola:
        # Verifica se il carattere è una lettera dell'alfabeto
        if carattere.isalpha():
            # Calcola il nuovo valore del carattere cifrato
            valore_cifrato = ord(carattere) + chiave
            # Verifica se il carattere è maiuscolo o minuscolo
            if carattere.isupper():
                # Se il carattere cifrato supera 'Z', ritorna all'inizio dell'alfabeto
                if valore_cifrato > ord('Z'):
                    valore_cifrato -= 26
            else:
                # Se il carattere cifrato supera 'z', ritorna all'inizio dell'alfabeto
                if valore_cifrato > ord('z'):
                    valore_cifrato -= 26
            # Aggiunge il carattere cifrato alla parola cifrata
            parola_cifrata += chr(valore_cifrato)
        else:
            # Se il carattere non è una lettera, aggiungilo alla parola cifrata senza modificarlo
            parola_cifrata += carattere
    return parola_cifrata

# Chiedi all'utente di inserire una parola
parola = input("Inserisci la parola da cifrare: ")

# Chiedi all'utente di inserire la chiave di cifratura (un numero intero)
try:
    chiave = int(input("Inserisci la chiave di cifratura (un numero intero): "))
    # Cifra la parola e stampa il risultato
    parola_cifrata = cifrario_di_cesare(parola, chiave)
    print("Parola cifrata:", parola_cifrata)
except ValueError:
    print("Errore: La chiave di cifratura deve essere un numero intero.")
