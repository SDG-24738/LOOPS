word = input("Enter a word")
character = input("Enter a character")
i = 0
count = 0
while i < len(word):
    if word[i] == character:
        count = count + 1
    i = i + 1
print("Total no.of times =", character, "has occured ", count, "times")    