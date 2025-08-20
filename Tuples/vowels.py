word = input("Enter a word")
count = 0
length = len(word)
for x in range(1, length):
    if word[x] == "a":
        count = count + 1
    if word[x] == "e":
        count = count + 1
    if word[x] == "i":
        count = count + 1
    if word[x] == "o":
        count = count + 1
    if word[x] == "u":
        count = count + 1
print(count)