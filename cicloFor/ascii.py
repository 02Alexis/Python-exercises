# Define una variable n con un valor de 8 que determina el tamaño del triángulo.
n = 8

#  Establece el valor inicial de la variable ascii en 65, que corresponde al código ASCII del carácter "A".
ascii = 65
# inicia un bucle que va desde 0 hasta 'n-1', es decir, desde 0 hasta 7
for i in range(n):
	# Imprime una cantidad de espacios en blanco que disminuye con cada iteración del bucle exterior, 
	# de manera que los caracteres impresos en la línea siguiente queden alineados hacia la derecha.
	print((n - 1 - i) * " ", end = "")
	for j in range(0, i + 1): #  Inicia un bucle que va desde 0 hasta el valor actual de i (inclusivo).
		print(chr(ascii), end = " ") # Imprime el carácter correspondiente al valor ASCII almacenado en ascii, seguido de un espacio en blanco.
		ascii += 1 # Incrementa el valor en 1 después de cada impresión
	print() # Imprime un salto de línea al final de cada fila del triángulo para pasar a la siguiente fila.