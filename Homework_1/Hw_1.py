# Write a program that accepts a digit indicating the day of the week 
# as input and checks whether this day is a weekend.

number = int(input("Enter the number of the day of the week: "))

def days(num):
    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    if num < 1 or num > 7:
        print('You entered an incorrect value!')
    elif num >= 6:
        print(f"{week[num-1]} It's a day off")
    else:
        print(f"{week[num-1]} It's a working day")

days(number)