print("********************")
print("* Programa que convierte numeros a vinario ")
print("******************** \n")

# Define una función, que tome un número decimal como argumento 
def binario(decimal):
    # devuelve su representación binaria como una cadena
    binario = ""
    # bucle while para calcular los dígitos binarios uno por uno
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Introduce el numero que quieras convertir a binario: "))
print(binario(numero))