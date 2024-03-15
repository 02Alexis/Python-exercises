class Personaje: #--------- creamos nombre de la clase

    #--------- 'self' argumento que hace referencia asi mismo al obj y permite atrabes del '.'
    #--------- tener acceso a los atributos y metodos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)

    #--------- self es el modificador de atributos
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    #--------- metodo que devuelve un balor boolean para indicar si el personaje esta vivo o no
    def esta_vivo(self):
        return self.vida > 0
    
    #--------- metodo que representa la accion de morir del personaje
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    #--------- metodo que calcule el daño que realiza el personaje a otro pj
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    #--------- metodo para atacar
    #--------- se encargara de calcular el daño y modificar la vida del enemigo con ese daño
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        #--------- confirmamos si el enemigo esta vivo
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

#---------para crear un objeto con la plantilla utilizamos el metodo constructor de la clase
#--------- es decir, Personaje(argumentos), le damos olos atributos y  lo guardamos en una var, 'mi_personaje'
mi_personaje = Personaje("alex", 10, 3, 2, 10)
mi_enemigo = Personaje("Vampiro", 8, 4, 1, 5)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()