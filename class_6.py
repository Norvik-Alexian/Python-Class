# Create a class for representing building with some attributes and behavior, create a classes for representing hotel
# building with specific attributes and behavior, create objects and use them.

class Building:
    def __init__(self, floor: int, elevator: int, manager: str):
        self.floor = floor
        self.elevator = elevator
        self.manager = manager

    def change_manager(self, new_manager: str):
        self.manager = new_manager
        print(f'{self.manager} is the new manager of the building')

    def add_elevator(self):
        self.elevator += 1
        print(f'this building now has {self.elevator} elevators')


class Hotel(Building):
    def __init__(self, floor, elevator, manager, rooms: int):
        Building.__init__(self, floor, elevator, manager)
        self.rooms = rooms

    def change_manager(self, new_manager: str):
        self.manager = new_manager
        print(f'{self.manager} is the new manager of the hotel')


hotel = Hotel(10, 2, 'Pouria', 50)
hotel.change_manager('Norvik')
