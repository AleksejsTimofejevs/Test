# coding: utf-8

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
    while number > 0:
        k = number%i
        number = number - k
        print(int(10 * k / i))
        i = i * 10
elif task == 2:
    # Задача-2
    number1 = input("Введите 1 переменную: ")
    number2 = input("Введите 2 переменную: ")
    number = number1
    number1 = number2
    number2 = number
    print("Поменял переменные местами, теперь: переменная 1 - ", number1, ", a переменная 2 - ", number2)
elif task == 3:
    # Задача-3
    age = int(input("Введите ваш возраст: "))
    if age >= 18:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")   
else:
    pass
