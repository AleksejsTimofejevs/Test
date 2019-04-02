# coding: utf-8

__author__ = 'Тимофеев Алексей'

import re
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = ('mtMmEZUOmcq')
pattern1 = '[a-z]+'
line1 = re.findall(pattern1, line)
print(line1)

# Задание-2. GeekBrains:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line = ('GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec')
pattern2 = '[a-z]{2}([A-Z]+)[A-Z]{2}'
line2 = re.findall(pattern2, line)
print(line2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

n = (random.randint(0, 9) for i in range(2500))
str = ''.join(str(i) for i in n)

file1 = input("Введите имя файла (Например, text.txt): ")
f = open(file1, 'w', encoding='utf-8')
f.write(str)
f.close