# Chapter 3:
# Data structire - storage to hold multiple values, manage (create, add, update, remove)
# Python Data structures: Lists, Dictionary, (Set, Tuple)
# [4, 10, 6] ['john, 'mark', 'jane'] [Tru,. False, True] lists
#list is considered mutable object (we can change in the list)
#Tuple - immutable DS, can not add or remove values after difining



friends = []  # emplty list
players = list()  # creates empty list
nums = [4, 10, 6] # values index 0, 1, 2 accordingly... or -3, -2, -1 starting from the last element
names = ['john', 'mark', 'jane', 'daniel']
bool_values = [True, False, True]

#comand + option +l AUTOFORMAT the file

print(nums)
print(names)

# add elmenets, remove, update, read through values (access each value)
#indexes always start with 0, always the last element is -1 (negative) fromn the end
print(nums[1])
print(nums[2])
print(nums[0])
print(nums[-3])
print(nums[-2])
print(nums[-1])

print('Hi, ', names[1].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[0].title())
print('Hi, ', names[-2].title())
print('Hi, ', names[-3].title())

# listname.append(newvalue) - adds new value to the end of the list
names.append("alex")
print(names)
# listname.insert(index number, "value")
names.insert(0, "araz")
print(names)

# updating elements of the list, for existing index
names[-1] = 'benny' # this is updating the last elemebt of the list
print(names)

#removing values from the list 3 ways
#1 by index: del listname(index)
del names[3]
print(names)
#2 by value: listname.pop(index, by default it removes last value if not mentioned index)
names.pop()
print(names)
names.pop(0)
print(names)
deleted_name = names.pop(0) # returns the value to the program after deleting, del does not
print("We deleted following names: ", deleted_name.title())
#3 remove element value: listname.remove(value)
names.remove('mark')
print(names)


#### 10/16/2022
# Exercises:
#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.

guests = ['akmal', 'said', 'lenur']
print(guests)
print(guests[0].title(), 'I am inviting you to a party')
print('Hello, ' + guests[0].title() + ', I am inviting you to a party')
print(f'Hello,  {guests[0].title()} , I am inviting you to a party') # f makes it one whole string

# print('Hello, ' + guests[0].title() + ', I am inviting you to a party')
# print('Hello, ' + guests[0].title() + ', I am inviting you to a party')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

removed_guest = guests.pop(1)
print(guests)
print(removed_guest)
print(guests)
print(removed_guest.title(), ', can not make it to the party')
print(f'{removed_guest.title()}, can not make it to the party')

guests.append('max')

print(guests)

print(f'Hello,  {guests[0].title()} , I am inviting you to a party')
print(f'Hello,  {guests[1].title()} , I am inviting you to a party')
print(f'Hello,  {guests[2].title()} , I am inviting you to a party')


#H/W: 3-6, 3-7 pg46-pg47








