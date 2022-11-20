print('-------------exercise9-2-------------------')
"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is : {self.restaurant_name}.")
        print(f"This is  {self.cuisine_type} restaurant.")
    def open_restaurant(self):
        print(f'Welsome to {self.restaurant_name}! We are now Open!')

# Make an instance
restaurant1 = Restaurant('Brooklyn Pizza', 'Italian')

# Print the two attributes individually
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

# calling both methods.
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


# H/W 9-2, 9-3







