apple = 0.45
banana = 0.371
cherry = 0.094

amt_apples = int(input("How many apples would you like? "))
print(f"=> {amt_apples} cost {apple*amt_apples:.2f}.")
amt_bananas = int(input("How many bananas would you like? "))
print(f"=> {amt_bananas} cost {banana*amt_bananas:.2f}.")
amt_cherries = int(input("How many cherries would you like? "))
print(f"=> {amt_cherries} cost {cherry*amt_cherries:.2f}.")

price = apple*amt_apples+banana*amt_bananas+cherry*amt_cherries

discount = int(input("You're a loyal customer, I shall give you a deal. How much % discount would you like? "))
calc_disc = price*(discount/100)
disc_price = price-calc_disc

print(f"[TOTAL] ${price:.2f}")
print(f"[DISCOUNT %] {discount}%")

print(f"=> With a discount of {calc_disc:.2f}, you owe me {disc_price:.2f}")

payment = float(input("How much can you pay? $"))
change = payment-disc_price
print(f"Here is your change: {change:.2f}")
