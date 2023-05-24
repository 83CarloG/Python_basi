# Esercizio 1
# Stampare i numeri interi da 1 a 10 usando un loop while.
# Esercizio 2
# Calcolare la somma dei primi n numeri interi positivi usando un loop while. L'utente deve inserire il valore di n.
# Esercizio 3
# Stampare i numeri pari da 2 a 10 usando un loop while.
# Esercizio 4
# Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
# Esercizio 5
# Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.
# Esercizio 6
# Stampare i numeri da 10 a 1 usando un loop while.
# Esercizio 7
# Calcolare il fattoriale di un numero intero positivo n usando un loop while.
# Esercizio 8
# Chiedere all'utente di inserire una lista di numeri interi. Stampare la somma di tutti i numeri usando un loop while.
# Esercizio 9
# Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.

1
i=1
while i<11:
    print(i)
    i += 1
#2
input_n = int(input("inserisci un numero: "))
somma = 0
i = 1
while i<=input_n:
    somma += i
    i += 1
print(somma)
#3
i = 2
while i<=11:
     print(i)
     i += 2
#4
randomNumber = 5
tryNumber = int(input("inserisci un numero "))
while tryNumber != randomNumber:
        tryNumber = int(input("inserisci un numero "))

print("bravo, indovinato!")
#5
str_user = input("inserisci una stringa ")
i = 0
str_nuova = ""
while i<len(str_user):
    str_nuova = str_user[i] + str_nuova
    print(str_user[i])
    i += 1

print(str_nuova)

#6
i = 10
while i>0:
    print(i)
    i -= 1
7
n = int(input("Inserisci un valore per n: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Il fattoriale di", n, "è", fact)
8
num_list = []
len_list = int(input("Quanti numeri vuoi inserire? "))
i = 0
while i < len_list:
         newNumber = int(input("inserisci un numero: "))
         num_list.append(newNumber)
         i += 1
somma = 0

for numero in num_list:
    somma += numero
print(somma)
9
word_example = input("inserisci una stringa: ")
i=0

while i<len(word_example):
    if word_example[i] not in ("aeiou"):
        print(word_example[i])
    i += 1
