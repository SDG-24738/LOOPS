try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    result = num1/num2
    print(result)
    print(result3)
except ValueError as ex:
    print(ex)
except ZeroDivisionError:
    print("Do not divide the number by 0")
except NameError as na:
    print(na)
finally:
    print("I am ouside the try block")