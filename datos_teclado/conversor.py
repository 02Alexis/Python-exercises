#Sentencia condicional anidad
print("=============")
print("¡¡Convertidor de numeros a letras!!")
print("=============\n")

print("Menu de opciones: \n")
print("Presione 1 para convertir de numero a palabra.")
print("Presione 2 para convertir de palabra a numero. \n")

opcion = int(input("¿Cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n Has elegido conversor de numero a palabra. \n")
    print("Ingresa un numero del 1 al 4: \n")

    opcion1 = int(input("¿Cual es el numero que deseas convertir a palabra?: "))
    
    if opcion1 == 1:
        print("El numero que ingresastes es 'Uno'")
    elif opcion1 == 2:
        print("El numero que ingresastes es 'Dos' ")
    elif opcion1 == 3:
        print("El numero que ingresastes es 'Tres' ")
    elif opcion1 == 4:
        print("El numero que ingresastes es 'Cuatro' ")
    else:
        print("Lo sentimos pero el valor ingresado no esta en el sistema")

elif opcion == 2:
    print("\n Has elegido conversor de palabra a numero. \n")
    print("Ingresa un numero del 1 al 4: \n")

    opcion2 = input("¿Cual es la palabra que deseas convertir a numero?: ")
    opcion2 = opcion2.lower()

    if opcion2 == 'uno':
        print("El numero es '1' ")
    elif opcion2 == 'dos':
        print("El numero es '2' ")
    elif opcion2 == 'tres':
        print("El numero es '3' ")
    elif opcion2 == 'cuatro':
        print("El numero es '4' ")
    else:
        print("Lo sentimos pero el valor ingresado no esta en el sistema")
else:
    print("Lo sentimos pero el valor ingresado no esta en el sistema")