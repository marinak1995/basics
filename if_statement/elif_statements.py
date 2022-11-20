# Chapter 5: ELIF statement:
# else if >> elif

#if expression1:
#    code to executr when expression1 is True
#elif expression2:
#    code to execute when condition2 is True
#elif expression3:
#    code to execute when condition3 is True
#elif expression4:
#    code to execute when condition4 is True
#else:
#    code to execute when none of above expression is True

age = 30
# if age is less than 0-17 then you can get DL,
# from 17-25, get DL pay more to insurance,
# older than 25 print dont drink and drive

if age < 17:
    print('Sorry, you still young, you can not get DL, just play PlayStation')
elif 17 <= age < 25:
    print('Good, you are eligible to get DL, but you will pay more to Insurance')
elif age >= 25: # or we can you else: instead of elif ...
    print('Great, if you have DL, please Do not Drink and Drive, Do not Smoke and Drive')
print('--------------------------------')


age = input('Please enter your age: ') # Input makes it more interactive, it asks the user to input and returns as string(always)
age = int(age) # one line version: age = int(input('Please enter your age: '))

if age < 17:
    print('Sorry, you still young, you can not get DL, just play PlayStation')
elif 17 <= age < 25:
    print('Good, you are eligible to get DL, but you will pay more to Insurance')
elif age >= 25: # or we can you else: instead of elif ...
    print('Great, if you have DL, please Do not Drink and Drive, Do not Smoke and Drive')


print('-----------------------------')

# H/W 5-3 to 5-7, 5-8 to 5-11

#Interview questions:
# H/W: Problem 1: If number dividable by 3 print "Fuzz", if number dividable by 5 then print "Buzz"
#      If number dividable by 3 and 5 then print "FuzzBuzz"

#n=10, n%3=1(remainder) -> 10 = 3*a + 1 , if n%3 == 0 its dividable by 3 m
if n % 3 == 0:
    print('dividable by 3')
else:
    print('this is not dividable by 3')

# H/W: Problem 2: how can you loop through the list of numbers and check that number 5 is in the list,
#     when you fing 5 then stop the loop print 'Hooray"
#     use 'break' keyword to stop the loop








