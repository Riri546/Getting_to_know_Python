# 7. Check the truth of the statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# for all predicate values.


input_x = int(input('Enter the number x: '))
input_y = int(input('Enter the number y: '))
input_z = int(input('Enter the number z: '))


def verification(x, y, z):
    if not (x or y or z) == (not (x) and not (y) and not (z)):
        print("The statement is true")
    else:
        print("The statement is incorrect")


verification(input_x, input_y, input_z)
