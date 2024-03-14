# Se define un diccionario que contiene varios pares clave-valor. Las claves son nombres de frutas y las correspondientes valores son precios.
# Además, una de las claves ('Galleta') tiene como valor una lista que contiene diferentes tipos de galletas.
my_dictionary = {'Banano':'$500', 'Manddarina':'$1000', 'Galleta':['Chocolate', 'Fresa', 'Coco'], 'Manzana':'1500', 'Mango':'1000', }

# Se agrega un nuevo par clave-valor al diccionario 'my_dictionary', donde la clave es 'Naranja' y el valor es 1000
my_dictionary['Naranja'] = 1000

# Se accede al valor asociado con la clave 'Galleta', que es una lista. Luego, se accede al elemento en la posición 2 de esa lista (que es 'Coco'),
print(my_dictionary['Galleta'][2].upper()) # se convierte a mayúsculas utilizando el método upper


# print(my_dictionary.keys()) # imprimiría las claves del diccionario 

# print(my_dictionary) # imprimiría el diccionario completo incluyendo todas las claves y sus respectivos valores