# coding: utf-8

__author__ = 'Тимофеев Алексей'

print("Список задач:")
print("[1] - Задача-1")
print("[2] - Задача-2")
print("[3] - Задача-3")

task = int(input("Какую задачу будем решать? "))

if task == 1:
    # Задача-1
    def my_round(number, ndigits):
        ndigits = int(ndigits)
        number = int(number*(10**ndigits))/(10**ndigits)
        return(number)
    print(my_round(2.1234567, 5))
    print(my_round(2.1999967, 5))
    print(my_round(2.9999967, 5))
elif task == 2:
    # Задача-2
    def lucky_ticket(ticket_number):
        if ticket_number < 10000:
            n1 = int(ticket_number/100)
        elif ticket_number < 100000:
            n1 = int(ticket_number/1000)
        elif ticket_number < 1000000:
            n1 = int(ticket_number/10000)  
        n1 = int(int((n1)/10) + n1%10) 
        n2 = int((ticket_number%100 - ticket_number%10)/10 + ticket_number%10)
        if n1 == n2:
            return ("Yes")
        else:
            return ("No")
    print(lucky_ticket(123006))
    print(lucky_ticket(12321))
    print(lucky_ticket(436751))