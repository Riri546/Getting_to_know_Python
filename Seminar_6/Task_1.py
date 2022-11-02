# from unittest import result


# lst = ['3', '5', '6', '4', '9']


# def summ(x):
#     return x + 2

# func = lambda x: x + 2

# res = map(int, lst)
# print(res)
# res2 = map(summ, res)
# print(tuple(res2))


# def more_five(x):
#     if x > 5:
#         return True


# # res_map = map(more_five, res)
# # print(list(res(res_map)))
# res = filter(more_five, res)
# print(list(res))

# # la = int(input())

# # f = lambda x: x - 2
# # print(f(la))

# --------------------------------------------------------------------
# lst = [1, 5, 6, 7, 2, 2, 1]

# for i, a in enumerate(lst):
#     print(f'{i = }, {a = }')

# for w in enumerate(lst):
#     print(w)
# --------------------------------------------------------------------
# def mystr():
#     return '555'


# def nest():
#     return [5, 3, 2, 6]


# my_dict = {
#     'a': "abc",
#     'b': "big",
#     'n': 'Sasha',
#     'age': 29,
#     mystr(): nest()
# }
# print(my_dict)
# --------------------------------------------------------------------
from pprint import pprint


my_dict = {
    'a': "abc",
    'b': "big",
    'n': 'Sasha',
    'age': 29,
    'sity': 'Yesk',
}
# print(my_dict)
pprint(my_dict)
print('Возрост: ', my_dict['age'])


my_dict['age'] = 30
print('Возрост: ', my_dict['age'])
# print('Есть машина: ', my_dict.get('is_car', False))
x = my_dict.setdefault('is_car', True)
print(x)

