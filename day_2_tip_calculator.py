"""Day 2 - Tip Calculator"""

#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the Tip Calculator!")
billAmount = float(input("What is your bill total?\n"))
peopleAmount = int(input("How many people is the bill being split between?\n"))
tipAmount = float(input("How much would you like to tip?\n"))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
splitAmount = (billAmount / peopleAmount) * (1 + tipAmount/100)

roundedAmount = round(splitAmount, 2)

#Format the result to 2 decimal places = 33.60

print(f"Each person should pay: ${roundedAmount}")
