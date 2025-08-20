List = [12, 5, 9, 34, 2, 89, 3]
length = len(List)
min = 99999
max = 0
for x in range(1, length):
    if List[x] > max:
        max = List[x]
    if List[x] < min:
        min = List[x]
print(max)
print(min)