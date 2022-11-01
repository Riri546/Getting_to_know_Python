import model as mod
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    operator = view.get_operation()
    mod.init(value_a, value_b)
    result = mod.do_it()
    view.view_data(result, 'result')
