#  Esercizio 1
# Creare una lista vuota e assegnarla a una variabile.
#  Esercizio 2
# Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.
#  Esercizio 3
# Accedere all'elemento con indice 2 della lista precedente.
#  Esercizio 4
# Aggiungere un nuovo elemento "6" alla lista precedente.
#  Esercizio 5
# Rimuovere l'elemento con indice 3 dalla lista precedente.
#  Esercizio 6
# Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
#  Esercizio 7
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
#  Esercizio 8
# Ordinare la lista precedente in ordine decrescente.
#  Esercizio 9
# Contare quante volte l'elemento "2" appare nella lista precedente.

#1
lista_vuota = []
print(lista_vuota)
#2
lista_numeri = list(range(1,6))
print(lista_numeri)
#3
print(lista_numeri[2])
#4
lista_numeri.append(6)
print(lista_numeri) 
#5
lista_numeri.pop(3)
print(lista_numeri)
#6
lista_numeri2 = lista_numeri[:3]
print(lista_numeri2)
#7
lista_numeri3 = lista_numeri2[1:2]
print(lista_numeri3)
#8
lista_numeri4 = [1,2,5,7,4,12]
lista_numeri4.sort(reverse=True)
print(lista_numeri4)