# coding: utf-8

import math

__author__ = 'Тимофеев Алексей'

print("Список задач:")
print("[1] - Задача-1")
print("[2] - Задача-2")
print("[3] - Задача-3")
print("[4] - Задача-4")

task = int(input("Какую задачу будем решать? "))

if task == 1:
    # Задача-1
    def fibonacci(n, m):
        a, b = 0, 1 
        fib1 = []
        for r in range(m):
            fib1.append(b)
            a, b = b, a+b
        fib2 = [fib1[i] for i in range(n-1, m-1)]
        print (fib2)
    fibonacci(3, 11)
elif task == 2:
    # Задача-2
    def sort_to_max(origin_list):
        list1 = []
        list2 = origin_list.copy()
        for r in origin_list:
            list1.append(min(list2))
            list2.pop(list2.index(min(list2)))
        print(list1)
    sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
elif task == 3:
    # Задача-3
    def filter1(function1, itr):
        new_itr = [elem for elem in itr if function1(elem)]
        if type(itr) is tuple:
            new_itr = tuple(new_itr)
        if type(itr) is set:
            new_itr = set(new_itr)
        if type(itr) is str:
            new_itr = ''.join(new_itr)
        print(new_itr)
    filter1(lambda x: x < 0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0])
elif task == 4:
    # Задача-4:
    # Четырехугольник является параллелограммом, если: Противоположные стороны попарно равны.
    
    def parallel(a1, a2, b1, b2, c1, c2, d1, d2):
        a = [a1, a2]
        b = [b1, b2]
        c = [c1, c2]
        d = [d1, d2]
        #Проверка на четырехугольник
        if a == b or a == c or a == d or b == c or b == d or c == d:
            print("Вершины не образуют параллелограмм!")
        else:
            #Определяем длинну сторон
            ab = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
            cd = math.sqrt((c[0] - d[0])**2 + (c[1] - d[1])**2)
            ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
            ac = math.sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)
            bd = math.sqrt((b[0] - d[0])**2 + (b[1] - d[1])**2)

            #Определяем какие стороны являются противоволожными и проверяем равность противоположных сторон
            dlinna1 = [ab, ac, ad]

            if max(dlinna1) == ac:
                if ab == cd and ad == cb:
                    print("Это параллелограмм!")
                else:
                    print("Вершины не образуют параллелограмм!")
            elif max(dlinna1) == ab:
                if ac == bd and cb == ad:
                    print("Это параллелограмм!")
                else:
                    print("Вершины не образуют параллелограмм!")
            elif max(dlinna1) == ad:
                if ac == bd and cd == ab:
                    print("Это параллелограмм!")
                else:
                    print("Вершины не образуют параллелограмм!")
    
    parallel(0, 0, 1, 3, 4, 3, 3, 0)