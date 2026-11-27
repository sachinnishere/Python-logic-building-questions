# collecting information

name = input("enter your name: ")
age = int(input("enter your age: "))
current_weight = float(input("enter your current body weight: "))
target_weight = float(input("enter your targeted weight: "))
monthly_gym_fee = float(input("enter your monthly gym membership fee: "))
monthly_diet_expenses = float(input("enter your monthly diet expenses: "))
monthly_supplement_expenses = float(input("enter your monthly supplement expenses: "))
completed_workout_days = int(input("workout days completed this month: "))
planned_workout_days = int(input("workout days planned this month: "))
average_workout_duration = float(input("enter your average workout duration per day (minutes): "))
daily_calorie_intake = float(input("enter your daily calorie intake: "))
daily_calorie_target = float(input("enter your daily calorie target: "))

# performing calculations 

total_fitness_expenses = monthly_gym_fee + monthly_diet_expenses + monthly_supplement_expenses
workout_day_shortfall = completed_workout_days - planned_workout_days
workout_completion_percentage = completed_workout_days / planned_workout_days * 100
total_workout_hours = average_workout_duration * completed_workout_days / 60

# assumes completed workout days is greater than zero

fitness_expense_per_workout_day = total_fitness_expenses / completed_workout_days

# positive means weight must be gained, negative means weight must be lost

weight_difference = target_weight - current_weight
calorie_difference = daily_calorie_intake - daily_calorie_target

# logical checks

workout_completion_achieved = workout_completion_percentage >= 80
all_planned_workout_days_completed = completed_workout_days >= planned_workout_days
monthly_expenses_exceeds_5000 = total_fitness_expenses > 5000

# requires an exact match; going beyond the target also returns False

target_weight_achieved = current_weight == target_weight

# printing results

print()

print("Personal Information")

print()

print("name:", name)
print("age:", age)
print("current weight:", current_weight)

print()

print("Fitness Goals")

print()

print("target weight:", target_weight)
print("Weight change needed (- lose, + gain):", weight_difference)

print()

print("Monthly Expenses")

print()

print("monthly gym fee:", monthly_gym_fee)
print("monthly diet expense:", monthly_diet_expenses)
print("monthly supplement expenses:", monthly_supplement_expenses)
print("total fitness expenses:", total_fitness_expenses)
print("average fitness expenses per workout day:", fitness_expense_per_workout_day)

print()

print("Workout Statistics")

print()

print("completed workout days:", completed_workout_days)
print("planned workout days:", planned_workout_days)
print("average workout duration in minutes:", average_workout_duration)
print("workout day shortfall:", workout_day_shortfall)
print("workout completion percentage of target days:", workout_completion_percentage)
print("total workout hours:", total_workout_hours)

print()

print("Calorie Intake")

print()

print("daily calorie intake:", daily_calorie_intake)
print("daily calorie target:", daily_calorie_target)
print("calorie difference:", calorie_difference)

print()

print("Logical Checks")

print()

print("Workout completion is at least 80%:", workout_completion_achieved)
print("planned workout days completed:", all_planned_workout_days_completed)
print("monthly expenses exceed 5000:", monthly_expenses_exceeds_5000)
print("target weight achieved:", target_weight_achieved)