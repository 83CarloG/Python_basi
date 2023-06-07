import miomodulo


class Persona:

    def __init__(self, name, surname) :
        self.name = name
        self.surname = surname

    def saluta(self):
        print("ciao sono " + self.name + " " + self.surname)

persona1 = Persona("carlo","colombo")


class Insegnante(Persona):

    def __init__(self, name, surname, materia):
        super().__init__(name, surname)
        self.materia = materia 
    def saluta(self):
        print("ciao sono " + self.name + " " + self.surname + " insegno " + self.materia)

insegnante = Insegnante("Mario","Rossi","Geo")

insegnante.saluta()

a = miomodulo.person1["country"]

b= miomodulo.fib2(5)
print(b)
