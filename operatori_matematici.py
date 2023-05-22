# Esercizio 1
#Dichiarare due variabili "numero1" e "numero2" e assegnargli due numeri interi. Eseguire l'addizione tra le due variabili e assegnare il risultato ad una nuova variabile "somma", mandandola a schermo.
# Esercizio 2
#Eseguire la sottrazione tra le due variabili e assegnare il risultato ad una nuova variabile "differenza". Mandare a schermo.
# Esercizio 3
#Eseguire la moltiplicazione tra le due variabili e assegnare il risultato ad una nuova variabile "prodotto". Mandare a schermo.
# Esercizio 4
#Eseguire la divisione tra le due variabili e assegnare il risultato ad una nuova variabile "quoziente". Mandare a schermo.
# Esercizio 5
#Eseguire l'operazione di modulo tra le due variabili e assegnare il risultato ad una nuova variabile "resto". Mandare a schermo.
# Esercizio 6
#Incrementare "numero1" di 1 e decrementare "numero2" di 3. Mandare a schermo i nuovi valori.
# Esercizio 7
#Moltiplicare "numero1" per se stesso + 5, sommarlo quindi a "numero2" elevato alla seconda. Assegnare l'operazione alla variabile risultato e mandare a schermo.
# Esercizio 8
#Trovare quella operazione per portare "numero1" a valere 1 senza riassegnarlo direttamente ad 1 e sottraendolo a se stesso.

#1
numero1 = 13
numero2 = 3

somma = numero1 + numero2
print(somma)
#2

differenza = numero1 - numero2
print(differenza)
#3
prodotto = numero1 * numero2
print(prodotto)
#4
quoziente = numero1 / numero2
print(quoziente)
#5
resto = numero1 % numero2
print(resto)
#6
#numero1 += 1
#print(numero1)
#numero2 -= 3
#print(numero2)

#7
numero1 += numero1 + 5 + pow(numero2,2)
print(numero1)
#8
print(numero1 - (numero1 - 1))