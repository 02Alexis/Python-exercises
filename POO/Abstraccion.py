class Personaje: #--------- creamos nombre de la clase
    #--------- darle personalidad con los atributos
    #--------- damos una variable para cada atributo y le asignamos un valor por default
    nombre = "alexis"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

#---------para crear un objeto con la plantilla utilizamos el metodo constructor de la clase
#--------- es decir, Personaje(argumentos), de momento ninguno, lo guardamos en una var, 'mi_personaje'
mi_personaje = Personaje()
mi_personaje.fuerza = 20 #--------- sobreescribimos los datos
print("el nombre del jugador es ", mi_personaje.nombre) #---------imprimimos los valores
print("el fuerza del jugador es", mi_personaje.fuerza)