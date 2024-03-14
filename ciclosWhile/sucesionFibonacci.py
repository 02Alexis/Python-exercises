
print("********************")
print("* programa que imprime en pantalla la sucesion fibonacci hasta el numero 1957 con solo 5 lineas de codigo ")
print("******************** \n")

# creacion devariables en menos lineas
num1, num2 = 0, 1

# El bucle while continúa imprimiendo 'num1' y 'num2' en la misma línea hasta que 'num2' 
# alcanza o supera el valor de 1957.
while num2 <= 1957:
    print(num1, num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2
# La actualización se realiza utilizando una asignación simultánea en una sola línea de código, lo que permite reducir la cantidad de líneas necesarias.
