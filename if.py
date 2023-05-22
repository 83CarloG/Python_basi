# Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".
# Esercizio 2
# Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".
# Esercizio 3
# Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".
# Esercizio 4
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".
# Esercizio 5
# Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
# Esercizio 6
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
# Esercizio 7
# Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". Se il numero è minore di 10, stampare "Il numero è minore di 10".
# Esercizio 8
# Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante isAlpha(), stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".
# Esercizio 9 (difficile)
# Scrivere un programma che chieda all'utente di inserire tre numeri interi. Il programma deve verificare se i tre numeri formano un triangolo rettangolo. Se i tre numeri formano un triangolo rettangolo, stampare "I tre numeri formano un triangolo rettangolo". Altrimenti, stampare "I tre numeri non formano un triangolo rettangolo".

#1
# test = input("inserisci un numero: ")
# if (int(test) >= 0):
#     print("Numero positivo")
# else:
#     print("Numero negativo")
# #2
# numero1 = input("Inserisci un numero: ")
# numero2 = input("Inserisci un altro numero: ")

# if numero1>numero2:
#     print("Il primo numero è maggiore")
# elif numero2>numero1:
#     print("Il secondo numero è maggiore")
# else:
#     print("I numeri sono uguali")
# #3
# str_test = input("Inserire una stringa: ")
# if len(str_test)<1:
#     print("La stringa è vuota")
# else:
#     print("la stringa non è vuota")
# #4
# numero_test = input("Inserisci un numero: ")
# test_pari_dispari =   numero_test + " è un numero pari" if int(numero_test)%2 == 0 else numero_test + " è un numero dispari"
# print(test_pari_dispari)
# #5
# str_word = input("Inserisci una lettera: ")
# test_vocale = "è una vocale" if str_word in "aeiou" else "è una consonante"
# print(test_vocale)
# #6
# numero_test_maggiore_10 = int(input("Inserisci un numero: "))
# test_maggiore_10 = "Il numero è compreso tra 1 e 10" if 1 <= numero_test_maggiore_10 <= 10 else "Il numero non è compreso tra 1 e 10"
# print(test_maggiore_10)
# #7
# numero_test2 = int(input("Inserisci un numero: "))
# if numero_test2 > 10:
#     print("Il numero è maggiore di 10")
# elif numero_test2<10:
#     print("Il numero è minore di 10")
# else:
#     print("Il numero è uguale di 10")
# #8
# carattere = input("Inserisci un carattere: ")
# if not carattere.isalpha() :
#     print("Il carattere inserito non è una lettera")
# elif carattere in "aeiou":
#     print("Il carattere è una vocale")
# else:
#     print("Il carattere è una conosnante")
#9
numero_1 = int(input("Inserisci un numero (1): "))
numero_2 = int(input("Inserisci un numero (2): "))
numero_3 = int(input("Inserisci un numero (3): "))

totale = [numero_1,numero_2,numero_3]

totale.sort()

print(int(pow(totale[0]**2 + totale[1]**2,1/2)),int(totale[2]**2) )

if pow(totale[0]**2 + totale[1]**2,1/2) == totale[2]:
    print("E' un triangolo rettangolo")
else:
    print("Non è un triangolo rettangolo")


