#4 Slicing list
pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'fughi', 'sicilian']

print(pizzas[0:3])
for pizza in pizzas[0:3]: #includes index 0, 1, 2
    print(f'we have {pizza} pizza today')

for pizza in pizzas[3:]: #includes 3rd index to the last
    print(f'we have {pizza} pizza today')

 #copy the list:

new_pizzas = pizzas #creates the new reference list to the same list (one list, two names), it refers to one list
copy_pizzas = pizzas[:] #creates the totally independent list(copy_pizza)
print(f'Lists before updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}')
pizzas.append('cheese steak')
new_pizzas.append('mushroom')
copy_pizzas.append('veggie')
copy_pizzas.append('drandma')
print(f'Lists after updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}')


# H/W: 4-10, 4-11, 4-12
# STYLING THE CODE: ctrl + alt + l











