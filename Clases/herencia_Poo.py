# definimos dos clases, 'Animal' y 'Perro'

# define una clase llamada Animal, la cual contiene tres metodos
class Animal():

    def __init__(self):
        print('Animal creado')

    def quien_soy(self):
        print('soy un Animal')

    def comer(self):
        print('estoy comiendo')

# define una segunda clase llamada Perro, que hereda de la clase Animal
class Perro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Perro creado')

    def quien_soy(self):
        print('soy un perro')