#------------------------------------------------------------------------------------------------------------
#
#   Ejercicios del Colab 03 Funciones, tuplas y diccionarios  ---  4.1 Ejercicios iteradores y generadores
#
#------------------------------------------------------------------------------------------------------------
"""1. Escribe una función generadora de la secuencia de Fibonacci y comprueba su correcto funcionamiento. Los valores de esta secuencia se calculan siguiendo la siguiente fórmula:

$$ F_0 = 0 $$
$$ F_1 = 1 $$
$$ F_n = F_{n-1} + F_{n-2} \hspace{0.5cm} \forall n > 1$$
"""
def fibonacci():
    a = 0
    b = 1 
    while True:  # La secuencia es infinita, por lo que usamos un bucle infinito
        yield a  # Genera el siguiente valor en la secuencia
        a, b = b, a + b  # Calculamos el siguiente valor de la secuencia

# --- int main () ----------------
generador = fibonacci()

#Recorremos el generador
"""for i in generador:
  print(i)"""


"""2. Implementa la siguiente función generadora:"""
def suma_tiempos(inicio, fin, incremento):
    """Función que devuelve tuplas de tiempo (hh,mm,ss) desde una hora inicial hasta una hora final
    Args: inicio (hh,mm,ss), fin (hh,mm,ss), incremento (segundos)
    Returns: hora (hh,mm,ss)
    """
    # Convertimos las horas, minutos y segundos en segundos desde el inicio del día
    inicio_seg = inicio[0] * 3600 + inicio[1] * 60 + inicio[2]
    fin_seg = fin[0] * 3600 + fin[1] * 60 + fin[2]
    
    # Generamos las tuplas de tiempo desde el inicio hasta el fin, con el incremento deseado
    tiempo_actual = inicio_seg
    while tiempo_actual <= fin_seg:
        hh = tiempo_actual // 3600
        mm = (tiempo_actual % 3600) // 60
        ss = tiempo_actual % 60
        yield (hh, mm, ss)  # Generamos la tupla (hh, mm, ss)
        tiempo_actual += incremento  # Incrementamos el tiempo

# --- int main () ----------------
inicio = (9, 0, 0)  # 09:00:00
fin = (9, 10, 0)    # 09:10:00
incremento = 60     # 60 segundos

# Usamos la función generadora
for hora in suma_tiempos(inicio, fin, incremento):
    print(hora)