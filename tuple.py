# Esercizio 1
# Creare una tupla vuota e assegnarla a una variabile.
# Esercizio 2
# Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
# Esercizio 3
# Accedere all'elemento "banana" della tupla precedente.
# Esercizio 4
# Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.
# Esercizio 5
# Verificare se l'elemento "ananas" è presente nella tupla precedente.
# Esercizio 6
# Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").
# Esercizio 7
# Verificare la lunghezza della tupla precedente.
# Esercizio 8
# Creare una tupla contenente i numeri interi da 1 a 5.
# Esercizio 9 (difficile)
# Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
# Esercizio 10
# Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

#1
tuple_example = ()
# tuple_example = tuple(())
print(type(tuple_example))
#2
tuple_example2 = ("mela", "banana", "kiwi")
print(tuple_example2)
#3
print(tuple_example2[1])
#4
tuple_example3 = tuple_example2[0:2]
print(tuple_example3)
#5
if "anans" in tuple_example3:
    print("ok")
else:
    print("ko")
#6
tuple_example5 = tuple_example2 + ("pesca" , "albicocca")
print(tuple_example5)
#7
print(len(tuple_example5))
#8
numeri = (1,2,3,4,5)
print(numeri)
#9
numeri_quadrato = tuple(numero**2 for numero in numeri)
print(numeri_quadrato)
#10
print(tuple_example5.count("mela"))