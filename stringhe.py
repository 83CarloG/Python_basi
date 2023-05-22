# # Esercizio 1
# #Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.
# # Esercizio 2
# Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile.
# # Esercizio 3
# Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per dividere la stringa in una lista di parole.
# # Esercizio 4
# Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World" con "Python".
# # Esercizio 5
# Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..
# # Esercizio 6
# Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
# # Esercizio 7
# Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".
# # Esercizio 8
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.
# # Esercizio 9
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

#1
stringa = "ciao mondo"
stringa_upper = stringa.upper()
print(stringa_upper)
#2
stringa = "Benvenuti a Roma"
stringa_lower = stringa.lower()
print(stringa_lower)
#3
string = "Il meglio deve ancora venire"
stringa_split = string.split()
print(stringa_split)
#4
string = "Hello World"
string_replace = string.replace("World", "Python")
print(string_replace)
#5
string = " Ciao         "
string_strip = string.strip()
print(string_strip)
#6
string = "abcdefg"
string_extract = string[:3]
print(string_extract)
#7
string = "Pyton"
string_startwith = string.startswith("Py")
print(string_startwith)
#8
string = "Ciao Mondo"
string_count = string.count("o")
print(string_count)
#9
string = "Ciao Mondo"
string_custom = string[-5:].replace("o","k").upper()
print(string_custom)