# Esercizio 1
# Dichiarare una variabile "numero_intero" e assegnargli un valore **intero**. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 2
# Dichiarare una variabile "numero_decimale" e assegnargli un valore **float**. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 3
# Creare una variabile "testo" e assegnargli una **stringa** contenente una frase. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 4
# Creare una variabile "valore_booleano" e assegnargli un valore **booleano**. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 5
# Creare una lista "numeri" contenente 5 numeri interi. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 6
# Creare una lista "misti" contenente un numero intero, un numero float, una stringa e un valore booleano. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 7
# Creare una tupla "giorni_settimana" contenente i giorni della settimana come stringhe. Mandare a schermo il tipo della variabile per conferma.
# Esercizio 8
# Creare un dizionario "informazioni_personali" contenente il tuo nome, cognome, età e città di residenza. Mandare a schermo il tipo della variabile per conferma.

#1
numero_intero = int(4)
print (type (numero_intero))
#2
numero_decimale = float(4.3)
print (type (numero_decimale))
#3
testo = str("test")
print (type (testo))
#4
valore_booleano = bool(False)
print (type (valore_booleano))
#5
numeri = list((1,2,3,4))
print(type(numeri))
#6
misti = list((1,2.3,"test",False))
print(type(misti))
#7
giorni_settimana = tuple(("lun","mart","merc","giove","ven","sabato","dome"))
print(type(giorni_settimana))
print(giorni_settimana)
#8
informazioni_personali = {"nome": "Carlo Giuseppe", "cognome": "Colombo", "eta": "40", "residenza":"Novara"}
print(type (informazioni_personali))
