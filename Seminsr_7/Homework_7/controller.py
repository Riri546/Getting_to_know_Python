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
