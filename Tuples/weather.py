weather = (1, 0, 0, 0, 1, 1, 0)
sun = 0
rain = 0
for x in range(0, 7):
    if(weather[x] == 0):
        rain += 1
    else:
        sun += 1
if (sun>rain):
    print("It is very sunny today")
else:
    print("It is very rainy today")