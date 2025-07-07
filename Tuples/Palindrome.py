def palindrome(r):
    start = 0
    end = len(r) - 1
    while start < end:
        if r[start] != r[end]:
            return False
        start += 1
        end -= 1
    return True
r = (1, 2, 3, 3, 2, 1)
if palindrome(r):
    print("The tuple is a palindrome because it is same from front to back")
else:
    print("It is not a palindrome")