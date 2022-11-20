# Chapter 7: user input in While loop:

name = 'john'
#while expression:
#    code to repeatedly execute with each iteration
#    code to repeatedly execute with each iteration
#    code to repeatedly execute with each iteration
#    code to repeatedly execute with each iteration

# be cautious of INFINITE loop
# to avoid make sure the condition is changing with each iteration

# current_number = 1
# while current_number <= 5:
#     print('current_number : ', current_number)
#     current_number += 1 # it means current_number = current_number += 1; increamEnting, adding +1 to each previous number, OTHERWISE the while loop will be INFINITE !! BE CAUTIOUS !!!
#
# print('------------   Fuzz Buzz example with while loop  #####################################')

# answer = ''    # this is called PLACE HOLDER
# # while (answer.lower() != 'n') and answer.lower() != 'no':
#     num = int(input('Please enter a number: '))
#     #num = 3
#     if num !=0:
#         if num % 3 == 0 and num % 5 == 0:
#             print('FuzzBuzz')
#         elif num % 3 == 0:
#             print('Fuzz')
#         elif num % 5 == 0:
#             print('Buzz')
#         else:
#             print('This is not dividable by 3 and 5')
#     else:
#         print('please enter a different number than 0')
#     answer = input("Do you want to continue? y/n: ")

print('-------- Akmals note copy-----------------------------')


def while_loop_increment():
    """
    Docstring - While loop when we are setting upper limit in the condition, we need to increment
    :return:
    """
    print("While loop when we are setting upper limit in the condition, we need to increment")
    current_number = 1
    while current_number <= 2:
        print('current number :', current_number)
        current_number = current_number + 1


def while_loop_decrement():
    """Docstring - "While" loop when we are setting bottom limit in the condition, we need to decrement
    :return:"""
    print("While loop when we are setting bottom limit in the condition, we need to decrement")
    current_number = 1
    while current_number > 0:
        print('current number :', current_number)
        current_number = current_number - 1


def fuzz_buzz():
    print("_______ Fuzz Buzz example with while loop ___________")
    answer = ''
    while (answer.lower() != 'n') and (answer.lower() != 'no'):
        # n == n -> True, n != n -> False , y != n -> True, '' != n -> True
        num = int(input('Please enter a number: '))
        # num = 3
        if num != 0:
            if num % 3 == 0 and num % 5 == 0:
                print('FuzzBuzz')
            elif num % 3 == 0:
                print('Fuzz')
            elif num % 5 == 0:
                print('Buzz')
            else:
                print('This is not dividable by 3 or 5')
        else:
            print("please enter different number than 0")
        answer = input("Do you want to continue? y/n: ")


# fuzz_buzz()
# while_loop_increment()
while_loop_decrement()

