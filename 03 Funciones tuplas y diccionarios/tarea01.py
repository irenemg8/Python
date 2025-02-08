#--------------------------------------------------------------------------------------
#
#   Ejercicios del Colab 03 Funciones, tuplas y diccionarios  ---  4.2 Tarea resumen
#
#--------------------------------------------------------------------------------------


"""Escribe un programa llamado **tarea01.py** que permita gestionar clientes mediante un diccionario. Cada cliente estará definido según puedes ver en la siguiente imagen (**no cambies los nombres**):

CLIENT:
NIF: string
name: string
address: string
phone: string
email: string
VIP: boolean


El programa mostrará un menú con las siguientes opciones y en función de la opción elegida por el usuario, se preguntarán unos datos, se llamará a una función diferente y se volverá a mostrar el menú:
* Añadir cliente: se preguntarán los datos del cliente y se añadirán al diccionario.
* Borrar cliente: se preguntará su NIF y se borrará el cliente.
* Mostrar cliente: se preguntará su NIF y se mostrarán sus datos.
* Listar clientes: se mostrarán los datos de todos los clientes.
* Listar clientes VIP: se mostrará los datos de todos los clientes que sean VIP.
* Terminar: terminará el programa.

Cada una de las funciones correspondientes a estas opciones, tiene que tener un **perfil y nombre concretos**, tal y como puedes ver a continuación:


add_client()
    Args: nif (string), name (string), address (string), phone (string), email (string), vip (bool)
    
delete_client()
    Args: nif (string)
    
get_client()
    Args: nif (string)
    Returns: nif (string), name (string), address (string), phone (string), email (string), vip (bool)

get_clients()
    Returns: iterator
   
get_vip_clients()
    Returns: dictionary
   
    

Algunas aclaraciones que debes tener en cuenta:

*   Puedes utilizar las claves que quieras para definir los elementos.
*   La función `add_client` no tendrá en cuenta si existe o no el cliente. Asumimos que siempre le pasaremos un NIF inexistente.
*   La función `delete_client` no tendrá en cuenta si existe o no el cliente. Asumimos que siempre le pasaremos un NIF existente.
*   La función `get_client` devolverá una tupla con los datos de un cliente concreto y no comprobará si existe o no. Asumimos que siempre le pasaremos un NIF existente.
*   La función `get_clients` devolverá un iterator para poderlo recorrer desde fuera y mostrar los datos de cada cliente.
*   La función `get_vip_clients` tendrá mayor nota si utiliza comprehension.

"""


# Diccionario para almacenar los clientes
clientes = {}

#Añadir un cliente al diccionario
def add_client(nif, name, address, phone, email, vip):
    clientes[nif] = {
        'NIF': nif,
        'name': name,
        'address': address,
        'phone': phone,
        'email': email,
        'VIP': vip
    }

#Borrar un cliente del diccionario por su NIF
def delete_client(nif):
    if nif in clientes:
        del clientes[nif]

#Obtener los datos de un cliente del diccionario por su NIF
def get_client(nif):
    if nif in clientes:
        cliente = clientes[nif]
        return (cliente['NIF'], cliente['name'], cliente['address'], cliente['phone'], cliente['email'], cliente['VIP'])
    return None

#Obtener un iterador de todos los clientes
def get_clients():
    return iter(clientes.values())

#Obtener los clientes VIP
def get_vip_clients():
    return {nif: cliente for nif, cliente in clientes.items() if cliente['VIP']}

#Mostrar menú principal
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Añadir cliente")
    print("2. Borrar cliente")
    print("3. Mostrar cliente")
    print("4. Listar clientes")
    print("5. Listar clientes VIP")
    print("6. Terminar")

#Ejecutar la opción seleccionada del menú
def ejecutar_opcion(opcion):
    if opcion == 1:  # Añadir cliente
        nif = input("Introduce el NIF: ")
        name = input("Introduce el nombre: ")
        address = input("Introduce la dirección: ")
        phone = input("Introduce el teléfono: ")
        email = input("Introduce el correo electrónico: ")
        vip = input("¿Es VIP? (True/False): ").lower() == 'true'
        add_client(nif, name, address, phone, email, vip)
        print("Cliente añadido.")
    
    elif opcion == 2:  # Borrar cliente
        nif = input("Introduce el NIF del cliente a borrar: ")
        delete_client(nif)
        print(f"Cliente con NIF {nif} borrado.")
    
    elif opcion == 3:  # Mostrar cliente
        nif = input("Introduce el NIF del cliente: ")
        cliente = get_client(nif)
        if cliente:
            print(f"Cliente encontrado: {cliente}")
        else:
            print("Cliente no encontrado.")
    
    elif opcion == 4:  # Listar todos los clientes
        for cliente in get_clients():
            print(cliente)
    
    elif opcion == 5:  # Listar clientes VIP
        vip_clients = get_vip_clients()
        for nif, cliente in vip_clients.items():
            print(cliente)
    
    elif opcion == 6:  # Terminar
        print("Programa terminado.")
        return False
    return True


def main():
    """Función principal que ejecuta el programa"""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")
        
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            continuar = ejecutar_opcion(int(opcion))
            if not continuar:
                break
        else:
            print("Opción no válida. Por favor, elige entre 1 y 6.")
        
if __name__ == "__main__":
    main()
