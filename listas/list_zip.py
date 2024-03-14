#--------------------- lista que contiene los números enteros del 1 al 4.
list1 = [1,2,3,4]
#--------------------- lista que contiene las letras minúsculas de la "a" a la "d"
list2 = ['a','b','c','d']
#--------------------- lista que contiene que contiene cuatro ceros
list3 = [0,0,0,0]

#---------------------  Utiliza la función 'zip()' para combinar las tres listas en una lista de tuplas.
print(list(zip(list1,list2,list3)))

if '3' in list2: #-------------- Verifica si el carácter '3' está presente en la lista 'list2'
    print('verdadero')
else:
    print('false')

print(max(list2)) #-------------- Encuentra el elemento máximo en 'list2' y lo imprime