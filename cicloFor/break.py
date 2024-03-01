# Se define una cadena llamada x con algun valor
x = 'Alexis'

# Bucle for para iterar sobre los caracteres de la cadena:
for letter in x:
    if letter == 'i': #verifica si el caracter actual es igual a 'i'
        # Si la condición es verdadera, se ejecuta break
        break
    # Impresión de cada caracter hasta encontrar 'i':
    print(letter)