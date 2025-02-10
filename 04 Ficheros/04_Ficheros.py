#--------------------------------------------------------------------------
#
#   Ejercicios del Colab 04 Ficheros  ---  1.4 Ejercicios ficheros
#
#--------------------------------------------------------------------------

"""1. Escribe un programa que genere un fichero de texto con los números del 1 al 5000 y sus cuadrados."""
f = open("e1.txt", mode="wt", encoding="utf-8")
i = 1
j = 1

f.write("Escribo los números del 1 al 5000.\n")
while i <= 5000:
    f.write(str(i) + " ")  #SIEMPRE deben ser de tipo string (ademá añado un espacio entre cada número)
    i += 1

f.write("Escribo los cuadrados del 1 al 5000.\n")
while j <= 5000:
    cuadrado = j * j
    f.write(str(cuadrado) + " ") 
    j += 1 

f.close()




"""2. Escribe una función que reciba el nombre de un fichero que contiene palabras (cada línea tiene una palabra) y que devuelva la palabra que tiene una longitud máxima y su longitud."""
def palabra_mas_larga(nombre_fichero):
    f = open(nombre_fichero, mode="rt", encoding="utf-8")
    texto = f.readlines()
    f.close()

    longitud_max = 0
    palabra_mas_larga = ""

    for palabra in texto:
        palabra = palabra.strip()  # Eliminar saltos de línea y espacios
        if len(palabra) > longitud_max:
            longitud_max = len(palabra)
            palabra_mas_larga = palabra

    return palabra_mas_larga, longitud_max  # Retorna la palabra y su longitud

# --- int main () ----------------
nombre_fichero = input("¿Cómo se llama tu fichero? ")
palabra, longitud = palabra_mas_larga(nombre_fichero)
print("La palabra más larga es", palabra, "con una longitud de", longitud, "caracteres.")




"""3. Escribe una función que recibe el nombre de un fichero (cada línea puede tener varias palabras) y una letra, y que muestre por pantalla las palabras del fichero que contienen la letra."""
#Versión que imprime toda la línea
def palabras_del_fichreo_que_contienen_letra_parrafo(nombre_fichero, letra):
    f = open(nombre_fichero, mode="rt", encoding="utf-8")
    texto = f.readlines()
    f.close()

    for palabra in texto:
        if letra in palabra:
            print(palabra)


#Versión que únicamente imprime esa palabra
def palabras_del_fichero_que_contienen_letra(nombre_fichero, letra):
    with open(nombre_fichero, mode="rt", encoding="utf-8") as f:
        # Leer todas las líneas y separar en palabras
        for linea in f:
            palabras = linea.strip().split()  # .strip() para quitar espacios y \n, .split() para separar las palabras
            for palabra in palabras:
                if letra in palabra:
                    print(palabra)

# --- int main () ----------------
nombre_fichero = input("¿Cómo se llama tu fichero? ")
letra = 'a'
palabras_del_fichero_que_contienen_letra(nombre_fichero, letra)




"""4. Escribe una función que reciba el nombre de un fichero y que muestre por pantalla cuántas veces aparece cada palabra."""
def contar_palabras_en_fichero(nombre_fichero):
    dic = {}
    f = open(nombre_fichero, mode="rt", encoding="utf-8")
    texto = f.readlines()
    f.close()

    # Procesar cada línea del archivo
    for linea in texto:
        palabras = linea.strip().split()  # Dividir la línea en palabras
        for palabra in palabras:
            if palabra in dic:
                dic[palabra] += 1  # Si la palabra ya está en el diccionario, aumentamos el contador
            else:
                dic[palabra] = 1  # Si la palabra no está, la agregamos con un contador inicial de 1

    # Mostrar el resultado
    for palabra, cantidad in dic.items():
        print(f"'{palabra}': {cantidad} veces")

# --- int main () ----------------
nombre_fichero = input("¿Cómo se llama tu fichero? ")
contar_palabras_en_fichero(nombre_fichero)



"""5. Escribe una función generadora que devuelva una palabra de un fichero cada vez que es llamada."""
def generadora(nombre_fichero):
    with open(nombre_fichero, mode="rt", encoding="utf-8") as f:
        for linea in f:
            for palabra in linea.split():
                yield palabra

# --- int main () ----------------
nombre_fichero = input("¿Cómo se llama tu fichero? ")
for palabra in generadora(nombre_fichero):
    print(palabra)




"""5. Escribe un función que anonimice el fichero `interview.txt`. Este fichero contiene una entrevista con Trump, pero su nombre no puede aparecer y hay que cambiarlo a "Mr. X" para anonimizar el fichero. El resultado, será escrito en un fichero `anonymous.txt`."""
def anonimalizar_fichero(fichero_entrada, fichero_salida):
    f = open(fichero_entrada, mode="rt", encoding="utf-8")
    texto = f.read()
    f.close()
    
    contenido_anonimo = texto.replace("Trump", "Mr. X")
    
    f2 = open(fichero_salida, mode="wt", encoding="utf-8")
    f2.write(contenido_anonimo)
    f2.close()

# --- int main () ----------------
anonimalizar_fichero("interview.txt", "anonymous.txt")




"""6. Escribe un programa que lee el nombre del fichero de texto del teclado y muestra por pantalla el texto codificado de forma que sólo las letras minúsculas se sustituyen por las siguientes según el abecedario (una `a` por una `b`, una `b` por una `c`, etc.)."""
def letras_abecedario(nombre_fichero):
    res = ""  # Inicializamos la variable 'res' para almacenar el resultado
    with open(nombre_fichero, mode="r", encoding="utf-8") as f:
        for linea in f:
            for letra in linea:
                if letra.islower():  # Verificamos si la letra es minúscula
                    # Obtenemos el siguiente carácter en el abecedario
                    if letra == 'z':
                        res += 'a'  # Si es 'z', la siguiente es 'a'
                    else:
                        res += chr(ord(letra) + 1)  # Incrementamos la letra
                else:
                    res += letra  # Si no es minúscula, dejamos la letra igual
    return res

# --- int main () ----------------
nombre_fichero = input("¿Cómo se llama tu fichero? ")
res = letras_abecedario(nombre_fichero)
print(res)