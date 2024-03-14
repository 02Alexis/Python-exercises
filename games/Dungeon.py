#  juego de aventura de texto simple llamado "Dungeon"

# Función principal que ejecuta el juego
import random
print('========================================')
print('\t\t#Bienvenido a la mazmorra#')
print('========================================\n\n')

# Lista de enemigos posibles
enemies = ['Esqueleto', ' Asesino', 'Vampiro', 'Pie Grande']

# El objetivo del juego es derrotar enemigos y recolectar pociones de salud.
player_health = 100  # Puntos de salud del jugador
number_of_positions = 4 # Número de pociones de salud disponibles
health_position = 30 # Cantidad de salud que proporciona cada poción
enemy_drop_chance = 50 # Probabilidad de que un enemigo suelte una poción de salud al ser derrotado
enemy_kill_count = 0 # Contador de enemigos derrotados
player_input1 = '' # Variable para almacenar la entrada del jugador

# Bucle principal del juego
while True:
	# Los enemigos son elegidos al azar
	enemy = random.choice(enemies)
	# Cada enemigo tiene una cantidad aleatoria de puntos de salud.
	enemy_health = random.randint(10, 76)
	# Imprimir información sobre el enemigo actual y la salud del jugador
	print('========================================')
	print(f'#		{enemy} ha aparecido		#')
	print(f'Tu HP: {player_health}')
	print(f"{enemy} HP: {enemy_health}")
	print('========================================\n\n')

	# Bucle para el combate con el enemigo
	while enemy_health > 1:
		print('========================================')
		print('¿Qué es lo que quieres hacer? ')
		print('1.Ataque')
		print('2.Beber poción de salud')
		print('3.Correr')
		player_input = input('Ingresa tu movimiento: ')
		# Realizar ataques y actualizar la salud del jugador y del enemigo
		if player_input == '1':
			enemy_damage = random.randint(10, 40)
			player_damage = random.randint(0, 10)

			enemy_health -= enemy_damage
			player_health -= player_damage

			print(f'\n Tu causaste a {enemy} {enemy_damage} daño en el ataque')
			print(f'¡En represalia! te causaste {player_damage} daño')
			print(f'Tu HP {player_health}')
			print(f"{enemy} HP: {enemy_health}")
			 # Verificar si el jugador ha perdido toda su salud
			if player_health < 1:
				print('¡Estás demasiado débil para luchar ahora! \n Te sacarán del juego.')
				break
		elif player_input == '2':
			# Beber una poción de salud si hay disponibles
			if number_of_positions > 0:
				print('Bebiste una posición.')
				player_health += health_position
				number_of_positions -= 1
				print(f'Tu HP: {player_health}')
				print(f'ahora tienes {number_of_positions} posiciones.')
			else:
				print('No tienes un solo puesto.')
				print('Debes matar a un enemigo para conseguir una posición.')
		elif player_input == '3':
			# Huir del enemigo
			print(f'Huiste del {enemy}')
			break
		else:
			# Manejar entrada inválida
			print('¡Comando no válido!Ingrese 1,2 o 3.')

	# Verificar si el jugador ha perdido toda su salud
	if player_health < 0:
		print('¡Gracias por jugar Dungeon!\n ¡¡Hiciste lo mejor que pudiste!!')
		break
	# Verificar si el enemigo ha sido derrotado
	if enemy_health < 0:
		print(f'Derrotaste al {enemy}')
		print('========================================')
		enemy_kill_count += 1
		
		# Verificar si el enemigo suelta una poción de salud
		if random.randint(0, 100) > enemy_drop_chance:
			print(f'{enemy} dejó caer una poción.')
			number_of_positions += 1
			print(f'Ahora tienes {number_of_positions} contigo')
			print('========================================')

	# Verificar si el jugador ha derrotado a tres enemigos seguidos
	if enemy_kill_count == 3:
		while True:
			print('¿Qué es lo que quieres hacer?')
			print('1. Continuar luchando')
			print('2. Salida')
			player_input1 = input('Introduzca su movimiento: ')
			if player_input1 == '1':
				print('¡Bien! Continúa luchando.')
				enemy_kill_count = 0
				break
			elif player_input1 == '2':
				print('¡Serás llevado a un lugar seguro!')
				break
			else:
				print('¡Comando inválido!')

	# Verificar si el jugador decide salir del juego
	if player_input1 == '2':
		print('¡Gracias por jugar Dungeon!\n ¡¡Hiciste lo mejor que pudiste!!')
		break

