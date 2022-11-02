from importlib import import_module
import data_provider as dp
import logger as log

def surname_view():
    data = dp.surname_use()


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
