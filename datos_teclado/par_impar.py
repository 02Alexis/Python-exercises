print("******************************************************")
print("* Programa que determina si un numero es par o impar *")
print("****************************************************** \n")

num = int(input("Por favor introduce un numero entero: "))

if num % 2 == 0:
    print("El numero ", num, " es 'PAR.'")

if num % 2 == 1:
    print("El numero ", num, " es 'IMPAR'.")