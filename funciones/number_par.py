########################################## logica en la funcion


# La función number_par toma un parámetro num_list, que es una lista de números.
def number_par(num_list):
    # La función itera sobre cada número en la lista utilizando un bucle 
    for number in num_list:
        # Para cada número en la lista, verifica si es par
        if number % 2 == 0:
            print('True') # Si encuentra un número par, imprime 'True' y devuelve 'True'
            return True # detiene la ejecución de la función y evita que busque más números en la lista.
        else:
            # Si la función ha recorrido toda la lista y no ha encontrado ningún número par, imprime 'False' 
            pass
        # devuelve 'False'
    print('False')
    return False

# Al final, se llama a la función number_par con una lista [1, 3] como argumento, 
# que no contiene números pares. Por lo tanto, la función imprime 'False' y devuelve False
number_par([1,3])