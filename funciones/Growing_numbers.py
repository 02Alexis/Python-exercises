# Programa que solicita al usuario dos números. Luego, verifica si el segundo número es mayor que el primero

# La función 'main' se define para realizar la tarea principal del programa.
def main():
    print("NÚMEROS CRECIENTES")
    # para obtener los datos números del usuario usamos 'input', 
    # que se almacenan como tipo de datos flotantes (float).
    numero_1 = float(input("Escriba un número: "))
    numero_2 = float(input("Escriba otro número más grande: "))
    if numero_1 >= numero_2:
        # Compara los dos números con una declaración 'if'
        print(f"¡Le he pedido un número más grande!")
    else:
        print(f"Gracias por su colaboración.")


# 'if __name__ == "__main__"': se usa para verificar si el script se está ejecutando como el programa principal. 
# Si es así, llama a la función main() para ejecutar el programa.
if __name__ == "__main__":
    main()