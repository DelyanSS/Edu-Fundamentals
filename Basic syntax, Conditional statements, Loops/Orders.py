number_of_orders = int(input())
counter = 0

for i in range(number_of_orders):
    coffee_price = float(input())
    days = int(input())
    capsule_needed = int(input())
    if coffee_price > 100.00 or coffee_price < 0.01:
        continue
    elif days > 31 or days < 1:
        continue
    elif capsule_needed < 1 or capsule_needed > 2000:
        continue

    cofee_total = (capsule_needed * days) * coffee_price
    counter += cofee_total

    total_money = counter * cofee_total

    print(f"The price for the coffee is: ${cofee_total:.2f}")

print(f"Total: ${counter:.2f}")
