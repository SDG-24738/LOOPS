decimal = int(input("Enter a number"))
binary = ""
while decimal//2 != 0:
    x = decimal%2
    decimal = decimal//2
    binary = binary + str(x)
x = decimal%2
binary = binary + str(x)
binary = binary[::-1]
print(binary)