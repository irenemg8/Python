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





#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 02 Intro a Python  ---  3.3 Ejercicios if-else
#
#--------------------------------------------------------------------------


"""1.   Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas. Como ejemplos de ejecución:
Introduce la hora: 8
Introduce los minutos: 57
Son las 08:57 AM
Introduce la hora: 21
Introduce los minutos: 31
Son las 09:31 PM
Introduce la hora: 26:
Hora inválida. Deben ser entre 0 y 23.
"""
hora = int(input("Introduce la hora:"))
minutos = int(input("Introduce los minutos:"))

if hora < 0 or hora > 23:
    print("Hora inválida. Deben ser entre 0 y 23")

elif minutos < 0 or minutos > 59:
    print("Minutos inválidos. Deben ser entre 0 y 59")

else:
    if hora > 12:
        hora = hora - 12
        print("Son las",hora,":",minutos,"PM")

    else:
        print("Son las",hora,":",minutos,"AM")




"""2.   Se nos ha solicitado programar el calculador de la tarifa a pagar por los usuarios de una compañía de telefonía móvil. Todos los usuarios pagan una tarifa base de 10 euros al mes siempre que no hablen más de 180 minutos al mes. A partir de los 180 minutos, los usuarios pagan 10 céntimos por cada minuto hablado desde los 180 hasta los 240 minutos. A partir de ese momento, los usuarios pagan 20 céntimos por cada minuto extra consumido a partir de los 240. El calculador debe pedir al usuario los minutos hablados y devolver los euros a pagar."""
tiempo_hablado = int(input("¿Cuántos minutos has hablado por teléfono?"))
base = 10
if tiempo_hablado < 180:
    print("Tienes que pagar",base,"€")

elif tiempo_hablado >= 180 and tiempo_hablado < 240:
    tiempo_extra = tiempo_hablado - 180
    incremento = 0.1
    precio = base + tiempo_extra*incremento
    print("Tienes que pagar",precio,"€")

else:
    tiempo_extra1 = 240 - 180
    incremento1 = 0.1
    tiempo_extra2 = tiempo_hablado - 240
    incremento2 = 0.2
    precio = base + tiempo_extra1*incremento1 + tiempo_extra2*incremento2
    print("Tienes que pagar",precio,"€")




"""3. Otra persona y tú queréis reservar mesa en un restaurante. Queremos un programa que nos pregunte el estilo de vestir nuestro y el de nuestro compañero, que serán valores entre 0 y 10. Si uno de los dos tenemos un estilo de 8 o superior, entonces sí que tendremos mesa para cenar y deberá mostrar un mensaje por pantalla. Esto es así siempre y cuando uno de los dos no tenga un 2, en cuyo caso no tendremos mesa. En cualquier otro caso, el mensaje que debe mostrar es que no sabemos si tendremos mesa."""
mi_estilo = int(input("¿Del 1 al 10 cuál es tu estilo?"))
compi_estilo = int(input("¿Del 1 al 10 cuál es el estilo de tu compi?"))

if mi_estilo == 2 or compi_estilo == 2:
    print("Lo sentimos, no tenemos mesa para vosotros")

elif mi_estilo >= 8 or compi_estilo >= 8:
    print("Sí tenemos mesa para vosotros")

else:
    print("No estamos seguros si tenemos mesa para vosotros")




"""4. Realiza un programa que pregunte por un día de la semana y si estamos o no de vacaciones. El programa deberá mostrar un mensaje indicando a qué hora nos suena la alarma. Entre semana, la alarma sonará a las 8:00 y los fines de semana a las 10:00. Sin embargo, si estamos de vacaciones, los días entre semana sonará a las 10:00 y los fines de semana estará apagada."""
dia = input("¿Qué día es hoy?")
vacaciones = int(input("¿Estamos de vacaciones?"))

#Día entre semana laborable
if (dia != "sábado" and dia != "domingo") and (vacaciones == 0):
    alarma = "8:00"
    print("La alarma sonará a las",alarma)

#Día entre semana de vacaciones
elif (dia != "sábado" and dia != "domingo") and (vacaciones == 1):
    alarma = "10:00"
    print("La alarma sonará a las",alarma)

#Fin de semana laborable
if (dia == "sábado" and dia == "domingo") and (vacaciones == 0):
    alarma = "8:00"
    print("La alarma sonará a las",alarma)

#Fin de semana de vacaciones
elif (dia == "sábado" and dia == "domingo") and (vacaciones == 1):
    print("La alarma está apagada")




"""5. Realiza un programa que pregunte tres valores enteros y muestre un mensaje por pantalla indicando si los dos primeros tienen una diferencia máxima de 1 mientras que el tercero tiene una diferencia mayor que 2 con los otros dos. Utiliza la función abs(sum) para calcular el valor absoluto de un número."""
#CÓDIGO CON ABS()
num1 = int(input("Dime un número"))
num2 = int(input("Dime un número"))
num3 = int(input("Dime un número"))

diferencia_1_2 = abs(num2 - num1)
diferencia_1_3 = abs(num3 - num1)
diferencia_2_3 = abs(num3 - num2)

if (diferencia_1_2 <= 1) and (diferencia_1_3 > 2) and (diferencia_2_3 > 2):
    print ("Sí se cumple")

else:
    print ("No se cumple")


#CÓDIGO CON ABS(SUM())
num1 = int(input("Dime un número"))
num2 = int(input("Dime un número"))
num3 = int(input("Dime un número"))

diferencia_1_2 = abs(sum([num2, -num1]))  
diferencia_1_3 = abs(sum([num3, -num1]))  
diferencia_2_3 = abs(sum([num3, -num2]))  

if (diferencia_1_2 <= 1) and (diferencia_1_3 > 2) and (diferencia_2_3 > 2):
    print ("Sí se cumple")

else:
    print ("No se cumple")
