#-----------------------------------------------------------------------------------------------------
#
#   Ejercicios del Colab 03 Funciones, tuplas y diccionarios  ---  1.3 Ejercicios comprehension
#
#-----------------------------------------------------------------------------------------------------
"""1.   Crea una función llamada `squares_greater` que dada una lista de números, devuelva una nueva lista con los cuadrados de aquellos números mayores que 10."""
def squares_greater(lista):
    return [i * i for i in lista]

# --- int main () ----------------
lista = [1,2,3,4,5]
res = squares_greater(lista)
print(res)




"""2.   Crea una función llamada `word_length` que dada una lista de palabras, devuelva una nueva lista con la longitud de cada una siempre y cuando la palabra no sea "el"."""
def word_lenght(lista):
    return [ len(x) if x != "el" else 0 for x in lista ]

# --- int main () ----------------
lista = ["casa", "ola", "el", "coche"]
res = word_lenght(lista)
print(res)




"""3.	Crea una función llamada `clean_list` que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados."""
def clean_list(usuarios, baneados):
    no_baneados = []
    no_baneados.append([u for u in usuarios  if u not in baneados])
    return no_baneados

# --- int main () ----------------
usuarios = ["Pepe", "Juan", "Manolo", "Miguel"]
baneados = ["Pepe", "Miguel"]
res = clean_list(usuarios,baneados)
print(res)