#NUM8

print("Введите число х")
x = int(input())
guess = x/2
while guess * guess - x > 10**(-12):
    guess = guess/2
    if guess * guess - x < 10**(-12):
        guess = (guess + x / guess)/2
print(guess)
