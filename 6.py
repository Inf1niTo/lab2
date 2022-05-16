#Num 6
z = 2
x = 3
c = 4
v = 4
b = 5
n = 6
p = 3
for i in range(1,8):
    p += 4/(z * x * c)
    print(p)
    p -= 4/(v * b * n)
    print(p)
    z += 4
    x += 4
    c += 4
    v += 4
    b += 4
    n += 4
