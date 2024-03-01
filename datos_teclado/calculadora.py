print("* Calculadora con una sola variable * \n")

print("********************")
print("* Menú de opciones. * \n 1.Suma. \n 2.Resta. \n 3.Multiplicación. \n 4.Division. \n 5.Division Entera \n 6.Exponente. \n 7.Módulo o resto ")
print("******************** \n")

opcion = int(input("Introduce la opcion deseada: "))

if opcion == 1:
    print("Elegiste Suma \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", opcion)

elif opcion == 2:
    print("Elegiste Resta \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ", opcion)

elif opcion == 3:
    print("Elegiste Multiplicación \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es: ", opcion)

elif opcion == 4:
    print("Elegiste Division \n")
    opcion = float(input("Introduce el primer numero: "))
    opcion /= float(input("Introduce el segundo numero: "))
    print("El resultado de la division es: ", round(opcion, 2))

elif opcion == 5:
    print("Elegiste Division Entera \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion //= int(input("Introduce el segundo numero: "))
    print("El resultado de la Division Entera es: ", opcion)

elif opcion == 6:
    print("Elegiste Exponente \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion **= int(input("Introduce el segundo numero: "))
    print("El resultado del exponente es: ", opcion)

elif opcion == 7:
    print("Elegiste Módulo o resto \n")
    opcion = int(input("Introduce el primer numero: "))
    opcion %= int(input("Introduce el segundo numero: "))
    print("El módulo o resto es: ", opcion)

else:
    print("La opcion elegida no existe, vuelve a intentar")