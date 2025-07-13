try:
    age = int(input("Enter the age"))
    if (age%2 == 0):
        print("The age is even")
    else:
        print("Age is odd")
except ValueError:
    print("Age is not valid")