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
            get_num_rows(): Devuelve el numero de filas del avión
            get_num_seats_per_row(): Devuelve el número de asientos por fila en el avión
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
        """ Esta función devuelve el número de filas del avión
            Returns:
                int: número de filas del avión
        """
        return self.__num_rows
    

    def get_num_seats_per_row(self):
        """ Esta función devuelve el número de asientos por fila del avión
            Returns:
                int: número de asientos por fila del avión
        """
        return self.__num_seats_per_row


    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row  -- genera una tupla con 2 valores (lista_tam_filas+1, asientos_cada_fila)
        Returns: 
            rows: A list of Nones (size num_rows + 1). - todos inicializados a none al principio
            seats: A string of letters such as "ABCDEF"
        """
        rows = [None] * (len(Aircraft.get_num_rows())+1)
        seats = "ABCDEF"
        return (rows, seats)


    def num_seats(self):
        """Calculates the number of seats
            Returns:
            seats: The number of seats
        """
        seats = self.get_num_rows() * self.get_num_seats_per_row()
        return seats

    
   
 #----- CLASE AIRBUS ----------------------------------------------------------
class Airbus(Aircraft):
    def __init__(self, model, num_rows, num_seats_per_row, variant):
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row
        self.__variant = variant

    
    def get_model(self):
        return self.__model
    

    def get_num_rows(self):
        return self.__num_rows
    

    def get_num_seats_per_row(self):
        return self.__num_seats_per_row


    def get_variant(self):
        return self.__variant        
        


#----- CLASE BOEING ----------------------------------------------------------
class Boeing(Aircraft):
    def __init__(self, model, num_rows, num_seats_per_row, airline):
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row
        self.__airline = airline

    
    def get_model(self):
        return self.__model
    

    def get_num_rows(self):
        return self.__num_rows
    

    def get_num_seats_per_row(self):
        return self.__num_seats_per_row


    def get_airline(self):
        return self.__airline    