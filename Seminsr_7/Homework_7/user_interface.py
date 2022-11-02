import data_provider as dp
import logger as log
from importlib import import_module

def surname_view(fam):
    data = dp.surname_use(fam)
    log.surname_logger(data)
    return data


def name_view(name):
    data = dp.name_use(name)
    log.name_logger(data)
    return data


def telephon_view(tel):
    data = dp.telephon_use(tel)
    log.telephon_logger(data)
    return data


def description_view(desc):
    data = dp.description_use(desc)
    log.description_logger(data)
    return data

