#--------------------------------------------------------------------------------------------------------
#
#   Ejercicios del Colab 03 Funciones, tuplas y diccionarios  ---  3.1 Ejercicios tuplas y diccionarios
#
#--------------------------------------------------------------------------------------------------------

"""1. Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico, y que devuelva un nuevo diccionario que contenga los dos anteriores. Muestra el resultado por pantalla."""
def todo_en_el_mismo_diccionario(dic1, dic2):
    res = {}
    res = dic1.copy()  # Copia dic1 para no modificarlo
    res.update(dic2)   # Agrega dic2
    return res

# --- int main () ----------------
dic1 = {"Edad": 3, "Casa": 90}
dic2 = {"Nombre": 83, "Año": 1909, "Foca": 14}
res = todo_en_el_mismo_diccionario(dic1,dic2)
print(res)




"""2. Escribe una función que reciba un diccionario y una lista de palabras. La función debe devolver un nuevo diccionario con los items del diccionario cuyas claves correspondan a alguna de las palabras de la lista. Muestra el resultado por pantalla."""
def palabras_en_el_diccionario(dic, lista):
    res = {}
    for palabra in lista:
        if palabra in dic:  # Verifica si la palabra es una clave en el diccionario
            res[palabra] = dic[palabra]  
    return res

# --- int main () ----------------
dic = {"Edad": 3, "Casa": 90}
lista = ["Edad"]
res = palabras_en_el_diccionario(dic,lista)
print(res)




"""3. Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo de este diccionario. Muestra el resultado por pantalla."""
def min_valor_dic(dic):
    return min(dic.values())  # Obtener el mínimo de los valores del diccionario

# --- int main () ----------------
dic = {"Edad": 3, "Casa": 90}
res = min_valor_dic(dic)
print(res)




"""4. Escribe un programa que lea un texto por teclado. Posteriormente debe crear un diccionario donde las claves sean las palabras del texto y sus valores el número de apariciones de cada una de éstas en el texto. Muestra el resultado por pantalla."""
def contar_palabras(texto):
    palabras = texto.split()  # Dividimos el texto en palabras
    diccionario = {}  

    for palabra in palabras:
        palabra = palabra.lower()  # Convertimos a minúsculas para evitar diferencias por mayúsculas/minúsculas
        diccionario[palabra] = diccionario.get(palabra, 0) + 1  # Incrementamos el contador

    return diccionario

# --- int main () ----------------
texto = input("Introduce un texto: ")

resultado = contar_palabras(texto)
print(resultado)




"""5. Escribe una función que reciba el siguiente diccionario y cuente la cantidad de items que tienen `True` el campo `success`:
{
    1 : {'id': 1,
    'success': True,
    'name': 'Lary'
    },
    2 : {'id': 2,
    'success': False,
    'name': 'Rabi'
    },
    3 : {'id': 3,
    'success': True,
    'name': 'Alex'
    }
}
"""

def contar_success(dic):
    contador = 0
    for item in dic.values():
        if item['success']:
            contador +=1
    return contador


def contar_success_comprehension(dic):
    return sum(1 for item in dic.values() if item['success'])

# --- int main () ----------------
dic = {
    1 : {'id': 1,
    'success': True,
    'name': 'Lary'
    },
    2 : {'id': 2,
    'success': False,
    'name': 'Rabi'
    },
    3 : {'id': 3,
    'success': True,
    'name': 'Alex'
    }
}

res = contar_success(dic)
res2 = contar_success_comprehension(dic)

print(res)
print(res2)