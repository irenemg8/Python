#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 02 Intro a Python  ---  3.5 Ejercicios while y for
#
#--------------------------------------------------------------------------

"""1. Realiza un programa para calcular el factorial de un número entero introducido por el teclado (sin utilizar la librería)."""
num = int(input("Dime un número"))
factorial = 1
i = 1 

while i <= num:
    factorial = factorial * i 
    i = i+1  # Incrementamos i++
print("El factorial de",num,"es",factorial)




"""2. Implementa un juego que genere un número entero aleatorio entre 1 y 100. Entonces, el usuario deberá introducir números por teclado para intentar adivinar el número generado. Cada vez que el usuario introduzca un número por teclado, el programa deberá determinar si el número es el generado inicialmente (ganando el usuario la partida), si el número introducido por el usuario es múltiplo o divisor del número (informando de que el número introducido es múltiplo o divisor), o si no es ninguno de los otros dos casos. Al final de la partida, el número de puntos obtenido por el usuario es 100 menos el número de intentos del usuario. La puntuación debe imprimirse al final del juego."""
import random
num_entre_1_y_100 = random.randint(1,100)    # creamos un entero aleatorio entre 1 y 100 (ambos incluidos)
num_usuario = int(input("Dime un número"))
intentos = 1  # cuento el primer intento

while num_usuario != num_entre_1_y_100:
    # Comprobar si es múltiplo o divisor
    if num_entre_1_y_100 % num_usuario == 0:
        print("Tu número es un múltiplo.")
    elif num_usuario % num_entre_1_y_100 == 0:
        print("Tu número es un divisor.")
    
    # Dar pistas al usuario
    elif num_usuario < num_entre_1_y_100:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    # Pedir un nuevo número y contar el intento
    num_usuario = int(input("Intenta de nuevo: "))
    intentos = intentos + 1

puntuacion = 100 - intentos
print("El número secreto era el", num_entre_1_y_100)
print("Tu puntuación es", puntuacion)