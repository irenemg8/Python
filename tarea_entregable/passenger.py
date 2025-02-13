from flight import *

class Passenger:
    """ Representación de un pasajero de un vuelo
        Attributes:
            name (str): El nombre de la persona
            surname (str): El apellido de la persona
            id_card (str): El id de identificación del pasajero

        Methods:
            passenger_data(): Muestra los datos del pasajero (name, surname, id_card) en formato tupla
    """
    
    
    def __init__(self, name, surname, id_card):    
        """ Inicializa un pasajero con sus datos
        Args:
            name (str): El nombre de la persona
            surname (str): El apellido de la persona
            id_card (str): El id de identificación del pasajero
        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card


    def passenger_data(self):
        """Obtains the data of a passenger
            Returns:
                name: The passenger's name such as 'Jack' - string
                surname: The passenger's family name such as 'Shephard' - string
                id_card: The passenger's id card such as '85994003S' - string
            Lo devuelve en forma de tupla
        """
        return (self.__name, self.__surname, self.__id_card)



""" -------- Pruebas ---------------------------
#--- int main()
p = Passenger("Jack", "Shephard", "85994003S")
res = p.passenger_data()
print(res)
#print(type(res))
---------------------------------------------"""