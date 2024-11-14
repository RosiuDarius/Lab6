# main.py

from ui.client_ui import ClientUI


def afiseaza_meniu():
    print("\nMeniu principal:")
    print("1. Adăugă client")
    print("2. Modifică client")
    print("3. Șterge client")
    print("4. Afișează clienți")
    print("5. Rapoarte")
    print("6. Ieși")


def main():
    ui = ClientUI()

    while True:
        afiseaza_meniu()
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            try:
                client_id = int(input("Introdu ID client: "))
                nume = input("Introdu numele clientului: ")
                cnp = input("Introdu CNP-ul clientului: ")
                nr_filme_inchiriate = int(input("Introdu numărul de filme închiriate: "))
                ui.adauga_client(client_id, nume, cnp, nr_filme_inchiriate)
            except ValueError as e:
                print(f"Eroare: {e}")

        elif optiune == "2":
            try:
                client_id = int(input("Introdu ID client de modificat: "))
                nume = input("Introdu noul nume (sau apasă Enter pentru a lăsa neschimbat): ")
                cnp = input("Introdu noul CNP (sau apasă Enter pentru a lăsa neschimbat): ")
                nr_filme_inchiriate = input(
                    "Introdu noul număr de filme închiriate (sau apasă Enter pentru a lăsa neschimbat): ")

                nr_filme_inchiriate = int(nr_filme_inchiriate) if nr_filme_inchiriate else None
                ui.modifica_client(client_id, nume, cnp, nr_filme_inchiriate)
            except ValueError as e:
                print(f"Eroare: {e}")

        elif optiune == "3":
            try:
                client_id = int(input("Introdu ID client de șters: "))
                ui.sterge_client(client_id)
            except ValueError as e:
                print(f"Eroare: {e}")

        elif optiune == "4":
            print("\nLista clienților:")
            ui.afiseaza_clienti()

        elif optiune == "5":
            ui.rapoarte()

        elif optiune == "6":
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă. Te rog alege din nou.")


if __name__ == "__main__":
    main()
