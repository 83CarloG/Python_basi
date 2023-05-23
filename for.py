# Esercizio 1
# Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
# Esercizio 2
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
# Esercizio 3
# Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
# Esercizio 4
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.
# Esercizio 5
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
# Esercizio 6
# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
# Esercizio 7
# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
# Esercizio 8
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.
# Esercizio 9
# Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
# Esercizio 10
# Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.

#1
list_example = [3,5,True,"here"]
for element in list_example:
    print(element)
#2
for i in range(1,11):
    print(i)
#3
list_number = [1,2,3,4,5,6]
totale = 0
for i in list_number:
    totale += i
print("il totale è" , totale) 
#4
# for i in range(2, 21, 2):
#     print(i)

for i in range(1,11):
    if i%2 == 0:
        print(i)
#5
for i in "ciao":
    print(i)
#6
persona = {"nome":"carlo","cognome":"colombo","eta":21}
# for i in persona:
#     print(i)
for i in persona.keys():
    print(i)
#7
for chiave,valore in persona.items():
    print(chiave,":",valore)
#8
str_test = ["carlo","pietro"]

for word in str_test:
    for chart in word:
        print(chart)
#9
str_single = "paolo"
chart_find = "o"
count = 0

for chart in str_single:
    if chart == chart_find:
        count += 1
print(count)
#10
list_number2 = [1,3,4,5,12,10]
somma = 0
for number in list_number2:
    somma += number

media = somma/len(list_number2)
print(media)