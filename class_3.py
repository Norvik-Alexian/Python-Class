# Create a class for representing a ticket with some attributes (from location, to location, transport type, duration
# in minutes, arrival time, passenger) and behavior (set from/to, change transport type, increase duration by some number,
# set passenger), create several tickets and perform operations on them.

class Ticket:
    def __init__(self, from_location: str, to_location: str, transport_type: str, duration: int, passengers: int, arrival_time: int):
        self.from_location = from_location
        self.to_location = to_location
        self.transport_type = transport_type
        self.duration = duration
        self.passengers = passengers
        self.arrival_time = arrival_time

    def increase_duration(self, increased_time: int):
        self.duration += increased_time
        print(f'Duration of this trip increased now the duration is {self.duration} hours.')

    def change_transport_type(self, new_transport: str):
        self.transport_type = new_transport
        print(f'New transportation for this trip is {self.transport_type}.')

    def passengers_amount(self, new_passengers_amount):
        self.passengers += new_passengers_amount
        print(f'Total of the passengers in this trip is {self.passengers} people.')


trip = Ticket('Yerevan', 'Canada', 'airplane', 12, 120, 3)
trip.increase_duration(3)
trip.change_transport_type('train')
trip.passengers_amount(50)
