import requests
from rich import print
from rich.prompt import Prompt

server_url = "http://localhost:8000"


def prikazi_zadatke():
    """Prikazuje zadatke."""
    response = requests.get(server_url)
    data = response.json()

    print("\nZa uraditi:")
    for todo in data['tasks']:
        stanje = "\[x]" if todo[2] else "[ ]"
        print(f"[{todo[0]}] {stanje} {todo[1]}")
    print("\n")

def dodaj_zadatak():
    """Kreira novi zadatk."""
    naziv = Prompt.ask("Naziv zadatka")
    zavrseno = Prompt.ask("Zavrseno?", choices=["Da", "Ne"])
    zavrseno_bool = True if zavrseno == "Da" else False

    todo = {
        "naziv": naziv,
        "zavrseno": zavrseno_bool,
    }

    requests.post(server_url, json=todo)

def izmeni_zadatak():
    """Menja postojeci zadatak."""
    id_zadatka = Prompt.ask("ID zadatka")
    server_url_sa_id = f"{server_url}/?id={id_zadatka}"

    naziv = Prompt.ask("Novi naziv")
    zavrseno = Prompt.ask("Da li je zavrseno?", choices=["Da", "Ne"])
    zavrseno_bool = True if zavrseno == "Da" else False

    novi_todo = {
        "naziv": naziv,
        "zavrseno": zavrseno_bool,
    }

    requests.put(server_url_sa_id, json=novi_todo)

def zavrsi_zadatak():
    """Menja postojeci zadatak."""
    id_zadatka = Prompt.ask("ID zadatka")
    requests.put(f"{server_url}/zavrsi?id={id_zadatka}")

def obrisi_zadatak():
    id_zadatka = Prompt.ask("ID zadatka")
    server_url_sa_id = f"{server_url}/?id={id_zadatka}"
    requests.delete(server_url_sa_id)


while True:
    prikazi_zadatke()
    akcija = Prompt.ask("Izaberi akciju:", choices=["Dodaj", "Izmeni", "Zavrsi", "Obrisi", "Izlaz"], default="Izlaz")

    if akcija == "Dodaj":
        dodaj_zadatak()
    elif akcija == "Izmeni":
        izmeni_zadatak()
    elif akcija == "Zavrsi":
        zavrsi_zadatak()
    elif akcija == "Obrisi":
        obrisi_zadatak()
    else:
        exit()