#NUM 4
import math
a = 1
x = 0
y = 0
s = 0
print("Введите первую координату Х")
x = int(input())
x1 = x
print("Введите первую координату Y")
y = int(input())
y1 = y
while a > 0:
    print("Введите следующую координату Х")
    x2 = int(input())
    print("Введите следующую координату Y")
    y2 = int(input())
    d = math.sqrt((x2-x)**2+(y2-y)**2)
    s += d
    x = x2
    y = y2
    print("Если желаете закончить - напишите 'Конец', иначе нажмите на Enter")
    b = str(input())
    if b == ('Конец'):
        break
    s = s + math.sqrt((x-x1)**2+(y-y1)**2)
print(s)