money=0
amount_due=50
while money < 50:
    print("Amount Due:",amount_due)
    add_money=int(input("Insert coin: "))
    if add_money == 25:
        money=add_money+money
        amount_due=amount_due-add_money
    elif add_money == 10:
        money=add_money+money
        amount_due=amount_due-add_money
    elif add_money == 5:
        money=add_money+money
        amount_due=amount_due-add_money
    else:
        print("integer isn’t an accepted denomination")
print("Change Owed:",money-50)
