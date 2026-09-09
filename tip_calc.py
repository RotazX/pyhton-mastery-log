
bill, tip = input("What is the bill amount and tip percentage?" ).split()

tip_amount = float(bill) * (float(tip)/100)
total = float(bill) + tip_amount
print(f"Tip amount is {tip_amount:.2f} and total bill is {total:.2f}.")