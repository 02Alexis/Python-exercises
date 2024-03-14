# convierte una lista de temperaturas en grados Celsius a una lista 
# de temperaturas equivalentes en grados Fahrenheit utilizando comprensión de listas

# Se define una lista celcius que contiene las temperaturas en grados Celsius
celcius = [0,10,20,34.5]

# Se utiliza la comprensión de listas para iterar sobre cada elemento de la lista celcius. 
# En cada iteración, se aplica la fórmula de conversión de grados Celsius a Fahrenheit, donde 'temp' es la temperatura actual en grados Celsius.
fahrenheit = [((9/5)*temp + 32) for temp in celcius ]
print(fahrenheit)