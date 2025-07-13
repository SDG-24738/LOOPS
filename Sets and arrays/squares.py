def squares(starting, ending):
    myList = []
    for x in range(starting, ending):
        sq = x * x
        myList.append(sq)        
    return myList
starting = int(input("Enter the start value"))
ending = int(input("Enter the ending value"))
myList = squares(starting, ending)
oddList = []
evenList = []
for x in myList:
    if x%2 != 0:
        oddList.append(x)
    else:
        evenList.append(x)
print("Odd squares are", oddList)
print("Even squares are", evenList)