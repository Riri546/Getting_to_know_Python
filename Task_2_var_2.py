# 2. Find the maximum of five numbers.

a = [5, 66, 33, 54, 11]


def find_max_value(list):
    index = 0
    max_index = len(list)-1
    max = list[0]
    while index <= max_index:
        if list[index] > max:
            max = list[index]
        index += 1
    return max


print('Answer: ', find_max_value(a))
