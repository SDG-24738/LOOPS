def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * factorial(a - 1)
num = int(input("Enter a number"))
if num < 0:
    print("INVALID!")
else:
    print(factorial(num))