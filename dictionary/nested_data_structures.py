# Nesting data structures:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

print(aliens)
print(aliens[1]) #printing the second element
print(aliens[1]['color']) #printing one element inside the second element
print(aliens[1]['points'])
print(f"alien 1 color is: {aliens[1]['color']} \n and points is:  {aliens[1]['points']}")

temp = aliens[1]
print(temp['color'])
print('---------------------------------------')
aliens_dictionary = {'alien_0' : {'color': 'green', 'points': 5},
           'alien_1' : {'color': 'yellow', 'points': 10},
           'alien_2' : {'color': 'red', 'points': 15}}
print(aliens_dictionary['alien_1']['color'])
print(aliens_dictionary['alien_1']['points'])
print(f"alien 1 color is: {aliens_dictionary['alien_1']['color']} \n and points is:  {aliens_dictionary['alien_1']['points']}")









