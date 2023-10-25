import socket
import threading


def scan_port(target_host, port):
    try:
        # Creazione di un oggetto socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Impostazione del timeout a 1 secondo
        socket.setdefaulttimeout(1)

        # Tentativo di connessione al port
        result = client.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        client.close()
    except Exception as e:
        pass


def port_scan(target_host, target_ports):
    try:
        # Risolve l'indirizzo IP del target
        target_ip = socket.gethostbyname(target_host)
        print(f"Scanning target: {target_ip}")

        # Creazione di thread per la scansione dei port
        threads = []
        for port in target_ports:
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Aspetta che tutti i thread terminino
        for thread in threads:
            thread.join()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Couldn't connect to server.")
    except KeyboardInterrupt:
        print("Scanning stopped by user.")
        exit()


# Esempio di utilizzo
if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports = list(range(1, 1025))  # Scansione dei primi 1024 port, ma puoi modificare questo intervallo a tuo piacimento
    port_scan(target, ports)
