persona = {
    "nome": "Carlo Giuseppe",
    "cognome": "Colombo",
    "eta": 40
}

print(persona)

crud = ("aggiungi","modifica","elimina","leggi")

def start():
    comando = input("Inserisci un comando (aggiungi,modifica,elimina,leggi): ")
    if comando.lower() == crud[0]:
        nuova_proprieta = input('inserisci nuovo chiave:valore divisi da una vigola: ')
        aggiungi(nuova_proprieta)
    elif comando.lower() == crud[1]:
        nuova_proprieta = input('inserisci la chiave:valore da modificare divisi da una vigola: ')
        aggiungi(nuova_proprieta)
    elif comando.lower() == crud[2]:
        nuova_proprieta = input('inserisci la chiave da eliminare: ')
        elimina(nuova_proprieta)
    elif comando.lower() == crud[3]:
        print(persona)
    else:
        print("comando non presente")

def aggiungi(args):
    args_split = args.split(",")
    persona[args_split[0]] = args_split[1]
    print(persona)

def modifica(args):
    args_split = args.split(",")
    persona[args_split[0]] = args_split[1]
    print(persona)

def elimina(args):
    del persona[args]
    print(persona)

while True:
    start()