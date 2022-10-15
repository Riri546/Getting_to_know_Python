# 1.Specify a list of several numbers. Write a program that will find the sum of the list items standing in an odd position.
# *Example:*
# - [2, 3, 5, 9, 3] -> on the odd positions of elements 3 and 9, the answer is: 12

filling = []

def filling_list(fil):
    length = int(input('Enter the length of the list: '))
    number = int(input(f'Enter {length} items in the list: '))
    
    for i in length:
        fil.append(number)
    print(filling)
    
filling_list(filling)
    


# def sum_num(fil):
#     count = 0
#     if fil % 2 != 0:
#         count += fil
#     print(f'Answer = {count}')


# sum_num(filling)

# number = int(input("Enter the number of the day of the week: "))

# # Checking the condition
# def days(num):
#     week = ['Monday', 'Tuesday', 'Wednesday',
#             'Thursday', 'Friday', 'Saturday', 'Sunday']
#     if num < 1 or num > 7:
#         print('You entered an incorrect value!')
#     elif num >= 6:
#         print(f"{week[num-1]} It's a day off")
#     else:
#         print(f"{week[num-1]} It's a working day")

# days(number)