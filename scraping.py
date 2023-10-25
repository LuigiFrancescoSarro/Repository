import requests

def get_webpage_content(url):
    try:
        response = requests.get(url)
        # Verifica se la richiesta è andata a buon fine (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            return f"Errore: Impossibile recuperare la pagina (Codice di stato: {response.status_code})"
    except Exception as e:
        return f"Errore: {e}"

# Esempio di utilizzo
if __name__ == "__main__":
    url = input("Inserisci l'URL della pagina web: ")
    content = get_webpage_content(url)
    print("Contenuto della pagina web:")
    print(content)
