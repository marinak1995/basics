# Chapter 8: Functions (methods- in some other languages)
# defining, executing function, docstring
# function overriding - reseting content with the same name, program will use the lates version
# wrong way of using the functions: calling it before defining
# functions with parameters (arguments are passed when you execute)
# executing functions with positional arguments
# executing functions with parameters and arguments mentioned, position does not matter
# keyword arguments, passing the values mentioning parameters



#built-in functions: print(), input(), list.append(), sorted(), all the functions that come with open-close parantases
#user defined functions, functions that user created:
#we are defining the function with def, declairing the function name, registering :
def greet_user():
    print('Hello class!')
    print("Wonderful sunny day today!")

#call the function- execution
greet_user()
# what is docstring?

# overriding function
def greet_user():
    print('Hello world!')
    print("Enjoy the day!")

# function with argument: positional argument, required
def greet_user_by_name(name, day_of_week): #name is parameter in this case
    """function with argument: positional argument, required"""
    print(f'Hello, {name.title()}!')
    print(f"Enjoy your {day_of_week.title()} today!")

# execution: call the function
greet_user()
print('logged in to the system')
greet_user_by_name('jane', 'saturday')
greet_user_by_name('beni', 'sunday')
greet_user_by_name('mike', 'monday')

print('# Keyword arguments ___________________________')

greet_user_by_name(day_of_week='monday', name='mike') # I can mention name of parameter if I change their positions
greet_user()


# H/W: 8-1, 8-2

print("Default values__________________________")
def greet_user_by_name_with_def(name, day_of_week='monday'): # optional argument should always be added in the end after the positional one
    """function with default values: name is required, day of week is not required(optional)
    """
    print(f'Hello, {name.title()}!')
    print(f"Enjoy your, {day_of_week.title()} today!")
greet_user_by_name_with_def('kamran', 'sunday')
greet_user_by_name_with_def('nadia')
greet_user_by_name_with_def('jamshid', day_of_week='wednesday')
greet_user_by_name_with_def(day_of_week='wednesday', name='nina')

print(' Exercise 8.3 -------------------')
'''
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
'''

def make_shirt(size, text_to_print):
    '''
    prints message and size of the shirt
    '''
    print(f"The size of your shirt is {size.upper()}.")
    print(f"The  message to be printed on your shirt is: \n\t\t'{text_to_print.title()}'.")
make_shirt('medium', 'level up') #posiional ergument
make_shirt(text_to_print='level up', size='medium') #keyword argument

# H/W: 8-4, 8-5










