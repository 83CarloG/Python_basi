# Esercizio 1
# Scrivi una lambda function che prenda un parametro e restituisca il quadrato del numero.
# Esercizio 2
# Scrivi una lambda function che prenda una lista e restituisca una lista di tutti gli elementi della lista originale moltiplicati per 2.
# Esercizio 3
# Scrivi una lambda function che prenda una lista di parole e restituisca una lista contenente solo le parole che iniziano con la lettera "a".
# Esercizio 4
# Scrivi una lambda function che prenda due numeri e restituisca la somma dei loro quadrati.
# Esercizio 5
# Scrivi una lambda function che prenda una stringa e restituisca True se la stringa è palindroma, altrimenti False.
# Esercizio 6
# Scrivi una lambda function che prenda una lista di parole e restituisca la lunghezza media delle parole nella lista.
# Esercizio 7
# Scrivi una lambda function che prenda una lista di numeri e restituisca la somma solo dei numeri pari.
# Esercizio 8
# Scrivi una lambda function che prenda una lista di dizionari e restituisca una lista di tutte le chiavi dei dizionari.
# Esercizio 9
# Scrivi una lambda function che prenda una lista di numeri e restituisca una lista di tutti i numeri maggiori di 10.
# Esercizio 10
# Scrivi una lambda function che prenda una lista di tuple e restituisca una lista di tuple ordinate per il secondo elemento di ciascuna tupla.

#1
quadrato = lambda x : x**2
print(quadrato(12))

#2
lista_per_due = lambda x : [y**2 for y in x]
print(lista_per_due([3,4,6]))

#3
filtra_parole = lambda lista,chr: [parola for parola in lista if parola.startswith(chr)]
print(filtra_parole(["vino","america"],"a"))

#4
somma_quadrati = lambda x,y: x**2+y**2
print(somma_quadrati(2,3))

#5
filtra_stringa = lambda stringa: stringa == stringa[::-1]
print(filtra_stringa("cane"))

#6
lunghezza_media = lambda lista: sum(len(parola) for parola in lista) / len(lista)
print(lunghezza_media(["vino","america"]))

#7
lista_numeri_pari = lambda lista: [numero for numero in lista if numero%2 == 0]
print(lista_numeri_pari([1,4,5,6,7,8]))

#8
tutte_le_chiavi = lambda lista: [chiave for dizionario in lista for chiave in dizionario.keys()]
print(tutte_le_chiavi([{"nome": "carlo","lavoro":"solution designer"}, {"peso": 50}]))

#9
numeri_maggiore_zero = lambda lista : [elemento for elemento in lista if elemento >10]
print(numeri_maggiore_zero([3,7,8,11,10,25]))

#10
lista_tuple = lambda lista: sorted(lista, key=lambda tupla: tupla[1])

print(lista_tuple([("test","manico"),("prova","a")]))