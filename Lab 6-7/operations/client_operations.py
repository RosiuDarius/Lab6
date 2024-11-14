# operations/client_operations.py

from domain.client import Client

class ClientExistsError(Exception):
    pass

class ClientNotFoundError(Exception):
    pass

class GestorClienti:
    def __init__(self):
        self.clienti = []

    def adauga_client(self, client):
        if any(c.client_id == client.client_id for c in self.clienti):
            raise ClientExistsError(f"Clientul cu ID-ul {client.client_id} există deja.")
        self.clienti.append(client)

    def sterge_client(self, client_id):
        client = next((c for c in self.clienti if c.client_id == client_id), None)
        if not client:
            raise ClientNotFoundError(f"Clientul cu ID-ul {client_id} nu a fost găsit.")
        self.clienti.remove(client)

    def modifica_client(self, client_id, nume=None, cnp=None, nr_filme_inchiriate=None):
        client = next((c for c in self.clienti if c.client_id == client_id), None)
        if not client:
            raise ClientNotFoundError(f"Clientul cu ID-ul {client_id} nu a fost găsit.")
        if nume:
            client.nume = nume
        if cnp:
            client.cnp = cnp
        if nr_filme_inchiriate is not None:
            client.nr_filme_inchiriate = nr_filme_inchiriate

    def cauta_client(self, nume=None, cnp=None):
        return [client for client in self.clienti if (nume and nume.lower() in client.nume.lower()) or (cnp and cnp == client.cnp)]

    def clienti_ordonati_dupa_nume(self):
        return sorted(self.clienti, key=lambda client: client.nume)

    def clienti_ordonati_dupa_nr_filme(self):
        return sorted(self.clienti, key=lambda client: client.nr_filme_inchiriate, reverse=True)

    def rapoarte(self):
        print("Cele mai inchiriate filme:")
        for client in self.clienti_ordonati_dupa_nr_filme():
            print(client)

        total_clienti = len(self.clienti)
        top_30_percent = self.clienti_ordonati_dupa_nr_filme()[:int(total_clienti * 0.3)]
        print("\nPrimii 30% clienți cu cele mai multe filme:")
        for client in top_30_percent:
            print(f"{client.nume} - Filme închiriate: {client.nr_filme_inchiriate}")
