# Q04 – Gym Membership & Fitness Progress Analyzer

## Project Overview

The Gym Membership & Fitness Progress Analyzer is a Python program that helps users analyze their fitness expenses, workout performance, weight goals, and daily calorie intake.

The program collects personal fitness information and performs different calculations to generate a structured fitness report.

## Features

- Collects personal information such as name and age.
- Collects current weight and target weight.
- Calculates total monthly fitness expenses.
- Calculates workout day shortfall.
- Calculates workout completion percentage.
- Calculates total workout hours.
- Calculates average fitness expenses per completed workout day.
- Calculates the weight difference between current and target weight.
- Calculates the difference between daily calorie intake and calorie target.
- Checks whether workout completion is at least 80%.
- Checks whether all planned workout days have been completed.
- Checks whether monthly fitness expenses exceed ₹5,000.
- Checks whether the target weight has been achieved.

## Concepts Used

This project uses the following Python concepts:

- Variables and data types
- `input()` and `print()`
- Type conversion using `int()` and `float()`
- Arithmetic operators
- Relational operators
- Boolean expressions
- Percentage calculations
- Variable grouping and calculations
- Structured output using print statements

**Note:** This project does not use `if/else`, loops, functions, lists, or dictionaries.

## Sample Input

| Input | Value |
|---|---:|
| Name | Rahul |
| Age | 28 |
| Current Weight | 78 kg |
| Target Weight | 70 kg |
| Monthly Gym Fee | ₹1,000 |
| Monthly Diet Expenses | ₹2,000 |
| Monthly Supplement Expenses | ₹1,500 |
| Completed Workout Days | 22 |
| Planned Workout Days | 24 |
| Average Workout Duration | 120 minutes |
| Daily Calorie Intake | 2,500 kcal |
| Daily Calorie Target | 2,000 kcal |

## Sample Output

```text
Personal Information

name: Rahul
age: 28
current weight: 78.0

Fitness Goals

target weight: 70.0
Weight change needed (- lose, + gain): -8.0

Monthly Expenses

monthly gym fee: 1000.0
monthly diet expense: 2000.0
monthly supplement expenses: 1500.0
total fitness expenses: 4500.0
average fitness expenses per workout day: 204.54545454545453

Workout Statistics

completed workout days: 22
planned workout days: 24
average workout duration in minutes: 120.0
workout day shortfall: -2
workout completion percentage of target days: 91.66666666666666
total workout hours: 44.0

Calorie Intake

daily calorie intake: 2500.0
daily calorie target: 2000.0
calorie difference: 500.0

Logical Checks

Workout completion is at least 80%: True
planned workout days completed: False
monthly expenses exceed 5000: False
target weight achieved: False
```

## Calculations Explained

### 1. Total Fitness Expenses

Adds the monthly gym fee, diet expenses, and supplement expenses.

₹1,000 + ₹2,000 + ₹1,500 = ₹4,500

### 2. Workout Day Shortfall

Calculates the difference between completed workout days and planned workout days.

22 - 24 = -2 days

A negative result means the user is behind the planned workout target.

### 3. Workout Completion Percentage

(Completed Workout Days / Planned Workout Days) × 100

(22 / 24) × 100 = 91.67%

### 4. Total Workout Hours

Converts the total workout duration from minutes into hours.

(120 × 22) / 60 = 44 hours

### 5. Fitness Expense Per Workout Day

Divides total monthly fitness expenses by completed workout days.

₹4,500 / 22 = ₹204.55

### 6. Weight Difference

Subtracts current weight from target weight.

70 - 78 = -8 kg

- Negative result means weight must be lost.
- Positive result means weight must be gained.
- Zero means the target weight has been reached.

### 7. Calorie Difference

Subtracts the daily calorie target from actual daily calorie intake.

2,500 - 2,000 = 500 kcal

- Positive result means calorie intake is above the target.
- Negative result means calorie intake is below the target.
- Zero means actual intake matches the target.

## Logical Checks

| Condition | Result | Explanation |
|---|---|---|
| Workout completion is at least 80% | True | 91.67% is greater than 80%. |
| All planned workout days completed | False | 22 completed days are fewer than 24 planned days. |
| Monthly expenses exceed ₹5,000 | False | Total expenses of ₹4,500 are below ₹5,000. |
| Target weight achieved | False | Current weight (78 kg) is not equal to target weight (70 kg). |

## What I Learned

While building this project, I practised:

- Collecting and converting multiple user inputs.
- Breaking a larger problem into smaller calculations.
- Working with fitness and financial data.
- Calculating percentages and converting minutes into hours.
- Understanding positive and negative differences.
- Using relational operators to compare values.
- Creating Boolean expressions for logical checks.
- Choosing meaningful variable names.
- Organizing program output into separate sections.

## Assumptions and Limitations

- Numeric inputs are assumed to be valid and positive.
- Planned workout days must be greater than zero.
- At least one workout day must be completed to calculate expense per workout day.
- The target weight check requires an exact match.
- The program uses a fixed ₹5,000 monthly fitness expense threshold.
- The program does not validate user inputs or handle invalid values.

## Future Improvements

- Add input validation.
- Handle zero values safely before performing division.
- Format monetary values and percentages to two decimal places.
- Add conditional statements to provide more detailed fitness feedback.
- Improve the overall user experience.

---

**Project:** Q04 – Gym Membership & Fitness Progress Analyzer  
**Language:** Python  
**Level:** Beginner  
**Status:** Completed