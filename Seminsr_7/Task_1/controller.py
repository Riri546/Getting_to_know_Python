from pyexpat import model
import model as mod
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    operator = view.get_operation()
    if operator == '+':
        result = mod.sum_num(value_a, value_b)
    elif operator == '-':
        result = mod.sub_num(value_a, value_b)
    elif operator == '/':
        result = mod.div_num(value_a, value_b)
    elif operator == '*':
        result = mod.mult_num(value_a, value_b)
    
    view.view_data(f'{value_a} {operator} {value_b} ', result)
