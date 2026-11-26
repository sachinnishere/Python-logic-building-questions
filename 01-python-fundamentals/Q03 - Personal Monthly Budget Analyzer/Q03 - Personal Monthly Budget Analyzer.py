# collecting information:

print("Assumes income and expenses are greater than zero")

print()

name = input("Enter your name: ")
monthly_income = float(input("Enter your monthly income: "))
monthly_house_rent = float(input("Enter your house rent: "))
monthly_food_expenses = float(input("Enter your monthly food expenses: "))
monthly_transportation_expenses = float(input("Enter your monthly transportation expenses: "))
monthly_entertainment_expenses = float(input("Enter your monthly entertainment expenses: "))
monthly_shopping_expenses = float(input("Enter your monthly shopping expenses: "))
monthly_savings_target = float(input("Enter your monthly savings target: "))

# categorizing expenses in groups

total_housing_expense = monthly_house_rent
total_living_expenses = monthly_transportation_expenses + monthly_food_expenses
total_lifestyle_expenses = monthly_entertainment_expenses + monthly_shopping_expenses

# performing calculations

total_monthly_expenses = total_housing_expense + total_living_expenses + total_lifestyle_expenses
balance_after_expenses = monthly_income - total_monthly_expenses
balance_after_savings = balance_after_expenses - monthly_savings_target
income_spent_percentage = total_monthly_expenses / monthly_income * 100
money_saved_percentage = balance_after_expenses / monthly_income * 100

# checking if the total expenses exceeds the 70% of the monthly income

expense_limit_amount = monthly_income * 70 / 100

# logic checks

expenses_exceed_70_percent = total_monthly_expenses > expense_limit_amount
savings_target_achieved = balance_after_expenses >= monthly_savings_target
expenses_exceeds_income = monthly_income < total_monthly_expenses

# adding extras for detailed overview, checking how much percentage they take of total expenses

house_rent_percentage = monthly_house_rent / total_monthly_expenses * 100
food_expenses_percentage = monthly_food_expenses / total_monthly_expenses * 100
transportation_expenses_percentage = monthly_transportation_expenses / total_monthly_expenses * 100
entertainment_expenses_percentage = monthly_entertainment_expenses / total_monthly_expenses * 100
shopping_expenses_percentage = monthly_shopping_expenses / total_monthly_expenses * 100

# printing statements

print()

print("Name:", name)
print("Monthly income:", monthly_income)
print("Monthly house rent:", monthly_house_rent)
print("Monthly food expenses:", monthly_food_expenses)
print("Monthly transportation expenses:", monthly_transportation_expenses)
print("Monthly entertainment expenses:", monthly_entertainment_expenses)
print("Monthly shopping expenses:", monthly_shopping_expenses)
print("Monthly savings target:", monthly_savings_target)

print()

print("Total monthly expenses:", total_monthly_expenses)
print("Income spent percentage:", income_spent_percentage)
print("Remaining money after all expenses:", balance_after_expenses)
print("Money saved in percentage after all expenses:", money_saved_percentage)
print("Balance after expenses and savings:", balance_after_savings)

print()

print("Share of total monthly expenses (in percent):")

print()

print("House rent as percentage:", house_rent_percentage)
print("Food expenses as percentage:", food_expenses_percentage)
print("Transportation expenses as percentage:", transportation_expenses_percentage)
print("Entertainment expenses as percentage:", entertainment_expenses_percentage)
print("Shopping expenses as percentage of total monthly expenses:", shopping_expenses_percentage)

print()

print("Final logic checks")

print()

print("Expenses exceeds 70 percent of income:", expenses_exceed_70_percent)
print("Savings target achieved:", savings_target_achieved)
print("Expenses exceeds monthly income:", expenses_exceeds_income)