print("Welcome to the tip calculator")

price = float(input("What was the total bill? R "))

tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

tip = price * (tip_percent/100)

total_price = price+tip

total_price = round(total_price / people, 2)
total_price = "{:.2f}".format(total_price)
print(f"Each person should pay R{total_price}")
