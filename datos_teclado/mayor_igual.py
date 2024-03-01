print("******************************************************")
print("* Programa que compara dos numeros *")
print("****************************************************** \n")

print("\n Introduce dos numeros a comparar: \n")

opcion1 = int(input("digite el primer numero: "))
opcion2 = int(input("digite el segundo numero: "))

print("\n Los numeros a comparar son: ", opcion1, " y ", opcion2, "\n")

if opcion1 == opcion2:
    print("son iguales...")
if opcion1 > opcion2:
    print("es mayor...")
if opcion1 >= opcion2:
    print("es mayor o igual...")
if opcion1 < opcion2:
    print("es Menor...")
if opcion1 <= opcion2:
    print("es Menor o igual...")
if opcion1 != opcion2:
    print("es Diferente...")