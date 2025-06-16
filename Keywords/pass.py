num = int(input("Enter a number"))
for i in range(num):
    if num%20 == 0:
        print("Twist")
    elif num%15 == 0:
        pass
    elif num%5 == 0:
        print("fizz")
    elif num%3 == 0:
        print("buzz")
    print(num)