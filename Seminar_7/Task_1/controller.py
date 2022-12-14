from pyexpat import model
import model as mod
import view
import logger as log


def button_click():
    value_a = view.get_value(1)
    value_b = view.get_value(2)
    operator = view.get_operation()
    if operator == '+':
        result = mod.sum_num(value_a, value_b)
    elif operator == '-':
        result = mod.sub_num(value_a, value_b)
    elif operator == '/':
        result = mod.div_num(value_a, value_b)
    elif operator == '*':
        result = mod.mult_num(value_a, value_b)
    op = f'{value_a} {operator} {value_b}'
    view.view_data(op, result)
    log.operation_logger(op, result)
