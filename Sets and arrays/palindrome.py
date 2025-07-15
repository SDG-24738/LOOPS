num = int(input("Enter a number"))
if str(num) == str(num)[::-1]:
    print("This number", num, "is a palindrome number")
else:
    print("It is not a palindrome number")
