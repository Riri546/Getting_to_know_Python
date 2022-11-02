import logger as log
import data_provider as dp


def button_click():
    surname = dp.surname_use()
    name = dp.name_use()
    tel = dp.telephon_use()
    dasc = dp.description_use()
    log.surname_logger(surname)
    log.name_logger(name)
    log.telephon_logger(tel)
    log.description_logger(dasc)

    # value_a = view.get_value(1)
    # value_b = view.get_value(2)
    # operator = view.get_operation()
    # if operator == '+':
    #     result = mod.sum_num(value_a, value_b)
    # elif operator == '-':
    #     result = mod.sub_num(value_a, value_b)
    # elif operator == '/':
    #     result = mod.div_num(value_a, value_b)
    # elif operator == '*':
    #     result = mod.mult_num(value_a, value_b)
    # op = f'{value_a} {operator} {value_b}'
    # view.view_data(op, result)
    # log.operation_logger(op, result)
