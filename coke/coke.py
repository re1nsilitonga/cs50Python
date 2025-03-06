amount = 50
while amount > 0:
    print(f'Amount Due: {amount}')
    ins = int(input("Insert Coin: "))
    match ins:
        case 5 | 10 | 25:
            amount -= ins
        case _:
            amount == amount
amount = abs(amount)
print(f'Change Owed: {amount}')
