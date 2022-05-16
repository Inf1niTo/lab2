#num9
print("Введите слово для проверки на палиндром")
s = str(input())
a = len(s)
if a > 2:
    reversed_string = s[::-1]
    if s == reversed_string:
        print(s, "палиндром")
    else:
        print(s, "не палиндром")
else:
    print("Введите полную форму")