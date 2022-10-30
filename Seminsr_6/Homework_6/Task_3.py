# 6. A number denoting the day of the week is given. Print its name and
# indicate whether it is a weekend.

number = int(input("Enter the name of the day of the week: "))


week = {'Monday': "It's a working day", 
        'Tuesday': "It's a working day", 
        'Wednesday': "It's a working day",
        'Thursday': "It's a working day", 
        'Friday': "It's a working day", 
        'Saturday':"It's a day off!", 
        'Sunday': "It's a day off!",
}

print(week())
# if number >= 6:
#     print(week.setdefault)
# else:
#     print(week.setdefault(2))
    
# for i in week.keys():
#     print(i, week[i])

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
