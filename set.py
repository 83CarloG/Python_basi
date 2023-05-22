# Esercizio 1
# Creare un set vuoto e assegnarlo a una variabile.
# Esercizio 2
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
# Esercizio 3
# Aggiungere l'elemento "pesca" al set precedente.
# Esercizio 4
# Rimuovere l'elemento "mela" dal set precedente.
# Esercizio 5
# Verificare se l'elemento "ananas" è presente nel set precedente.
# Esercizio 6
# Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".
# Esercizio 7
# Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().
# Esercizio 8 (difficile)
# Creare un nuovo set contenente i numeri pari del set precedente.

#1
set_example = set(())
print(set_example)
#2
frutti =  {"mela", "banana", "kiwi"}
print(frutti,type(frutti))
#3
frutti.add("pesca")
print(frutti)
#4
frutti.remove("mela")
print(frutti)
#5
if "anans" in frutti:
    print("ok")
else:
    print("ko")
#6
nuovo_set = {"banana", "kiwi", "arancia"}
print(nuovo_set)
#
nuovo_set_range = set((range(1,6)))
print(nuovo_set_range)
#
nuovo_set_range_pari = set(())
for numero in nuovo_set_range:
    if numero%2:
        nuovo_set_range_pari.add(numero)

#numeri_pari = set(x for x in numeri if x % 2 == 0)

print(nuovo_set_range_pari)