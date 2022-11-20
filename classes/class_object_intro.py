# Chapter 9: Classes and objects

# all class names should be named with title case
# each class will have attributs (variables), behaviour (functions)


class Dog():
    """
    Model of dogs, template for dogs.
    """
    # attribute (description) - variables, instance variables
    name = 'a'
    # breed = 'no breed'
    # size = 'medium'
    age = '2'
    # color = ''

    #   CONSTRUCTOR (OF THE CLASS WHEN YOU INSTANTIATE)
    # default functions to make required arguments
    # executed authomatically every time you create an object
    def __init__(self, name, breed, color, size='medium'):  # required, instance variables # this is assighned locally until we assign it to a global
        self.name = name # assigned local to a global function
        self.breed = breed
        self.color = color
        self.size = size

    # behaviour (actions) - functions/methods
    def eat(self): # self means this function belongs to the current class, it does not mean any parameter
        print(f'{self.name} is eating ....')
        print(f'{self.name} wants more ...')
        print(f'{self.name} done eating.')
    def run(self):
        miles = 5
        print(f'{self.name} is running {miles} miles.')
    def get_description(self):
        # run() # outside of the class
        # self.run() # within the class
        print(f"Name of the dog: {self.name}")
        print(f"Breed of the dog: {self.breed}")
        print(f"Color of the dog: {self.color}")
        print(f"Size of the dog: {self.size}")
        print(f"Age of the dog: {self.age}")

    pass

#instantiation - creating instance of the class - creating object:
# dog1 = Dog()
print('---------Dog1------------')
dog1 = Dog('chubby', 'chow chow', 'brown')
print('Name of the dog before changing the value: ', dog1.name)
dog1.name = 'trex' # assigning a value to the attributes
print('Name of the dog after assigning new name: ', dog1.name.title())
dog1.eat()
# dog1.size = 'small'
# dog1.breed = 'chow chow'
print('Dog1 breed: ', dog1.breed)
print('Dog1 color: ', dog1.color)
dog1.get_description()

print('---------Dog2--------------')
# Dog1 and Dog2 are objects
dog2 = Dog('max', 'german sheppard', 'black', 'large')
print(dog2.name)
print(dog2.breed)
dog2.get_description()















