peso = 92
altezza = 191

#print("ciao sono luca e sonop alto " + str(altezza) + " cm")

frase = "ciao sono luca e sono alto {} cm e peso {} kg ed ho {} anni"
print(frase.format(altezza,peso,"39"))

frase2 = "ciao sono luca peso {1} kg e sono alto {2:.2f} cm ed ho {0}"
print(frase2.format(39,peso,altezza))

frase3 = "ciao sono luca peso {peso} kg e sono alto {altezza:.2f} cm ed ho {eta}"
print(frase3.format(eta=39,peso = peso,altezza = altezza))