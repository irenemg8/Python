from flight import *

class Aircraft:
    """ Representación de un avión
        Attributes:
            registration (str): Registro
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión

        Methods:
            get_registration(): Devuelve el registro
            get_model(): Devuelve el modelo de avión
            seating_plan(): Devuelve una tupla con la lista de filas y los asientos por fila
            num_seats(): Devuelve el número de asientos del avión
    """


    def __init__(self, registration, model, num_rows, num_seats_per_row):    
        """ Inicializa un pasajero con sus datos
        Args:
            registration (str): Registro
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    
    def get_registration(self):
        """ Esta función devuelve el registro
            Returns:
                string: El registro
        """
        return self.__registration
    

    def get_model(self):
        """ Esta función devuelve el modelo de avión
            Returns:
                string: modelo de avión
        """
        return self.__model
    
    
    def get_num_rows(self):
        """ Esta función devuelve el numero de filas
            Returns:
                int: numero de filas
        """
        return self.__num_rows
    
    
    def get_num_seats_per_row(self):
        """ Esta función devuelve el numero de asientos por fila
            Returns:
                int: numero de asientos por fila
        """
        return self.__num_seats_per_row
    
    
    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
            Returns: 
                rows: A list of Nones (size num_rows + 1).
                seats: A string of letters such as "ABCDEF"
                ----- type: Tupla
        """
        rows = [None] * (len(self.__num_rows) + 1)
        seats = "ABCDEF"[:self.__num_seats_per_row]
        return (rows, seats)     
       

    def num_seats(self):
        """Calculates the number of seats
            Returns:
            seats: The number of seats
        """
        seats = len(self.get_num_rows()) * len(self.get_num_seats_per_row())
        return seats

    
   
 #----- CLASE AIRBUS ----------------------------------------------------------
class Airbus(Aircraft):
    """ Representación de un avión de la marca Airbus
        Attributes:
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión
            variant (str): Variante del avión

        Methods:
            get_variant(): Devuelve la variante del avión
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row, variant):
        """ Inicializa un avión de la marca Airbus
        Args:
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión
            variant (str): Variante del avión
        """
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__variant = variant

    def get_variant(self):
        """ Esta función devuelve la variante del avión
            Returns:
                string: variante del avión
        """
        return self.__variant        
        


#----- CLASE BOEING ----------------------------------------------------------
class Boeing(Aircraft):
    """ Representación de un avión de la marca Boeing
        Attributes:
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión
            airline (str): Aerolinea del avión

        Methods:
            get_airline(): Devuelve la aerolínea del avión
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row, airline):
        """ Inicializa un avión de la marca Airbus
        Args:
            model (str): El modelo de avión
            num_rows (int): Número de filas del avión
            num_seats_per_row (int): Número de asientos por fila en el avión
            airline (str): Aerolinea del avión
        """
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__airline = airline

    def get_airline(self):
        """ Esta función devuelve la aerolínea del avión
            Returns:
                string: aerolinea del avión
        """
        return self.__airline    