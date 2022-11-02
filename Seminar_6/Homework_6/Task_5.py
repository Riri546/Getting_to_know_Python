# 2 The string is given:
#'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
# It is necessary to get a dictionary in which the keys are words, the values are the number of words in
# a line:
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}


word = 'дом', 'окно', 'дверь', 'стена', 'кухня', 'стол', 'стул', 'дверь', 'дом', 'стул', 'стол', 'окно', 'стул'
d = dict()


for i in set(word):
    d[i] = word.count(i)
for i in d:
    print(i + ':', d[i])
