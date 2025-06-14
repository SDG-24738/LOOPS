def cube(a):
    return a ** 3
def check_cube(a):
    if a%3 == 0:
        result = cube(a)
        print("Number", a, "is divisible by 3")
        print("The cube of", a, "is", cube(a))
    else:
        print("It is not divisible")
check_cube(9)