# 3. Display the numbers from -N to N.

print('Enter a negative number a: ')
a = int(input())
print('Enter the number b: ')
b = int(input())

print('Answer: ')

for num in range(a, b):
    if num == b + 1:
        continue
    print(num+1)
