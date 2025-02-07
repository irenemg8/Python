#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 02 Intro a Python  ---  4.2 Ejercicios listas
#
#--------------------------------------------------------------------------

"""1. Dada una lista de enteros, muestra por pantalla si un número introducido por teclado está en la primera o en la última posición. La longitud mínima de la lista será de 1, en caso contrario, el programa terminará."""
num = int(input("Dime un número:"))
lista = [1, 3, 2, 4]
if len(lista) < 1:
    print("La longitud es inferior a 1")   
elif lista[0] == num:
    print("Está en la primera posición")

elif lista[-1] == num:
    print("Está en la última posición")
    
else:
    print("No está ni en la primera ni en la última posición")




"""2. Pide 4 números y añádelos a una lista. Después, rota los elementos y guárdalos en una nueva lista (el último es el primero, etc.), mostrando por pantalla esta nueva lista."""
num1 = int(input("Dime un número: "))
num2 = int(input("Dime un número: "))
num3 = int(input("Dime un número: "))
num4 = int(input("Dime un número: "))

# Crear la lista original - opción 1
# lista = [num1, num2, num3, num4]

# Crear la lista original - opción 2
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.append(num4)

lista2 = lista[::-1]  # Rotar la lista (invertir el orden)
print("Lista en el orden inverso:", lista2)




"""3. Dadas dos listas de longitudes diferentes, averiguar si el primero o el último elemento de ambas listas es el mismo. En este caso, eliminar dicho elemento y mostrar las listas resultantes."""
lista1 = [1, 3, 5, 4]
lista2 = [1, 2, 4]

if len(lista1) == len(lista2):
    print("Las listas deben ser de igual tamaño")

elif lista1[0] == lista2[0] and lista1[-1] == lista2[-1]:
    print("Coinciden tanto el primer elemento como el último")
    lista1.pop(0)
    lista1.pop(-1)
    lista2.pop(0)
    lista2.pop(-1)

elif lista1[0] == lista2[0]:
    print("Coinciden el primer elemento de cada lista")
    lista1.pop(0)
    lista2.pop(0)


elif lista1[-1] == lista2[-1]:
    print("Coinciden el último elemento de cada lista")
    lista1.pop(-1)
    lista2.pop(-1)


elif lista1[0] == lista2[-1] or lista1[-1] == lista2[0]:
    print("Coinciden el primero de una lista coincide con el último de la otra lista")
    if lista1[0] == lista2[-1]:
        lista1.pop(0)
        lista2.pop(-1)

    elif lista1[-1] == lista2[0]:
        lista1.pop(-1)
        lista2.pop(0)

else:
    print("No coinciden")

print("Lista 1:", lista1, "Lista 2:", lista2)




"""4. Dada una lista de enteros, averiguar si el primer o el último elemento es el mayor y sustituir el resto de elementos por éste (sin contar el primero y el último). Por ejemplo, la lista [11, 5, 9, 7] debería quedar como [11, 11, 11, 7]."""
lista = [11, 5, 9, 7] 
lista2 = []
mayor = lista[0]

for num in lista:
    if num > mayor:
        mayor = num

if mayor == lista[0] or mayor == lista[-1]:
    lista2 = [lista[0]] + [mayor] * (len(lista) - 2) + [lista[-1]]

else:
    print("Ni el primero ni el último son el mayor")

print(lista2)




"""5. Calcular la cantidad de números impares que hay en una lista de enteros."""
lista = [11, 5, 9, 7, 2, 1] 
contador = 0
for num in lista:
    if num % 2 != 0:
        contador += 1
print ("En la lista hay",contador,"números impares")




"""6. Dada una lista de enteros, mostrar por pantalla la diferencia entre el mayor y el menor valor de la lista. Prueba a utilizar funciones del API para obtener estos valores."""
lista = [2,1,3,4,6,5]
mayor = lista[0]
menor = lista[0]

# -------------- Versión sin funciones de la API ---------------------------------
for num in lista:
    if num > mayor:
        mayor = num

    elif num < menor:
        menor = num

diferencia = mayor - menor
print("La diferencia entre el mayor,",mayor,", y el menor,",menor," es", diferencia)

# -------------- Versión con las funciones min y max de la API -------------------
minimo = min(lista)
maximo = max(lista)
dif = maximo - minimo
print("La diferencia entre el mayor,",maximo,", y el menor,",minimo," es", dif)




"""7. Dada una lista de enteros, devolver la media de todos los valores. Prueba a buscar en el API."""
lista = [2,4,6,8]
suma =  0

# -------------- Versión sin funciones de la API ---------------------------------
for num in lista:
    suma += num

numero_elementos = len(lista)
media = suma / numero_elementos
print("La media vale", media)

# -------------- Versión con las funciones min y max de la API -------------------
suma = sum(lista)
numero_elementos = len(lista)
media = suma / numero_elementos
print("La media vale", media)




"""8. Dada una lista de enteros, mostrar por pantalla si hay algún número que esté repetido en dos posiciones consecutivas."""
lista = [2, 1, 1, 4, 6, 5]
for i in range(len(lista) - 1):  # Evita desbordamiento de índice
    if lista[i] == lista[i + 1]:
        print("El número que se repite dos veces consecutivas es el", lista[i])   




"""9. Dada una lista de enteros, elegir un número aleatorio de la lista."""
import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("El número random de la lista es", random.choice(lista))