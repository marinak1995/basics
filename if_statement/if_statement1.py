# Chapter 5: If statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(f'car value was bmw so we are doing print differently: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() print: {car.title()}')
print('------------------------------')
# 'and' operator , 'or' operator

for car in cars:
    if car == 'bmw' and 2 == 2: #2 compared to 2 is True
        print(f'car value was bmw so we are doing print differently: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() print: {car.title()}')



# Expressions:

name = 'john'
num = 45.55
is_good = True
friends = []


#name == 'jane' # False, cheching if the value of the name ar is equal of 'jane'
#name > 'abc' # True,   A-z (a, b, .... j...)
#num == 45 #False
#num > 45 #True
#name.lower() != 'jane' #True

if friends: #if list is empty we dont need to use any exprssion, just name the list
    print('frineds is not empty list')
else:
    print('frineds expressions returned false, this means it is empty list')


print('---------------------------------')
#cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
if 'tesla' in cars:
    print('cars list includes tesla')
else:
    print(f'tesla is not in the cars list.')

# H/w Exercise 5-1, 5-2















