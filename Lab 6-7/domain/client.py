# domain/client.py

class Client:
    def __init__(self, client_id, nume, cnp, nr_filme_inchiriate=0):
        if not nume or not cnp:
            raise ValueError("Numele și CNP-ul sunt obligatorii.")
        self.client_id = client_id
        self.nume = nume
        self.cnp = cnp
        self.nr_filme_inchiriate = nr_filme_inchiriate

    def __str__(self):
        return f"ID: {self.client_id}, Nume: {self.nume}, CNP: {self.cnp}, Filme închiriate: {self.nr_filme_inchiriate}"

    def adauga_filme_inchiriate(self, nr_filme):
        if nr_filme < 0:
            raise ValueError("Numărul de filme adăugat nu poate fi negativ.")
        self.nr_filme_inchiriate += nr_filme

    def returneaza_filme(self, nr_filme):
        if nr_filme < 0:
            raise ValueError("Numărul de filme returnat nu poate fi negativ.")
        self.nr_filme_inchiriate = max(0, self.nr_filme_inchiriate - nr_filme)
