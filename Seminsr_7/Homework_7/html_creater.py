# from user_interface import surname_view as sn
# from user_interface import name_view as n
# from user_interface import telephon_view as tel
# from user_interface import description_view as dasc

# def create():
#     style = 'style ="font-size:30px;"'
#     html = '<html>\n <head></head>\n <body>\n'
#     html += f'Surname: {style}, {sn()}\n'
#     html += f'Name: {style}, {n()}\n'
#     html += f'Telephon: {style}, {tel()}\n'
#     html += f'Description: {style}, {dasc()}\n'
#     html += '  </body>\n</html>'

#     with open('tel_index.html', 'w') as page:
#         page.write(html)
#     return html


# def create(device=1):
#     style = 'style ="font-size:22px;"'
#     html = '<html>\n <head></head>\n <body>\n'
#     html += '  <p {}>Temperature: {} c</p>\n'\
#         .format(style, temperature_view(device))
#     html += '  <p {}>Wind speed: {} m/c</p>\n'\
#         .format(style, wind_speed_view(device))
#     html += '  <p {}>Pressure: {} mmHg</p>\n'\
#         .format(style, preassure_view(device))
#     html += '  </body>\n</html>'

#     with open('index.html', 'w') as page:
#         page.write(html)
#     return html


# def new_create(data, device=1):
#     t, p, w = data
#     style = 'style ="font-size:22px;"'
#     html = '<html>\n <head></head>\n <body>\n'
#     html += '  <p {}>Temperature: {} c</p>\n'\
#         .format(style, t)
#     html += '  <p {}>Wind speed: {} m/c</p>\n'\
#         .format(style, w)
#     html += '  <p {}>Pressure: {} mmHg</p>\n'\
#         .format(style, p)
#     html += '  </body>\n</html>'

#     with open('new_index.html', 'w') as page:
#         page.write(html)
#     return data
