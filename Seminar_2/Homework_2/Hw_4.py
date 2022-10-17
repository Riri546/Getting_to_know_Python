# 4.Specify a list of N elements filled with numbers from the interval [-N, N].
# Find the product of the elements at the specified positions. The positions are stored
# in a file file.txt there is one number in one line.

n_neg = int(input('Enter a negative number: '))
n_pos = int(input('Enter a positive number: '))
position_1 = int(input('Enter the index of the first number: '))
position_2 = int(input('Enter the index of the second number: '))

list_num = [i for i in range(n_neg, n_pos+1)]
print(list_num)


def mult_number(l, pos_1, pos_2):
    mult = 1
    for i in range(len(l)):
            if i in (pos_1, pos_2):
                mult *= l[i]
    print(f'The product of the numbers standing by the index {pos_1} and {pos_2} = {mult}')

mult_number(list_num, position_1, position_2)


# def sum_number(l, pos_1, pos_2):
#     count = 0
#     for i in l:
#         if i == pos_1:
#             count *= l[i]
#         if i == pos_2:
#             count *= l[i]
#     print(f'The sum of the numbers standing by the index {position_1} and {position_2} = {count}')


# sum_number(list_num, position_1, position_2)
