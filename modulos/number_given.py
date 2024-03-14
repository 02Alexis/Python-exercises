# Se importa el módulo random, que se utiliza para generar números aleatorios
import random

# Se define una función main() que representa la ejecución principal del programa.
def main():
    # se utiliza 'random.randrange(0, 6)' para generar un número aleatorio entre 0 y 5.
    dado = random.randrange(0, 6)
    print(f"Ha sacado un {dado + 1}.")

# se verifica si el script se está ejecutando como el programa principal. Si es así, se llama a la función 
# 'main()' para iniciar la ejecución del programa.
if __name__ == "__main__":
  main()