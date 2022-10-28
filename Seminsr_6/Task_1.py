from unittest import result


lst = ['3', '5', '6', '4', '9']


def summ(x):
    return x + 2


def func(x): return x + 2
func = lambda x: x + 2

res = map(int, lst)
print(res)
res2 = map(summ, res)
print(tuple(res2))


def more_five(x):
    if x > 5:
        return True


# res_map = map(more_five, res)
# print(list(res(res_map)))
res = filter(more_five, res)
print(list(res))