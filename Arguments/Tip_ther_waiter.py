def total_calc(bill_amount, tip_perc):
    tip_amount = (tip_perc/100) * bill_amount
    total = bill_amount + tip_amount
    print("total_amount", total)
    print("bill_amount", bill_amount)
    print("tip_amount", tip_amount)
total_calc(1000, 5)