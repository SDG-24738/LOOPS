rows = int(input("Enter the number of rows"))
number = 1
for x in range(1, rows + 1):
    for y in range (1, x + 1):
        print(number, end = ' ')
        number = number + 1
    print()