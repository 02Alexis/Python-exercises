# ------------  Define una lista llamada mylist que contiene elementos
mylist = [1,2,3]

# ------------ Inicia un bucle for que itera sobre los números generados por la función range()
# ------------ Esto genera una secuencia de números desde 0 hasta 10, con un paso de 2 en 2. 
for num in range(0,11,2): 
    print(num) # ------------ Imprime cada número generado por el bucle for.

print(list(range(11))) # Imprime una lista que contiene números del 0 al 10 utilizando la función range