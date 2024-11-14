# ui/client_ui.py

from operations.client_operations import GestorClienti, ClientExistsError, ClientNotFoundError
from domain.client import Client

class ClientUI:
    def __init__(self):
        self.gestor_clienti = GestorClienti()

    def adauga_client(self, client_id, nume, cnp, nr_filme_inchiriate):
        try:
            client = Client(client_id, nume, cnp, nr_filme_inchiriate)
            self.gestor_clienti.adauga_client(client)
            print(f"Clientul {client.nume} a fost adăugat.")
        except ValueError as e:
            print(f"Eroare: {e}")
        except ClientExistsError as e:
            print(f"Eroare: {e}")

    def sterge_client(self, client_id):
        try:
            self.gestor_clienti.sterge_client(client_id)
            print(f"Clientul cu ID-ul {client_id} a fost șters.")
        except ClientNotFoundError as e:
            print(f"Eroare: {e}")

    def modifica_client(self, client_id, nume=None, cnp=None, nr_filme_inchiriate=None):
        try:
            self.gestor_clienti.modifica_client(client_id, nume, cnp, nr_filme_inchiriate)
            print(f"Clientul cu ID-ul {client_id} a fost modificat.")
        except ClientNotFoundError as e:
            print(f"Eroare: {e}")

    def afiseaza_clienti(self):
        clienti = self.gestor_clienti.clienti_ordonati_dupa_nume()
        for client in clienti:
            print(client)

    def rapoarte(self):
        self.gestor_clienti.rapoarte()
