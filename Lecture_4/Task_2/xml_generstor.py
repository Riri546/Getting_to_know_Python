from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import preassure_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '  <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '  <wind speed view units= "m/s">{}</wind speed view>\n'\
        .format(wind_speed_view(device))
    xml += '  <pressure units = "mmHg">{}</pressure >\n'\
        .format(preassure_view(device))
    html += '  </xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
    return xml
