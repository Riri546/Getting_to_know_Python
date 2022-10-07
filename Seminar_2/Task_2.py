# 2.For a natural n, create a list consisting of elements of the sequence 3n + 1
# Example:
# - For n = 6: [4, 7, 10, 13, 16, 19]

n = int(input('Enter the natural number n: '))
result = []
for i in range(1, n +1):
    result.append(3*i+1)
print(result)
print(*result, sep=', ')


# result = ''
# sigh = 1

# for i in range(0, n+1):
#     result += str((3*i)+1)
#     result += ', '
# print(result[0:(len(result)-2)])
