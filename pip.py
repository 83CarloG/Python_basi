
#usare
#   ex.: pip install camelcase
# rimuovere 
#   pip uninstall camelcase
# mostrare pacchetti
#   pip list


import camelcase

c = camelcase.CamelCase()


frase = "ciao sono edo"

print(c.hump(frase))
