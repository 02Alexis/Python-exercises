# La función func toma un número variable de argumentos de palabras clave (kwargs).

def func(**kwargs):
    # Dentro de la función, verifica si la clave 'fruit' está presente en el diccionario kwargs utilizando la instrucción if 'fruit' in kwargs:

    # Si 'fruit' está presente en kwargs, imprime un mensaje indicando que la fruta escogida es el valor asociado a la clave 'fruit'.
    # Si 'fruit' no está presente en kwargs, imprime un mensaje indicando que no se ha especificado ninguna fruta.
    if 'fruit' in kwargs:
        print('Mi fruta escogida es: {}'.format(kwargs['fruit']))
    else:
        print('no hay fruta')

# Luego, se llama a la función func con un argumento de palabra clave 'fruit' con el valor 'manzana'
#  y otro argumento de palabra clave 'veggie' con el valor 'Tomate'
func(fruit='manzana', veggie='Tomate')
