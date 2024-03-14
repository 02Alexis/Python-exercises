import time

# Se definen las variables 'username' y 'password' con los valores predefinidos.
username = 'alexis'
password = '12345'

# Se solicita al usuario que ingrese su nombre de usuario y contraseña.
username_input = input('Username: ')
password_input = input('Password: ')

# Se verifica si el nombre de usuario y la contraseña ingresados coinciden con los valores predefinidos.
if username_input == username and password_input == password:
    print('Acceso permitido')
    print('Espere por favor')
    time.sleep(5) # se simula una pausa de 5 segundos antes de imprimir mensajes adicionales
    print('Ok... Cargando...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Muy bien, tienes autorización de seguridad. Levantando la computadora central secreta.')
# Si el nombre de usuario es correcto pero la contraseña es incorrecta, se imprime:
elif username_input == username and password_input != password:
    print('Contraseña incorrecta')
# Si el nombre de usuario es incorrecto pero la contraseña es correcta, se imprime
elif username_input != username and password_input == password:
    print('Nombre de usuario incorrecto')
else:
    # Si tanto el nombre de usuario como la contraseña son incorrectos, se imprime:
    print('Quizás quieras marcar ambos campos...')