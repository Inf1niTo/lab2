#NUM 1
print("Введите все значения. Для завершения ввода введите '0' ")
a = int(input())
count = 0
c = 0
while a != 0:
    c = c + a
    count += 1
    print("Введите все значения. Для завершения ввода введите '0' ")
    a = int(input())
    if a == 0:
        break
print("Среднее значение =", c/count)