budget = int(input())
price = input()
counter = 0
while price != "End":
    current_price = int(price)
    counter += current_price
    if counter > budget:
        print("You went in overdraft!")
        exit()
    price = input()
print("You bought everything needed.")