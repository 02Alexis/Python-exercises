# Se define una función llamada maximum con tres parámetros: a, b y c
def maximum(a, b ,c):
	# Dentro de la función, se utilizan declaraciones 'if', 'elif' y 'else' para comparar los valores de 'a, b y c' y encontrar el número más grande
	# Si 'a' es mayor o igual que 'b' y 'a' es mayor o igual que 'c', entonces a es el más grande 
	if(a >= b) and (a >= c):
		# y se asigna a la variable 'largest'
		largest = a
    # Si 'b' es mayor o igual que 'a' y 'b' es mayor o igual que 'c', entonces 'b' es el más grande 
	elif(b >= a) and (b >= c):
		# y se asigna a la variable 'largest'
		largest = b
	else:
    # Si ninguna de las condiciones anteriores se cumple, entonces 'c' es el más grande y se asigna a la variable 'largest'.
		largest = c

    # Finalmente, se devuelve el valor de largest
	return largest

# Se definen las variables a, b y c con los valores 10, 100 y 30 respectivamente.
a =	10; b = 100; c = 30

print(maximum(a,b,c))