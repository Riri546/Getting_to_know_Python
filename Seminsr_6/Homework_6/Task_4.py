# 2.Write the programmu, kotoraя atй production par chisel spiska.
# The sloganй schollement and the lastй э, the secondй and the prelastй and the ETC.D.
# * Example:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint


int_list = [randint (0,10) for i in range(11)]
print(int_list)


result_list = []


for i in range((len(int_list)+1)//2):
    result_list.append(int_list[i]*int_list[len(int_list)-1-i])
print(result_list)


# for element in input('Enter integers in the list separated by a space: ').split():
#     int_list.append(int(element))
# print(int_list)