# Importa el módulo 'time' proporciona funciones relacionadas con el tiempo
import time

# Define una función llamada 'countdown' que toma un argumento 't'
def countdown(t):
	# inicia un bucle 'while' que continúa hasta que 't' llega a cero. En cada iteración del bucle:
	while t:
		# Divide 't' por 60 para obtener los minutos (mins) y los segundos restantes (secs)
		mins, secs = divmod(t, 60)
		# Formatea los minutos y los segundos en un formato "mm:ss" utilizando {:02d}:{:02d}.format(mins,secs)
		timer = '{:02d}:{:02d}'.format(mins,secs)
		# Imprime el tiempo formateado en la misma línea
		print(timer,end = '\r')
		# Espera un segundo utilizando 'time.sleep(1)'
		time.sleep(1)
		t -= 1 #Decrementa 't' en uno

	print("Timer Ended!") # Cuando el bucle termina, imprime "Timer Ended!" para indicar que el temporizador ha terminado
	
# Solicita al usuario que ingrese el tiempo en segundos a través de la entrada estándar utilizando :
t = input('Enter the time in seconds: ')

countdown(int(t)) # Llama a la función countdown pasando el tiempo ingresado convertido a entero (int(t))