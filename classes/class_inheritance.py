# Class inheritance:
from classes.working_with_classes import Car, Bike

print("-------------------------------------")
# Class B inherits class A
# CLass A is a parent of Class B,
# Class B (child) has everything that class A has
class A:
    name = 'I am from class A'

    def greet(self):
        print("Hello!")

class B:

    age = 25

    def get_age(self):
        print(f"My age is: {self.age}")

class C(A, B):
    pass
# object of class B has access to att and methods of class A and B
# item1 = B() #created an object # when class B inherits class A
item1 = C() # when class C inherits class A and B
print(item1.name)
print(item1.age)
item1.greet()
item1.get_age()

item2 = A() # has access to att and methods of both class A and B
print(item2.name)
item2.greet()

print(" Implementing the concepts with Car class ************************")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # super().__init__() executes the constructor of parent class
        self.battery_size = 80


    def fill_the_tank(self): # setting new logic
        """
        we are overriding the fill_the_tank function from the parent class.
        :return:
        """
        print("Sorry, this car does not have a tank, please go to charging station.")

    def get_description(self):
        super().get_description()
        print(f"Battery size: {self.battery_size}")



ecar1 = ElectricCar('tesla', 'model X', 2022)
ecar1.get_description()
ecar1.fill_the_tank()
ecar1.get_description()
print("--------------------------------------")
car1 = Car('bmw', 'x5', 2022)
car1.fill_the_tank()
car1.get_description()

# H/W 9-6 , 9-7, 9-8, 9-9









