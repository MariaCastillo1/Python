
print("Welcome to the tip calculator.")
amount = input("What was your total bill? $")
amount_int = int(amount)

tip = input("What percentage of tip would you like to give, 10, 12, 15? ")
tip_int = int(tip)

everyone = input("How many people splitting the bill? ")
everyone_int = int(everyone)

cal_tip = (tip_int / 100) * amount_int
result = (amount_int + cal_tip) / everyone_int
result_round = round(result, 2)

print(f"Each person should pay ${result_round}")




