# La función 'func' toma cualquier cantidad de argumentos posicionales (args) 
# y cualquier cantidad de argumentos de palabras clave (kwargs).
def func(*args,**kwargs):
    # Dentro de la función, imprime los argumentos posicionales y los argumentos de palabras clave
    print(args)
    print(kwargs)
    print(' Me gustaria {} {}'.format(args[0], kwargs['fruta']))

func(10,20,30, fruta='naranja', comida='galletas', animal='perro')