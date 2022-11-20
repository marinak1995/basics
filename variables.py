# comment line
print("Hello Wortld!")

# variable - storage while code runs, varname = value
# note : name should be
# 1. should not start with numbers
# 2. starts woth lower case (highly preferable)
#
a = 45 # number, integer (data type)
b = 6.78 # number, integer (data type)
name = 'jamal' # text, i.e. string (data type)
msg = "Hello, this is my first coding practice!!!" # string



print(a)
print(a)
print(a)
print(a) # command+D copies the line

a=90
print(a) # changed the value of a 
print(a)
print(a)

print(b)
print(name)
print(msg)


# 10/9/2022

a = a + 1

print(a)

print("name before title", name)
print("name with title", name.title())
print("name after title", name)

print("using is lower: ", name.islower()) # is.. returns True or False
print(name.upper())
print(name.lower())
print(name.lower()) # command + D duplicates previous line

print('My message is : ' + name.title() + ', ' + msg.upper()) # concatenation

print('special characters: \\t  \\n') # t for Tab, n for new line as if when you hit Enter
print('My message is:\t\t\t' + name.title() + ',\n\t\t\t\t' + msg.upper())

location =  ' \thawai\n\t'
print(location)
print(location.strip()) # strip() will remove spaces from both sides, rstrip() - in the end, lstrip() in the begining
print('My wedding venue: ' + location.strip()+ ' islands')
print('My wedding venue: ' + location.strip().upper() + ' islands')

print('##### working with numbers ##############')
num1 = 3
num2 = 8
print("addition: ", num1 + num2)
print("substraction: ", num1 - num2)
print("multiplication: ", num1 * num2)
print("division: ", num1 / num2)
print("exponent: ", num1 ** 2) # exponent "Stepen'"
print("floor division: ", 20 // num1) #how many num1 in num2, always returns integer
print("modulo: ", 20 % num1) # 20= num1*3 + 2, so 2 is modulo, remainder number after devision ...

#find odd numbers 20-50 -> 21 (21= 2*10 +1), 23 (2*11 +1)
# if n%2 returns 1 then n is add number (pseudocode)
# if n%2 returns 0 then n is ene number (pseudocode)

print('addition: :' + str(num1 + num2)    ) # str converts numbers to a string(text)
num3 = '456' #this is a string because it's covered by quotes

num4 = 45.4566 #this is a float data type
print("addition with num3: ", num1 + int(num3)) #int converts expression to intiger if possible
print('converted to int:', int(num4))

print(num1)
print(int(num4))

#summary:
# variables (naming), values string, int, float(contains decimals), double, boolean (True/False- have to start with Upper case) - These are Primitive data types
# string : remember how to concatenate, upper(), title(), lower(), str(), '\t', '\n'
# numbers: int, float/double, int(), +, -, *, /, **, //, %







