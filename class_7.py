# 7. Create a class for representing animal, create a class for bear and class for wolf, create objects and use them

class Animal:
    def __init__(self, animal_type: str, gender: str, name: str, sound: str):
        self.animal_type = animal_type
        self.gender = gender
        self.name = name
        self.sound = sound

    def animal_info(self):
        print(f'hello I am {self.animal_type}, my name is {self.name} and my gender is {self.gender}')

    def animal_sound(self):
        print(f'my sound is {self.sound}')


class Bear(Animal):
    def __init__(self, animal_type: str, gender: str, name: str, sound: str):
        Animal.__init__(self, animal_type, gender, name, sound)

    def animal_info(self):
        print(f'hello I am {self.animal_type}, my name is {self.name} and my gender is {self.gender}')

    def animal_sound(self):
        print(f'my sound is {self.sound}')


class Wolf(Animal):
    def __init__(self, animal_type: str, gender: str, name: str, sound: str):
        Animal.__init__(self, animal_type, gender, name, sound)

    def animal_info(self):
        print(f'hello I am {self.animal_type}, my name is {self.name} and my gender is {self.gender}')

    def animal_sound(self):
        print(f'my sound is {self.sound}')


bear = Bear('bear', 'male', 'Teddy', 'roar')
bear.animal_info()

wolf = Wolf('wolf', 'male', 'Max', 'howl')
wolf.animal_sound()