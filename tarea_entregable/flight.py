from pprint import pprint
from passenger import *
from aircraft import *

class Flight:

    #Constructor
    def __init__(self, number, aircraft, seating):    
        self.__number = number
        self.__aircraft = aircraft
        self.__seating = seating 


    def get_number(self):
        return self.__number
    
    
    def get_aircraft_model(self):
        return self.__aircraft
    

    def get_seating(self):
        return self.__seating
    

    def allocate_passenger(self,seat,passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
        dic = self.get_seating()
        for i in dic:
            if i["Seat"] == seat:
                i["Passenger"] = passenger


    def reallocate_passenger(self, from_seat, to_seat):
        """Reallocate a passenger to a different seat
        Args:
            from_seat: The existing seat designator for the passenger such as '12C'
            to_seat: The new seat designator
            """
        dic = self.get_seating()
        for i in dic:
            if i["Seat"] == from_seat:
                 i["Seat"] = to_seat
        

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
                print("|     ", i["Passenger"][0], i["Passenger"][1], i["Passenger"][2], i["Seat"], self.get_number(), self.get_aircraft_model(), "     |")
                print("----------------------------------------------------------")
    

    def parse_seat(self, seat):
        """Divide a seat designator in row and letter
            Args:
                seat: The seat designator to be divided such as '12C'
            Returns:
                row: The row of the seat such as 12
                letter: The letter of the seat such as 'C'
        """
        row = seat[:-1]
        letter = seat[-1]
        return row, letter
        

    def passenger_seats(self):
        """A generator function to iterate the occupied seating locations
            Returns:
            generator: Tuple of the passenger data and the seat
        """
        dic = self.get_seating()
        for i in dic:
            yield (i["Passenger"], i["Seat"])
            