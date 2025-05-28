consumed = int(input("Enter the number of units consumed"))
if consumed < 50:
    print("The pre-unit tax will be 2.60 and the tax on that bill will be 25.")
    amount = consumed * 2.60 + 25
    print(amount)
elif consumed > 50 and consumed < 100:
    print("The pre unit tax = 3.25 and tax = 35")
    amount = consumed * 3.25 + 35
    print(amount)
elif consumed > 100 and consumed < 200:
    print("Pre unit tax = 5.26 and tax = 45")
    amount = consumed * 5.26 + 45
    print(amount)
else:
    print("Pre-unit tax = 8.45 and tax = 75")
    amount = consumed * 8.45 + 75
    print(amount)
