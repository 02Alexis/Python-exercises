
print("=============")
print("Programa para calcular el promedio de un estudiante!!")
print("=============\n")

name = input("Para comenzar, ¿cual es tu nombre?: ")

nota1 = int(input(name + " ¿cual es tu calificacion en Matemáticas?: "))
nota2 = int(input(name + " ¿cual es tu calificacion en Español?: "))
nota3 = int(input(name + " ¿cual es tu calificacion en Ingles?: "))
print("\n")

promedio = (nota1 + nota2 + nota3) / 3 
promedio = int(promedio)

if promedio >= 4:
    print('Felicidades 🎉 ' + name + ' "Aprobastes" con un promedio de: ', promedio)
elif promedio <= 4:
    print("Flicidades, eres un pendejo 😹, tu promedio es de: ", promedio)