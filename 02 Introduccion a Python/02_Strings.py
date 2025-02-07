#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 02 Intro a Python  ---  4.4 Ejercicios Strings
#
#--------------------------------------------------------------------------

"""1. Escribe un programa que, dado un string y un valor n no negativo, muestre por pantalla el string repetido n veces."""
texto = "Hola"
num = 5
i = 1 
while i <= num:
   print(texto)
   i += 1




"""2. Modifica el script anterior para que repita sólo los 3 primeros caracteres del string. La longitud mínima del string será de 3, si no, el programa mostrará un mensaje y terminará."""
texto = "Hola"
num = 5
i = 1 
if len(texto) > 3:
    while i <= num:
        print(texto[0:3])   #De la posición 0 a la 3-1 (Hol)
        i += 1
else:
    print("Longitud inferior a 3")




"""3. Dado un string, muestra por pantalla un nuevo string que sea 3 copias de los últimos dos caracteres del string original. La longitud mínima del string será de 2, si no, el programa mostrará un mensaje y terminará."""
texto = "Hola"
nuevo_texto = ""

if len(texto) > 2:
    nuevo_texto = (texto[-2:]*3)
    print(nuevo_texto)

else:
    print("Longitud inferior a 2")




"""4. Dado un string, muestra por pantalla un nuevo string que tenga los dos últimos caracteres movidos al inicio. La longitud mínima del string será de 2."""
texto = "Hola"
nuevo_texto = ""

if len(texto) > 2:
    nuevo_texto = texto[-2:] + texto[:-2]
    print(nuevo_texto)

else:
    print("Longitud inferior a 2")




"""5. Dado un string, muestra por pantalla un nuevo string que sea el original, repitiendo cada caracter dos veces."""
texto = "Hola"
nuevo_texto = ""

for letra in texto:
    nuevo_texto += letra * 2  # Concatenar cada letra repetida dos veces
print(nuevo_texto)




"""6. Dados dos strings, muestra por pantalla la cantidad de veces que el segundo string aparece en el primero."""
texto1 = "ha"
texto2 = "Hoy han habido habichuelas para comer"
contador = texto2.count(texto1)  #Función de la API
print("Se repite",contador,"veces")


"""7. Dados dos strings, muestra por pantalla un mensaje indicando si uno de los dos aparece al final del otro, ignorando diferencias de mayúsculas y minúsculas. Por ejemplo, el string "AbC" y "HiaBc" debería mostrar que si que aparece uno al final del otro."""
texto1 = "AbC"
texto2 = "HiaBc"

t1 = texto1.lower()
t2 = texto2.lower()

# Comprobar si uno aparece al final del otro, endswith es una función de la API
if t2.endswith(t2) or t1.endswith(t2):
    print("Sí, uno aparece al final del otro.")
else:
    print("No, ninguno aparece al final del otro.")




"""8. Realiza un script que genere 10 identificadores de socio aleatoriamente. Un identificador de socio está basado en 3 letras y 2 números del 0 al 9. Si se genera un identificador repetido, tendrá que generarse otro hasta que no salga repetido."""
import random
import string

identificadores = []

# Generar 10 identificadores únicos
while len(identificadores) < 10:
    # Generar 3 letras aleatorias y 2 números aleatorios
    letras = random.choices(string.ascii_uppercase, k=3)  # 3 letras aleatorias
    numeros = random.choices(string.digits, k=2)  # 2 números aleatorios
    identificador = ''.join(letras + numeros)
    
    # Añadir identificador al conjunto si no está repetido
    identificadores.append(identificador)

# Mostrar los 10 identificadores generados
for id in identificadores:
    print(id)
