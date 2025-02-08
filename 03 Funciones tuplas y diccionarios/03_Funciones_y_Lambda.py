#-----------------------------------------------------------------------------------------------------
#
#   Ejercicios del Colab 03 Funciones, tuplas y diccionarios  ---  1.2 Ejercicios funciones y lambda
#
#-----------------------------------------------------------------------------------------------------

"""1.   Crea una función llamada `without_first_letter` que dada una lista de palabras, devuelva una nueva lista con la primera letra de cada palabra eliminada."""
def without_first_letter(lista):
    lista_sin_primera_letra = []
    for palabra in lista:
        lista_sin_primera_letra.append(palabra[1:])
    return lista_sin_primera_letra

# Con lambda:
# without_first_letter = lambda lista: [palabra[1:] for palabra in lista]

# --- int main () ----------------
lista = ["hola", "casa", "barco"]
res = without_first_letter(lista)
print(res)




"""2.   Crea una función llamada `get_minimum` que dado una lista de números,devuelva el valor mínimo encontrado el dicho array."""
def get_minimum(lista):  #Función sin usar la API
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

# Con lambda:
# get_minimum = lambda lista: min(lista)

def get_minimum_api(lista):  #Función con API
    return min(lista)

# --- int main () ----------------
lista = [5,3,4,1,9]
res = get_minimum(lista)
res_api = get_minimum_api(lista)
print(res)
print(res_api)




"""3.   Crea una función llamada `every_element_greater_than` que tome por parámetro un número y una lista numérica y devuelva `True` si todos los elementos son mayores que el número pasado por parámetro y `False` en caso contrario."""
def every_element_greater_than(num, lista):
    for n in lista:
        if n < num:
            return False
    return True

# Con lambda:
# every_element_greater_than = lambda num, lista: all(n > num for n in lista)

# --- int main () ----------------
lista = [5,3,4,2,9]
res = every_element_greater_than(3,lista)
print(res)




"""4.   Crea una función llamada `greater_than_average` que tome un parámetro x de tipo numérico, y una lista llamada data_array. La función deberá devolver cierto en caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario."""
def greater_than_average(x,data_array):
    media = sum(data_array) / len(data_array)
    if x > media:
        return True
    return False

# Con lambda:
# greater_than_average = lambda x, data_array: x > (sum(data_array) / len(data_array))

# --- int main () ----------------
data_array = [5,3,4,2,9]
res = every_element_greater_than(2, data_array)
print(res)




"""5.	 Crea una función llamada `clean_list` que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados."""
def clean_list(usuarios, baneados):
    no_baneados = []
    for u in usuarios:
            if u not in baneados:
                no_baneados.append(u)
    return no_baneados

# Con lambda:
# clean_list = lambda usuarios, baneados: [u for u in usuarios if u not in baneados]

# --- int main () ----------------
usuarios = ["Pepe", "Juan", "Manolo", "Miguel"]
baneados = ["Pepe", "Miguel"]
res = clean_list(usuarios,baneados)
print(res)