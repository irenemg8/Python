# lista = [2, 3, 8)   # SyntaxError: invalid syntax  - error de sintaxis
#print(lista[9])      # IndexError: list index out of range - la posición 9 no existe en la lista

try:
    print(lista[9])
except:
    print("Se ha producido una excepción")

print("fin")



try:
    print(lista[9])
except:
    print("Se ha producido una excepción")

print("fin")





try:
    print(lista[9]) 

#De más específica a más general
except IndexError as e:
    print("Se ha producido una excepción de tipo IndexError")

except Exception as e:
    print("Se ha producido una excepción")

print("fin")








try:
    print(lista[9])
except (RuntimeError, IndexError) as e:
    print("Se ha producido una excepción", str(e))

print("fin")