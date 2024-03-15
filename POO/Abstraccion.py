class Personaje: #--------- creamos nombre de la clase

    #--------- 'self' argumento que hace referencia asi mismo al obj y permite atrabes del '.'
    #--------- tener acceso a los atributos y metodos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

#---------para crear un objeto con la plantilla utilizamos el metodo constructor de la clase
#--------- es decir, Personaje(argumentos), le damos olos atributos y  lo guardamos en una var, 'mi_personaje'
mi_personaje = Personaje("alex", 10, 3, 2, 50)
print("el nombre del jugador es ", mi_personaje.nombre) #---------imprimimos los valores
print("el fuerza del jugador es", mi_personaje.fuerza)