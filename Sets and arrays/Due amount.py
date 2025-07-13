def CalculateBalance(billAmount, amountPaid):
    balance = amountPaid - billAmount
    return balance
mybillAmount = float(input("Enter the bill amount"))
myamountPaid = float(input("Enter the amount paid"))
balance = CalculateBalance(mybillAmount, myamountPaid)
print(balance)