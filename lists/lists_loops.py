# Chapter 4: Looping through the list

places = ['hawaii', 'paris', 'bahamas', 'iceland', 'canada']
# Loops - executing the code repetitively (what to loop, how many times)
print('Looping through entire list: ')

print(f"I want to visit {places[0]} next summer")
# for var_each_element in list_name:
#     print('lines of code to be repeated') - make sure this line starts with 4 spaces
print("we are looping through rge places")
for place in places: # variable place is only in this scope, and is not recognizable ouside of this scope
    print(place) # prints each element in the list separately
    #pass - means do nothing, skip
    print(f"I want to visit {place.title()} next summer") # repeating line with each element of the list
    print(f'How far is the {place.title()} from new york?')
print("Ohhhh I need to convince my wife now.")

# H/W: 4-1, 4-2

print("Working with list of numbers, range() functions")
# range(5) -> 0, 1, 2, 3, 4
# range(2, 6) -> 2, 3, 4, 5
# range(4, 15, 3{step, how much it will be incimented to next number}) -> 4, 7, 10, 13

print(range(5))
print( list(range(5)) )

print('------')
for num in range(5):
    print(f'Each number: {num}')

print('-----')
for num in range(2, 6):
    print(f'Each number: {num}')

print('-------')
for num in range(4, 16, 3):
    print(f'Each number: {num}')
print("--------")

# Problem solving:
# problem1: list all numbers between 21 abd 36 that can be devided by 4

list_of_numbers = []
for num in range(24, 37, 4):
    print(f"each number: {num}")
    list_of_numbers.append(num)
print(f'list of numbers: {list_of_numbers} ')
print('------')

# problem 2: list the squares of numbers between 25 and 30

num_squares = []
for num in range(25, 31):
    print(f'num= {num} and square is: {num**2}')
    num_squares.append(num**2)
print("final list of squares", num_squares)
print('------')


print('*******')
nums = [4, 2, 9, 10]
print(sum(nums))

print('******')
sum = 0
for num in nums:
    sum = sum + num
print(sum)

# H/W 4-3 to 4-9







