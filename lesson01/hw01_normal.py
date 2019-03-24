# coding: utf-8

import math

__author__ = 'Тимофеев Алексей'

print("Список задач:")
print("[1] - Задача-1")
print("[2] - Задача-2")
print("[3] - Задача-3")

task = int(input("Какую задачу будем решать? "))

if task == 1:
    # Задача-1
    number = int(input("Введите число: "))
    i = 10
    k = 0
    p = 0
    a = 0
    while number > 0:
        k = number%i 
        number = number - k
        p = int(10 * k / i)
        if p > a:
            a = p
        i = i * 10
    print(a)
elif task == 2:
    # Задача-2
    number1 = int(input("Введите 1 переменную: "))
    number2 = int(input("Введите 2 переменную: "))
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    '''number1, number2 = number2, number1'''
    print("Поменял переменные местами, теперь: переменная 1 - ", number1, ", a переменная 2 - ", number2)
elif task == 3:
    # Задача-3
    a = 0
    b = 0
    c = 0
    x1 = 0
    x2 = 0
    print("ax² + bx + c = 0")
    a = int(input("Введите коэф. a: "))
    b = int(input("Введите коэф. b: "))
    c = int(input("Введите коэф. c: "))
    if (b**2 - 4 * a * c) < 0:
        print("корней нет")
    elif (b**2 - 4 * a * c) == 0:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 / a
        print("Корень: ", x1)
    else:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 / a
        x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 / a
        print("Корни: ", x1, x2)
else:
    pass


