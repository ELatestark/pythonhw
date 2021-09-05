#!/usr/bin/env python3
def cod(n):
    if n == "":
        return ""
    else:
        a = str(n[0]) + str(cod(n[1:]))
        return int(a)

while 1:
    inp = str(input("Введите строку (введите 'cancel' для выхода): "))
    if inp == "cancel":
        print("Bye!")
        exit()
    elif inp.isdigit():
        num = cod(inp)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        print(num)
    else:
        print("Не удалось преобразовать введенный текст в число.")