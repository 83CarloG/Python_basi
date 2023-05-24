# Esercizio 1
# Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.
# Esercizio 2
# Scrivi una funzione che prende una stringa e restituisce la stringa invertita.
# Esercizio 3
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.
# Esercizio 4
# Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.
# Esercizio 5
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.
# Esercizio 6
# Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.
# Esercizio 7
# Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.
# Esercizio 8
# Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.
# Esercizio 9
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.
# Esercizio 10
# Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.

1
list_number = [4,5,6,7,8,12]

def somma_lista (lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

print(somma_lista(list_number))
2

def inverso_stringa(stringa):
    inversa = ''
    indice = len(stringa) - 1
    while indice >= 0:
        inversa += stringa[indice]
        indice -= 1
    return inversa

print(inverso_stringa("pippo"))

3
def stampa_parole(words, chr):
    new_list = []
    for word in words:
        if chr in word:
            new_list.append(word)
    return new_list

print(stampa_parole(["ciao", "pippo"],"o"))
4
def numeri_pari(numeri):
    lista_numeri = []
    for numero in numeri:
        if numero%2 == 0:
            lista_numeri.append(numero)
    return lista_numeri

print(numeri_pari([2,5,4,7,8,10,5]))

5
def lunghezza_parole(lista):
    lista_lunghezza_parole= []
    for parola in lista:
        lista_lunghezza_parole.append(len(parola))
    return lista_lunghezza_parole

print(lunghezza_parole(["ciao","due","carlogiuseppe"]))

6
def numero_piu_alto(numeri):
    massimo = numeri[0]
    for numero in numeri:
        if numero > massimo:
            massimo = numero
    return massimo

print(numero_piu_alto([2,5,4,7,8,10,5]))

7
def lunghezza_parole_max(lista):
    massimo = lista[0]
    for parola in lista:
        if len(parola) > len(massimo):
            massimo = parola
    return massimo

print(lunghezza_parole_max(["ciaoooooooooooo","e","ca"]))

8
def media_lista_numeri(lista):
    lunghezza_lista = len(lista)
    somma = 0
    for numero in lista:
        somma += numero
    return somma/lunghezza_lista

print(media_lista_numeri([5,10]))

9
def lista_palindrome(lista):
    parola_palindroma = str()
    lista_parole_palindrome = []
    for parola in lista:
        i = len(parola) -1
        while i>-1:
            parola_palindroma += parola[i]
            i -= 1
        if parola == parola_palindroma:
            lista_parole_palindrome.append(parola)
        parola_palindroma = ""
    return lista_parole_palindrome

def lista_palindrome2(lista):
    lista_parole_palindrome = []
    for parola in lista:
        if parola == parola[::-1]:
            lista_parole_palindrome.append(parola)
    return lista_parole_palindrome

print(lista_palindrome2 (['cane','osso','anna']))

print(lista_palindrome (['cane','osso','anna']))
10

def trova_il_maggiore(lista, n):
    lista_numeri = []
    for numero in lista:
        if numero > n:
            lista_numeri.append(numero)
    return lista_numeri

print(trova_il_maggiore([10,25,1,4,12,32], 10))