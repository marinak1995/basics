# Chapter 3: Organizing lists

cars = ['tesla', 'bmw', 'moskvich', 'lexus']
print("Permanent sorting: - sort(). ")
print("list before sorting: ", cars)
cars.sort() #sorts a-z, asc order
print("list after sorting: ", cars)

names = ['john', 'jane', 'mark']
print("list before sorting: ", names)
names.sort(reverse=True) #sorts z-a, desc order
print("list after sorting: ", names)

# 'sort' affects/changes the original list

print("Sorting temporarily - sorted() ")
car_models = ['model x', '550 xi', 'corolla', 'camry']
print("Car models before sorting: ", car_models)

sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True) #reverse is an option in this case

print("sorted Car models after sorting in asc order: ", sorted_car_models_asc)
print("sorted Car models after sorting in desc order: ", sorted_car_models_desc)

#sorted() does not affect the original list

nums = [6, 3, 9, 7, 10]
print("List before sorting: ", nums)
nums.reverse() # reverse is the function in this case , it affects the original list
print("List after reversing: ", nums)

#example
#unsorted number 10mln nums = [.....]
#print largest and smallest value
#nums.sort()
#print('smallest number: ', nums[0])
#print('largest number: ', nums[-1])

print("#number of elements in the list with len() functions")
print('number of elements in the nums list: ', len(nums))
print('number of elements in the names list: ', len(names))
print('number of elements in the cars list: ', len(cars))

# !!!!!!!!! H/W 3-8, 3-9, 3-10















