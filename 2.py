#NUM 2
a = 1
summa = 0
while a > 0:
    print("Введите начальную цену товара. Если вы хотите закончить - введите '0'")
    t = float(input())
    summa += t
    if t == 0:
        break
    else:
        p = t - (t * 0.6)
        print("Изначальная цена", t, '\n', "Цена по скидке", p)
s = summa - (summa * 0.6)
print("Сумма по изначальной цене", summa, '\n', "Сумма по скидке", s)
