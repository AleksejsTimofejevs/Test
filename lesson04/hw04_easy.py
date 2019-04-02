# coding: utf-8

__author__ = 'Тимофеев Алексей'

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst1 = [1, 2, 4, 0]
squarelst1 = [el**2 for el in lst1]
print(squarelst1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['Apple', 'Banana', 'Grapefruit']
fruits2 = ['Grapes', 'Kiwifruit', 'Banana', 'Lemon', 'Apple']

fruitsinboth = [el for el in fruits1 if el in fruits2]
print(fruitsinboth)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

randomlist = [random.randint(-100, 100) for _ in range(10)]
print(randomlist)
newlist = [el for el in randomlist if el%3 == 0 and el >= 0 and el%4 != 0]
print(newlist)