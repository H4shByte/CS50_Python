amount_due = 50
while amount_due > 0:
    print("Amount due: ", amount_due)
    coin = int(input("Insert coin: "))
    if coin in [25, 5, 10]:
        amount_due -= coin
change_owed = abs(amount_due)
print("change owed: ", change_owed)
