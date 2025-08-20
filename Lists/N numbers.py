count = int(input("How many numbers do you want to enter?"))
total = 0
for x in range(count):
    num = float(input("Enter a number"))
    total = total + num
if count > 0:
    average = total/count
    print("The average is ", average)
else:
    print("There is no average")