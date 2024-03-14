#  juego de ahorcado simple implementado en Python. Aquí está el funcionamiento del juego
# Se importan los módulos random y os.
import random
import os

# define una función llamada run
def run():

# Se definen dos variables 'IMAGES' y 'DB'
	IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

	DB = [
		"PYTHON",
		"JAVASCRIPTS"
	]

  # Se selecciona una palabra aleatoria de la lista 'DB'
	word = random.choice(DB)
	# Se crea una lista llamada 'spaces' que contiene tantos guiones bajos como letras tiene la palabra seleccionada.
	spaces = ["_"] * len(word)
	# Se establece el número máximo de intentos en 6.
	attemps = 6

  # Se inicia un bucle 'while' que continuará hasta que el juego termine
	while True: # En cada iteración del bucle
		os.system("cls") # Se limpia la pantalla
		for character in spaces: 
			# Se muestra en pantalla la palabra con espacios en blanco o letras adivinadas.
			print(character, end = " ")
		print(IMAGES[attemps]) # Se muestra la imagen correspondiente al número de intentos restantes.
		letter = input("Elige una letra: ").upper() # Se solicita al usuario que elija una letra.

    # Se busca la letra en la palabra:
		found = False
		for idx, character in enumerate(word):
			# Si la letra está en la palabra, se reemplaza el guion bajo en la posición correspondiente con la letra.
			if character == letter:
				spaces[idx] = letter
				found = True

    # Si la letra no está en la palabra, se decrementa el número de intentos
		if not found:
			attemps -= 1

    # Se verifica si todas las letras de la palabra han sido adivinadas
    # Si es así, se imprime "Ganaste" y el juego termina.
		if "_" not in spaces:
			os.system("cls")
			print("Winner")
			break
			input()

    # Se verifica si se han agotado los intentos. 
    # Si es así, se imprime "Game Over" y el juego termina.
		if attemps == 0:
			os.system("cls")
			print("Game Over")
			break
			input()




if __name__ == '__main__':
	run()