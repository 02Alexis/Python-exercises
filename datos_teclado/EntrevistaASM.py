name = input("Por favor escribe tu nombre: ")
lastname = input("Por favor escribe tu apellido: ")
age = int(input("Edad: "))
sexo = input("Sexo: ")
horario1 = int(input("Horario de entrada: "))
horario2 = int(input("Horario de salida: "))

print("\n los datos ingresados son: \n")
print("Nombre: ", name, lastname)
print("Edad: ", age)
print("Sexo: ", sexo)
print("Horario: ", horario1, "-", horario2)

if horario1 == 600 and horario2 == 1600:
    print("\n CONTRATADO \n")
else:
    print("\n Sigue intentando \n")