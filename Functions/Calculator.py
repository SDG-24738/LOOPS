def add(P , Q):
    return P + Q
def subtract(P , Q):
    return P - Q
def multiply(P , Q):
    return P * Q
def divide(P , Q):
    return(P / Q)
print("Seclect one of the given operations")
print("a - add.")
print("b - subtract.")
print("c - multiply")
print("d - divide.")
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
choice = input("Enter your choice")
if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("This is an invalid input")