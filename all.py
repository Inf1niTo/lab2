# NUM 1
# print("Введите все значения. Для завершения ввода введите '0' ")
# a = int(input())
# count = 0
# c = 0
# while a != 0:
#     c = c + a
#     count += 1
#     print("Введите все значения. Для завершения ввода введите '0' ")
#     a = int(input())
#     if a == 0:
#         break# print("Среднее значение =", c/count)
#NUM 2
# a = 1
# summa = 0
# while a > 0:
#     print("Введите начальную цену товара. Если вы хотите закончить - введите '0'")
#     t = float(input())
#     summa += t
#     if t == 0:
#         break
#     else:
#         p = t - (t * 0.6)
#         print("Изначальная цена", t, '\n', "Цена по скидке", p)
# s = summa - (summa * 0.6)
# print("Сумма по изначальной цене", summa, '\n', "Сумма по скидке", s)
#NUM 3
# for i in range(1,101):
#     if i % 10 == 0:
#         print("Градусы по Цельсию:", i, "Градусы по Фаренгейту:", i * 1.8 + 32)
#NUM 4
# import math
# a = 1
# x = 0
# y = 0
# s = 0
# print("Введите первую координату Х")
# x = int(input())
# x1 = x
# print("Введите первую координату Y")
# y = int(input())
# y1 = y
# while a > 0:
#     print("Введите следующую координату Х")
#     x2 = int(input())
#     print("Введите следующую координату Y")
#     y2 = int(input())
#     d = math.sqrt((x2-x)**2+(y2-y)**2)
#     s += d
#     x = x2
#     y = y2
#     print("Если желаете закончить - напишите 'Конец', иначе нажмите на Enter")
#     b = str(input())
#     if b == ('Конец'):
#         break
#     s = s + math.sqrt((x-x1)**2+(y-y1)**2)
# print(s)
#Num 5
# print("Вводите группы из 8 битов")
# while 1>0:
#     a = str(input())
#     s1 = 0
#     s0 = 0
#     b = len(a)
#     if b != 8:
#       print("Вы ввели группу не из 8 битов")
#     else:
#         s1 = a.count('1')
#         s0 = a.count('0')
#         if s1 % 2 == 0:
#             print("Бит четности должен равняться 0")
#         else:
#             print("Бит четности должен равняться 1")
#     print("Если вы хотите закончить, нажмите Enter, если нет, введите любой символ")
#     k = input()
#     if k == (''):
#         break

#Num 6
# z = 2
# x = 3
# c = 4
# v = 4
# b = 5
# n = 6
# p = 3
# for i in range(1,8):
#     p += 4/(z * x * c)
#     print(p)
#     p -= 4/(v * b * n)
#     print(p)
#     z += 4
#     x += 4
#     c += 4
#     v += 4
#     b += 4
#     n += 4

#Num7
# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# smeshenie = 3
# message = input("Сообщение для ДЕшифровки: ").upper()
# itog = ''
# lang = input('Выберите язык RU/EU: ')
# if lang == 'RU':
#     for i in message:
#         mesto = alfavit_RU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# else:
#     for i in message:
#         mesto = alfavit_EU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_EU:
#             itog += alfavit_EU[new_mesto]
#         else:
#             itog += i
# print (itog)

#NUM8

# print("Введите число х")
# x = int(input())
# guess = x/2
# while guess * guess - x > 10**(-12):
#     guess = guess/2
#     if guess * guess - x < 10**(-12):
#         guess = (guess + x / guess)/2
# print(guess)

#num9
# print("Введите слово для проверки на палиндром")
# s = str(input())
# a = len(s)
# if a > 2:
#     reversed_string = s[::-1]
#     if s == reversed_string:
#         print(s, "палиндром")
#     else:
#         print(s, "не палиндром")
# else:
#     print("Введите полную форму")