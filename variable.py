
#Esercizio 1: Creare una variabile chiamata nome e assegnargli un valore qualsiasi. Fatto ciò mandare a schermo la lunghezza della stringa.
# Esercizio 2: Mandare a schermo la variabile nome tutta in maiuscolo.
# Esercizio 3: Sostituire il carattere “a” contenuto nella variabile con “e” e stampare.
# Esercizio 4: Creare una variabile chiamata frase inserendoci la frase “ciao come stai?”. Dividere la frase in una lista di singole parole utilizzando il metodo split() e mandare a schermo il risultato.
# Esercizio 5: Stampare il numero di parole contenute nella frase mischiando il metodo split() per dividere e len() per contare.
# Esercizio 6: Verificare se frase comincia con “Ciao” utilizzando il metodo startswith() e mandare a schermo il risultato booleano.
# Esercizio 7: Creare la variabile cognome e nome_completo. Assegnare a quest’ultima la stringa concatenata tra nome e cognome e mandare a schermo.
# Esercizio 8: Creare la variabile età ed assegnarli in formato numero un valore casuale. Mostrare a schermo il nome completo e l’età in una sola stringa di testo.
# Esercizio 9: Mandare a schermo l’ultimo carattere della variabile frase in maiuscolo.
# Esercizio 10: Stampare gli ultimi 2 caratteri della stringa.

#1
nome = "Carlo Giuseppe"
print(len(nome))
#2
print(nome.upper())
#3
print(nome.replace("a", "e"))
#4
frase = "ciao come stai?"
print(frase.split())
#5
print(len(frase.split()))
#6
print(frase.startswith("Ciao"))
nome = "Carlo"
cognome = "Colombo"
nome_cognome = nome + ' ' + cognome
print(nome_cognome)
#8
età = 30

print(nome_cognome + ' ' + str(età))
#9
print(frase[-2:])