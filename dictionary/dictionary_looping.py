# Chapter 6: Looping through a dictionary
# Dictionary keys, value, key-value
person1 = {'name': 'john doe','age': 25,'location':'ny'}

#default case, looping throgh keys only
for k in person1:
    print(k)


print('#   looping throgh keys only --------------------')
for x in person1.keys():
    print(x)

print('#   looping throgh key and key value only-------------------')
for key in person1.keys():
    print('Key in this iteration is: ', key)
    print('value in this iteration is: ', person1[key])

#accessing value
print('#   looping throgh values only--------------------------')
for value in person1.values():
    print(value)
print('---------------------')

for value in person1.values():
    print(value)
print('--------------------')

# accessing keys and values
print('#   looping throgh keys and values -------------------')
for key, value in person1.items():
    print('Key in this iteration is: ', key)
    print('value in this iteration is: ', value)
print('------------------------')
print('########################')
# Exercise 6-5
#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#   • Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#   • Use a loop to print the name of each river included in the dictionary.
#   • Use a loop to print the name of each country included in the dictionary.

rivers_countries = {'nile': 'egypt',
                    'amazon': 'brazil',
                    'volga': 'russia',
                    'mississippi': 'usa',
                    'thames': 'uk' }
print("# 1. Use a loop to print a sentence about each river, such as The Nile runs through Egypt.#######################################")

for river, country in rivers_countries.items():
    print(f"The {river.title()} runs throgh {country.title()} ")

print('# 2. Use a loop to print the name of each river included in the dictionary. ########################')

for river in rivers_countries.keys():
    print(f"river: {river.title()} ")

print("# 3. Use a loop to print the name of each country included in the dictionary. ##########################")

for country in rivers_countries.values():
    print(f"Country: {country.title()} ")

# H/W: 6-4, 6-5
