import pytest
from aircraft import Aircraft, Airbus, Boeing
from passenger import Passenger
from flight import Flight

def test_creacion_objetos_flight():
    """
    Prueba la creación de objetos Flight.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    assert f1.get_number() == "BA117"
    assert f1.get_aircraft_model().get_model() == "Airbus A319"

    f2 = Flight(number="AF92", aircraft=Boeing(registration="F-GSPS", airline="Emirates"))
    assert f2.get_number() == "AF92"
    assert f2.get_aircraft_model().get_model() == "Boeing 777"

    f3 = Flight(number="BA148", aircraft=Airbus(registration="G-EUPT", variant="A319-100"))
    assert f3.get_number() == "BA148"
    assert f3.get_aircraft_model().get_variant() == "A319-100"

def test_allocate_passenger():
    """
    Prueba la asignación de pasajeros a los asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert any(seat["Seat"] == "12A" and seat["Passenger"] == p1.passenger_data() for seat in f1.get_seating())

    p2 = Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    assert any(seat["Seat"] == "12B" and seat["Passenger"] == p2.passenger_data() for seat in f1.get_seating())

def test_reallocate_passenger():
    """
    Prueba la reasignación de pasajeros a diferentes asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert any(seat["Seat"] == "12C" and seat["Passenger"] is None for seat in f1.get_seating())
    f1.reallocate_passenger("12A", "12C")
    assert any(seat["Seat"] == "12A" and seat["Passenger"] is None for seat in f1.get_seating())
    assert any(seat["Seat"] == "12C" and seat["Passenger"] == p1.passenger_data() for seat in f1.get_seating())

    p2 = Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    assert any(seat["Seat"] == "12D" and seat["Passenger"] is None for seat in f1.get_seating())
    f1.reallocate_passenger("12B", "12D")
    assert any(seat["Seat"] == "12B" and seat["Passenger"] is None for seat in f1.get_seating())
    assert any(seat["Seat"] == "12D" and seat["Passenger"] == p2.passenger_data() for seat in f1.get_seating())

def test_num_available_seats():
    """
    Prueba el número de asientos disponibles.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    assert f1.num_available_seats() == 22 * 6
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert f1.num_available_seats() == 22 * 6 - 1

    p2 = Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12B", p2.passenger_data())
    assert f1.num_available_seats() == 22 * 6 - 2

    f1.reallocate_passenger("12A", "12C")
    assert f1.num_available_seats() == 22 * 6 - 2

    f1.reallocate_passenger("12B", "12A")
    assert f1.num_available_seats() == 22 * 6 - 2

if __name__ == "__main__":
    pytest.main()
