print("***********************************************************************")
print("* Programa que determina Cual es el numero mas grande de tres numeros *")
print("*********************************************************************** \n")

num1 = int(input("Por favor introduce el primer numero: "))
num2 = int(input("Por favor introduce el segundo numero: "))
num3 = int(input("Por favor introduce el tercero numero: "))

if num1 > num2 and num1 > num3:
    print("El numero", num1, "Es el mas grande de los tres.")
else:
    if num2 > num3:
        print("El numero", num2, "Es el mas grande de los tres.")
    else:
        print("El numero", num3, "Es el mas grande de los tres.")