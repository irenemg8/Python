"""
lista = [elemento_1, elemento_2, ... elemento_n]
tupla = (elemento_1, elemento_2, ... elemento_n)
diccionario = {llave:valor}
"""


lenguajes = ["pyton", 51, "python", True]

lenguajes [0]  # python

len(lenguajes)  #longitud = 4

lenguajes [-1]  #True

lenguajes [0:2]  #python, 51


#Lista dentro de listas
programacion = [lenguajes, "hola", "casa"]
# [ ["pyton", 51, "python", True], "hola", "casa"]

programacion [0][0]   #para acceder a python
programacion [0][1]   #para acceder a 51


lenguajes.extend(programacion)    #añade los elementos de prog en las últimas posiciones
lenguajes.append(programacion)    #añade los elementos de prog en LA ÚLTIMA POS todos los eleemntos


