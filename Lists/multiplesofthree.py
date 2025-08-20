#Print all multiples of 3 between 1 and 100.
#Bonus: Count how many multiples were found.
count = 0
for x in range(1, 100):
    if x%3 == 0:
        print(x)
        count = count + 1
print(count, "= count")