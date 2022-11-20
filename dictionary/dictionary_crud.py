# Chapter 6: Dictionary - data structure (key-value pair)
# CRUD (creat, read, update, delete)
# 1 creating empty dictionary (C-create in CRUD)
person1 = {}
person2 = dict() # empty dictionary

person1 = {'name': 'john doe',
           'age': 25,
           'location':'ny',
           'cars': ['audi', 'bmw', 'subaru', 'toyota']} # list as a value, not as a variable

# 2 accessing the values(R-read in CRUD)
print(f"getting name of person1: {person1['name']}")
print(f"getting age of person1: {person1['age']}")

# 3 adding/updating key value  pair to the dictionary (U-update in CRUD)
print('Original dictinary: ', person1)
person1['phone'] = '(929) 456-7891' #phone does not exist in keys, so it adds new key-value pair (element)
print('Updated with new key dictinary: ', person1)
# updatng the value og 'age' in the person1 dictionary.
person1['age'] = 30 # !!! pay attemtion you mentioning the existing key!!!
print('Updated age in person1 dictinary: ', person1)

# updating the list value va;ur inside the dictionary:
#cars[0] = 'mers'
person1['cars'][0] = 'mers'
print('Updated list(audi to mers) in person1 dictinary: ', person1)

print('------------------')
print('dictionary', person1['cars'][1].upper())
print('------------------')

languages_list = ['eng', 'ru', 'esp', 'marsian']
person1['languages'] = languages_list # adding existing list as a value to dictionary, *if we make a change in the original list, it will affect the list inside the dictionary, it creates the two-way reference to the list
print(person1)
print("updating the value of the list in the dictionary")
languages_list[3] = 'ger'
print('updated list: ', languages_list)
print('dictionary', person1)
print("updating the value of the list in the dictionary")
person1['languages'][2] = 'french'
print('updated list: ', languages_list)
print('dictionary', person1)

# 4 Delete key-value pair from Dictionary (D-Delete in CRUD)

print("Deleting the location key-value pair from person1....")
del person1['location']
print("Updated person1 Dictionary:", person1)

print('----------------')
#exercise: 6-2 Favourite numbers
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
#print eaxh persons name and their favorite number
print(f"Nicole's favourite number is : {fav_nums['nicole']}")
print(f"Alex's favourite number is : {fav_nums['alex']}")
print(f"Yulia's favourite number is : {fav_nums['yulia']}")

#H/W: 6-1, 6-3



















