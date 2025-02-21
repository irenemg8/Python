import flight as f
"""
# Test de creación de vuelo
def test_create_flight1():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    assert f1.get_number() == "BA117"
    assert f1.get_aircraft_model().get_registration() == "G-EUAH"
    assert f1.get_aircraft_model().get_model() == "Airbus A319"
    assert f1.get_aircraft_model().get_num_rows() == 22
    assert f1.get_aircraft_model().get_num_seats_per_row() == 6

def test_create_flight2():
    f2 = f.Flight(number = "AF92", aircraft = f.Boeing(registration = "F-GSPS", airline = "Emirates"))
    assert f2.get_number() == "AF92"
    assert f2.get_aircraft_model().get_registration() == "F-GSPS"
    assert f2.get_aircraft_model().get_airline() == "Emirates"

def test_create_flight3():
    f3 = f.Flight(number = "BA148", aircraft = f.Airbus(registration = "G-EUPT", variant = "A319-100"))
    assert f3.get_number() == "BA148"
    assert f3.get_aircraft_model().get_registration() == "G-EUPT"
    assert f3.get_aircraft_model().get_variant() == "A319-100"

# Test de asignación de pasajeros
def test_allocate_passenger1():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert f1.get_seating()[0]["Passenger"] == p1.passenger_data()

def test_allocate_passenger2():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    assert f1.get_seating()[0]["Passenger"] == p1.passenger_data()
    assert f1.get_seating()[1]["Passenger"] == p2.passenger_data()

# Test de reasignación de pasajeros
def test_reallocate_passenger1():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.reallocate_passenger("12A", "12B")
    assert f1.get_seating()[0]["Passenger"] == None
    assert f1.get_seating()[1]["Passenger"] == p1.passenger_data()

def test_reallocate_passenger2():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    f1.reallocate_passenger("12A", "12B")
    assert f1.get_seating()[0]["Passenger"] == None
    assert f1.get_seating()[1]["Passenger"] == p1.passenger_data()

# Test de número de asientos disponibles
def test_num_seats_available1():
    f1 = f.Flight(number = "BA117", aircraft = f.Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert f1.num_available_seats() == 131

    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    assert f1.num_available_seats() == 130

    f1.reallocate_passenger("12A", "12B")
    assert f1.num_available_seats() == 131

    f1.reallocate_passenger("12B", "12A")
    assert f1.num_available_seats() == 130

    f1.allocate_passenger("12A", p1.passenger_data())
    f1.allocate_passenger("12B", p2.passenger_data())
    assert f1.num_available_seats() == 129

    f1.reallocate_passenger("12A", "12B")
    f1.reallocate_passenger("12B", "12A")
    assert f1.num_available_seats() == 129

def test_num_seats_available2():
    f2 = f.Flight(number = "AF92", aircraft = f.Boeing(registration = "F-GSPS", airline = "Emirates"))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f2.allocate_passenger("12A", p1.passenger_data())
    assert f2.num_available_seats() == 0

    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f2.allocate_passenger("12B", p2.passenger_data())
    assert f2.num_available_seats() == 0

    f2.reallocate_passenger("12A", "12B")
    assert f2.num_available_seats() == 0

    f2.reallocate_passenger("12B", "12A")
    assert f2.num_available_seats() == 0

    f2.allocate_passenger("12A", p1.passenger_data())
    f2.allocate_passenger("12B", p2.passenger_data())
    assert f2.num_available_seats() == 0"""



def test_allocate_passenger1():
    f1 = f.Flight(number="BA117", aircraft=f.Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"})
    assert f1.get_seating()[0]["Passenger"] == {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"}

def test_allocate_passenger2():
    f1 = f.Flight(number="BA117", aircraft=f.Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"})
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", {"first_name": "Kate", "last_name": "Austen", "passport_number": "12589756P"})
    assert f1.get_seating()[0]["Passenger"] == {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"}
    assert f1.get_seating()[1]["Passenger"] == {"first_name": "Kate", "last_name": "Austen", "passport_number": "12589756P"}

def test_reallocate_passenger1():
    f1 = f.Flight(number="BA117", aircraft=f.Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"})
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", {"first_name": "Kate", "last_name": "Austen", "passport_number": "12589756P"})
    f1.reallocate_passenger("12A", "12C")  # Cambiar a un asiento vacío
    assert f1.get_seating()[0]["Passenger"] == None
    assert f1.get_seating()[2]["Passenger"] == {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"}

def test_num_seats_available1():
    f1 = f.Flight(number="BA117", aircraft=f.Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = f.Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", {"first_name": "Jack", "last_name": "Shephard", "passport_number": "85994003S"})
    assert f1.num_available_seats() == 131
    p2 = f.Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", {"first_name": "Kate", "last_name": "Austen", "passport_number": "12589756P"})
    assert f1.num_available_seats() == 130
    f1.reallocate_passenger("12A", "12C")
    assert f1.num_available_seats() == 131
    f1.reallocate_passenger("12B", "12A")
    assert f1.num_available_seats() == 130
