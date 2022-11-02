import data_provider as dp
import logger as log


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


# def temperature_view(sensor):
#     data = dp.get_temperature(sensor)
#     log.temperature_logger(data)
#     return data


# def preassure_view(sensor):
#     data = dp.get_preassure(sensor)
#     log.pressure_logger(data)
#     return data


# def wind_speed_view(sensor):
#     data = dp.get_wind_speed(sensor)
#     log.wind_speed_logger(data)
#     return data
