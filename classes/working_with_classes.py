# Chapter 9: Working with classes and instances

# OOPs concepts(Object Oriented programming) - class, object, encapsulation, overriding
# encapsulation - hiding sensitive information from the object , child classes

class Car():
    # attribute - required, optional(dafualt)
    # bahaviour(actions) - CRUD operations -> set(CUD), get(R), other functions
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__mileage = 0    # hiding from the object , child classes - encapsulation

    def get_description(self):
        """gets all the details of the car"""
        print(f"Car details: \nManufecturer: {self.make},\tModel: {self.model},\tYear: {self.year}")
        print(f"Current Mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
        # applying the logic to our class, because logically mileage only increases and never goes down
        if new_mileage > self.__mileage:
            print("setting new value a mileage")
            self.__mileage = new_mileage
        else:
            print("mileage was less than current mileage, mileage not updated")

    def add_to_mileage(self, miles):
        """ increments the mileage with given miles. """
        if miles > 0:
            self.__mileage = self.__mileage + miles
            print(f"{miles} miles were added to your car mileage.")
        else:
            print("You cannot give negative number to increament mileage")

    def fill_the_tank(self):
        print('filling the tank...')
        print('Done. It is ready to hit the road!')

class Bike:
    pass

# to make it user-interacive use INPUT:
# make = input("Enter the make of the car: ")
# model = input("Enter the model of the car: ")
# year = input("Enter the year of the car: ")
# car2 = Car(make, model, year)
# car2.get_description()

# COMMENTED LINES DUE TO IMPORT IN CLASS_INHERITENCE.PY MODULE (FILE)
# car1 = Car('bmw', 'x5', 2022)
# print(car1.make, car1.year+1)
# print("--------------## GETTER functions--------------------")
# car1.get_description()
# print("------------- # SETTERs - updating the values of attributes ")
# car1.model = 'X5-M'
# # car1.__mileage = 50 # since mileage is hidden from the object we cannot update the value
# car1.set_mileage(50)
# car1.get_description()
# # car1.__mileage = 10
# car1.set_mileage(10)
# car1.get_description()
# # adding miles to the mileage
# print("Total mileage after adding more miles. ")
# # input: 100, -15
# car1.add_to_mileage(100)
# car1.get_description()
# car1.add_to_mileage(-15)
# car1.get_description()










