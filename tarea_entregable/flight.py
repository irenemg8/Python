from pprint import pprint
from passenger import *
from aircraft import *

class Flight:
    """ Representación de un vuelo
        Attributes:
            number (str): Número de vuelo
            aircraft (Aircraft): Modelo de avión
            seating (list): Lista de diccionarios con la información de los asientos

        Methods:
            get_number(): Devuelve el número de vuelo
            get_aircraft_model(): Devuelve el modelo de avión
            get_seating(): Devuelve la lista de asientos
            allocate_passenger(seat, passenger): Asigna un asiento a un pasajero
            reallocate_passenger(from_seat, to_seat): Reasigna un pasajero a un asiento diferente
            num_available_seats(): Devuelve el número de asientos disponibles
            print_seating(): Imprime en consola el plan de asientos
            print_boarding_cards(): Imprime en consola la tarjeta de embarque de cada pasajero
            __parse_seat(seat): Divide un designador de asiento en fila y letra
            __passenger_seats(): Generador para iterar las ubicaciones de asientos ocupadas
    """
    
    def __init__(self, number, aircraft):    
        """ Inicializa un vuelo con su número y modelo de avión
        Args:
            number (str): Número de vuelo
            aircraft (Aircraft): Modelo de avión
        """
        """------ Excepciones ------"""
        if not number[:2].isalpha():
            raise ValueError("Los dos primeros caracteres deben ser letras")
        
        if not number[:2].isupper():
            raise ValueError("Los dos primeros caracteres deben ser mayúsculas")
        
        if not number[2:].isdigit():
            raise ValueError("Todos los caracteres a partir del tercero deben ser números")
        
        if int(number[2:]) > 9999:
            raise ValueError("Los caracteres a partir del tercero exceden el 9999")
        """-------------------------"""

        self.__number = number
        self.__aircraft = aircraft
        rows, seats = self.__aircraft.seating_plan()
        self.__seating = [{"Seat": f"{row}{seat}", "Passenger": None} for row in range(1, len(rows)) for seat in seats]


    def get_number(self):
        """ Esta función devuelve el número de vuelo
            Returns:
                string: Número de vuelo
        """
        return self.__number
    
    
    def get_aircraft_model(self):
        """ Esta función devuelve el modelo de avión
            Returns:
                string: modelo de avión
        """
        return self.__aircraft
    

    def get_seating(self):
        """ Esta función devuelve la lista de asientos
            Returns:
                list: lista de asientos
        """
        return self.__seating
    

    def allocate_passenger(self,seat,passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """

        """------ Excepciones ------"""
        if len(seat) < 2:
            raise ValueError("El asiento debe tener al menos 2 caracteres (un número y una letra).")
        
        if seat is None:
            raise ValueError("El asiento no debe estar vacío.")
        
        if passenger is None:
            raise ValueError("El pasajero no debe estar vacío.")
        """-------------------------"""

        dic = self.get_seating()
        for i in dic:
            if (seat is not None ) and (i["Seat"] == seat):
                i["Passenger"] = passenger


    def reallocate_passenger(self, from_seat, to_seat):
        """Reallocate a passenger to a different seat
        Args:
            from_seat: The existing seat designator for the passenger such as '12C'
            to_seat: The new seat designator
        """

        """------ Excepciones ------"""
        if len(to_seat) < 2:
            raise ValueError("El asiento debe tener al menos 2 caracteres (un número y una letra).")
        
        if from_seat is None:
            raise ValueError("El sitio origen no debe estar vacío, debe tener al pasajero que queremos mover de sitio.")
        
        if from_seat == to_seat:    
            raise ValueError("El asiento de origen y el de destino no pueden ser iguales.")
        """-------------------------"""

        dic = self.get_seating()
        pasajero = None
        for i in dic:
            if i["Seat"] == from_seat:
                pasajero = i["Passenger"]
                i["Passenger"] = None 
                break

        if pasajero is None:
            raise ValueError(f"No hay pasajero en el asiento {from_seat}")

        for i in dic:
            if i["Seat"] == to_seat:
                if i["Passenger"] is not None:
                    raise ValueError("El sitio destino debe estar vacío.")
                i["Passenger"] = pasajero
                break
        

    def num_available_seats(self):
        """Obtains the amount of unoccupied seats
        Returns:
            The number of unoccupied seats  
        """
        contador = 0
        dic = self.get_seating()
        for i in dic:
            if i["Passenger"] == None:
                contador += 1
        return contador


    def print_seating(self):
        """Prints in console the seating plan
            Example of one row:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        dic = self.get_seating()
        for i in dic:
            pprint(i)


    def print_boarding_cards(self):
        """Prints in console the boarding card for each passenger
            Example of one boarding card:
            ----------------------------------------------------------
            |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
            ----------------------------------------------------------
        """
        dic = self.get_seating()
        for i in dic:
            if i["Passenger"] != None:
                print("----------------------------------------------------------")
                print("|     ", i["Passenger"][0], i["Passenger"][1], i["Passenger"][2], i["Seat"], self.get_number(), self.get_aircraft_model().get_model(), "     |")
                print("----------------------------------------------------------")
    

    def __parse_seat(self, seat):
        """Divide a seat designator in row and letter
            Args:
                seat: The seat designator to be divided such as '12C'
            Returns:
                row: The row of the seat such as 12
                letter: The letter of the seat such as 'C'
        """

        """------ Excepciones ------"""
        if len(seat) < 2:
            raise ValueError("El asiento debe tener al menos 2 caracteres (un número y una letra).")

        if (not seat[-1].isalpha()) or (seat[-1].upper() not in self.get_aircraft_model().seating_plan()[1]):   #Recordatorio: seating_plan() devuelve (rows, seats)  ->  0 = rows, 1 = seats
            raise ValueError("El último caracter debe ser una letra y debe ser una letra válida para el Aircraft que tenga asociado este vuelo.")
        
        if not seat[:-1].isdigit():
            raise ValueError("Todos los caracteres excepto el último deben ser números")
        
        if int(seat[:-1]) > self.get_aircraft_model().seating_plan()[0]:   #Recordatorio: seating_plan() devuelve (rows, seats)  ->  0 = rows, 1 = seats
            raise ValueError("El número que forman estos caracteres debe ser un valor de fila válido para el `Aircraft` que tenga asociado este vuelo.")
        """-------------------------"""

        row = seat[:-1]
        letter = seat[-1]
        return row, letter
        

    def __passenger_seats(self):
        """A generator function to iterate the occupied seating locations
            Returns:
            generator: Tuple of the passenger data and the seat
        """
        dic = self.get_seating()
        for i in dic:
            yield (i["Passenger"], i["Seat"])
