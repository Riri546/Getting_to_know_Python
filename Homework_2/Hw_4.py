# 4.Specify a list of N elements filled with numbers from the interval [-N, N].
# Find the product of the elements at the specified positions. The positions are stored
# in a file file.txt there is one number in one line.

n_neg = int(input('Enter a negative number: '))
n_pos = int(input('Enter a positive number: '))

list = [i for i in range(n_neg, n_pos+1)]
print(list)
print('Sum of numbers:', sum(list))