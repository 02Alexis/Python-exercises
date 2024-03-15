class Personaje: #--------- creamos nombre de la clase

    #--------- 'self' argumento que hace referencia asi mismo al obj y permite atrabes del '.'
    #--------- tener acceso a los atributos y metodos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(self.__nombre, ":", sep="")
        print(".Fuerza:", self.__fuerza)
        print(".Inteligencia:", self.__inteligencia)
        print(".Defensa:", self.__defensa)
        print(".Vida:", self.__vida)

    #--------- self es el modificador de atributos
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    #--------- metodo que devuelve un balor boolean para indicar si el personaje esta vivo o no
    def esta_vivo(self):
        return self.__vida > 0
    
    #--------- metodo que representa la accion de morir del personaje
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    #--------- metodo que calcule el daño que realiza el personaje a otro pj
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    #--------- metodo para atacar
    #--------- se encargara de calcular el daño y modificar la vida del enemigo con ese daño
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        #--------- confirmamos si el enemigo esta vivo
        if enemigo.esta_vivo():
            print("la vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

#---------para crear un objeto con la plantilla utilizamos el metodo constructor de la clase
#--------- es decir, Personaje(argumentos), le damos olos atributos y  lo guardamos en una var, 'mi_personaje'
mi_personaje = Personaje("alex", 10, 3, 2, 10)
mi_enemigo = Personaje("Vampiro", 8, 4, 1, 5)

mi_personaje.set_fuerza(-5)
mi_personaje.atributos()