#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 02 Intro a Python  ---  2.5 Ejercicios básicos
#
#--------------------------------------------------------------------------

"""1.   Realiza un programa que calcule la suma de los números 43582134 y 1234567, almacene el resultado en una variable, e imprima el resultado por pantalla."""
a = 43582134
b = 1234567
suma = a+b
print(suma)



"""2.   Hoy en día, la tasa de cambio entre el euro y el dolar es de 0.85 euros por cada dólar. Atendiendo a esta información, construye un programa que lea una cantidad de dólares por teclado e informe al cliente de la cantidad de euros que obtendría al cambiar."""
tasa = 0.85
dolares = int(input("Introduce cuántos $ quieres pasar a €:")) #pido la info al usuario
res = dolares*tasa
print("Tienes",res,"€")



"""3.   Se cree comúnmente que 1 año humano equivale a 7 años en un perro. Construye un programa que le pregunte al usuario en qué año nació y le informe de su edad perruna. Asume que el año actual es 2025."""
anyos_perro = 7
anyo_actual = 2025
anyo_nacimiento_persona = int(input("¿En qué año naciste?"))
edad_persona = anyo_actual - anyo_nacimiento_persona
res = edad_persona * anyos_perro
print("Si fueras un perro tendrías",res,"años")