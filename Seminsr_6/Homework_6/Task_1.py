# 4. Show the first digit of the fractional part of the number.


num = float(input('Enter a fractional number: '))


# num = 5,77
round_num = int(num)  # 5
result = lambda x, y: (x - y) * 10
# result = (num - round_num)*10 #7.7


print(f'The first digit of the fractional part: {result(num, round_num)}')