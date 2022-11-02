import pprint

# Пример того, как нужно описывать функцию

# Функция суммирует жва числа
def summ(x: int, y: int) -> float:
    """
    Functional get ywo integer numbers and return sum 
    :param x: int
    :param y: int
    :return: float
    """
    return float(x + y)


summ(5, 2)
lst = [2, 3, 5]
sum(lst)
# lst2 = ['2', 5, [3, 2]]
# sum(lst2)
