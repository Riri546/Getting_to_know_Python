# 1. Write a program that removes from text all words containing "abc".

from cgitb import text

text_user = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'
print(f'Initial text: {text_user}')


def del_some_words(text_us):
    text_us = list(filter(lambda x: 'абв' not in x, text_us.split()))
    return " ".join(text_us)


text_u = del_some_words(text_user)
print(f"Corrected text: {text_u}")
