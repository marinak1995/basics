# scenarios
from while_loop import fuzz_buzz as fz #imports only 1 function fuzz_buzz
from while_loop import * #imports all functions
# FROM location_of_file IMPORT ...
from functions.functions_return import  *
# from lists.lists_loops import * #IMPORTS EVERYTHING FROM THE FILE AND EXECUTES


#import while_loop , we need to mention moduke name with each function use
#while_loop.fuzz_buzz()
print("# execution of functions from while_loop.py")
fz() # executing fuzz_buzz function with the alias name 'fz'
while_loop_increment()
while_loop_decrement()

print("# execution of functions from functions returns.py")
print("Result of the function: ", build_full_name('john', 'doe'))
person2 = build_full_name('jane', 'doe')
print('Person2:', person2)

print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))

# H/W 8-15












