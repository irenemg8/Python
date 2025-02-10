class Passenger:

    #Constructor
    def __init__(self, name, surname, id_card):    
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card


    def get_name(self):
        return self.__name


    def get_surname(self):
        return self.__surname


    def get_id_card(self):
        return self.__id_card


    def passenger_data(self):
        """Obtains the data of a passenger
           Returns:
                name: The passenger's name such as 'Jack'
                surname: The passenger's family name such as 'Shephard'
                id_card: The passenger's id card such as '85994003S'
            Lo devuelve en forma de tupla
        """
        res = (self.__name, self.__surname, self.__id_card)
        return res



""" -------- Pruebas ---------------------------
#--- int main()
p = Passenger("Jack", "Shephard", "85994003S")
res = p.passenger_data()
print(type(res))
---------------------------------------------"""