rows = int(input("Enter the number of rows"))
if rows%2 == 0:
    half = rows // 2
else:
    half = (rows // 2) + 1
space = half - 1
for i in range(1, half + 1):
    for _ in range(space):
        print(" ", end="")
    space -= 1
    num = 1
    for _ in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()
space - 1
for i in range(1, half):
    for _ in range(space):
        print(" ", end="")
    space += 1
    num = 1
    for _ in range(2 * (half - i) - 1):
        print(num, end="")
        num += 1
    print()