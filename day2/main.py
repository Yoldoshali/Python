print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_per = int(input("What percentage tip would you like to give?"))
total_people = int(input("How many people to split the bill? "))
money_per_person = (bill + (bill * tip_per)/100) / total_people
print(f"Each person should pay: ${round(money_per_person, 2)}")
