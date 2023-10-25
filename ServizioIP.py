import socket


def get_service_type(target_host, target_port):
    try:
        # Creazione di un oggetto socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Impostazione del timeout a 1 secondo
        socket.setdefaulttimeout(1)

        # Tentativo di connessione al port
        result = client.connect_ex((target_host, target_port))

        # Verifica del tipo di servizio basato sulla risposta
        if result == 0:
            service_name = socket.getservbyport(target_port)
            print(f"Port {target_port} is open and the service is: {service_name}")
        else:
            print(f"Port {target_port} is closed")
        client.close()
    except Exception as e:
        print(f"An error occurred: {e}")


# Esempio di utilizzo
if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    get_service_type(target, port)
