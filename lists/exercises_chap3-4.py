#4.8 Cubes

cubes = []
for num in range(1, 11):
    print(num**3)
    cubes.append(num**3)
print(f"This is our new list: {cubes}")

print('-----------------')

#4-9 List comprehension - short form(specifically for appending and creating the list after looping)

cubes = [num**3 for num in range (1, 11)]
print(cubes)
print("========")

cubes = [num**3 for num in range(1, 11)]
print(cubes)
print(f"This is our new list: {cubes}")



