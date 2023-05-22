#  Esercizio 1
# Creare un dizionario vuoto e assegnarlo a una variabile.
#  Esercizio 2
# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
#  Esercizio 3
# Accedere al valore dell'elemento con chiave "età" del dizionario precedente.
#  Esercizio 4
# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.
#  Esercizio 5
# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
#  Esercizio 6
# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.
#  Esercizio 7
# Creare una nuova lista che contenga solo i valori del dizionario precedente.
#  Esercizio 8
# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
#  Esercizio 9
# Contare il numero di elementi nel dizionario precedente.

#1
dizionario = dict()
print(dizionario)
#2
dizionario = {"nome":"Mario","cognome":"Rossi", "età":30}
print(dizionario)
#3
print(dizionario["età"])
#4
dizionario["email"]="mario.rossi@email.com"
print(dizionario)
#5
del dizionario["cognome"]
print(dizionario)
#6
chiavi_dizionario = list(dizionario.keys())
print(chiavi_dizionario)
#7
valore_dizionario = list(dizionario.values())
print(valore_dizionario)
#8
dizionario["età"] = 35
print(dizionario)
#6
print(len(dizionario))
