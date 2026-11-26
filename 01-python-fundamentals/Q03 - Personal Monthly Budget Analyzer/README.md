# Q03 – Personal Monthly Budget Analyzer

## Project Overview

The Personal Monthly Budget Analyzer is a Python program that helps users analyze their monthly income, expenses, and savings.

The program collects financial information from the user and performs different calculations to provide a detailed overview of their monthly budget.

## Features

- Collects monthly income and expense details.
- Categorizes expenses into housing, living, and lifestyle expenses.
- Calculates total monthly expenses.
- Calculates remaining money after expenses.
- Calculates the remaining balance after achieving the savings target.
- Calculates the percentage of income spent and saved.
- Calculates the percentage share of each expense category.
- Checks whether expenses exceed 70% of monthly income.
- Checks whether the savings target has been achieved.
- Checks whether total expenses exceed monthly income.

## Concepts Used

This project uses the following Python concepts:

- Variables and data types
- `input()` and `print()`
- Type conversion using `float()`
- Arithmetic operators
- Relational operators
- Boolean expressions
- Percentage calculations
- Variable grouping and calculations

**Note:** This project does not use `if/else`, loops, functions, or lists.

## Sample Input

| Input | Value |
|---|---:|
| Name | Sachin |
| Monthly Income | ₹90,000 |
| House Rent | ₹15,000 |
| Food Expenses | ₹8,000 |
| Transportation Expenses | ₹10,000 |
| Entertainment Expenses | ₹10,000 |
| Shopping Expenses | ₹20,000 |
| Savings Target | ₹25,000 |

## Sample Output

```text
Name: Sachin
Monthly income: 90000.0
Monthly house rent: 15000.0
Monthly food expenses: 8000.0
Monthly transportation expenses: 10000.0
Monthly entertainment expenses: 10000.0
Monthly shopping expenses: 20000.0
Monthly savings target: 25000.0

Total monthly expenses: 63000.0
Income spent percentage: 70.0
Remaining money after all expenses: 27000.0
Money saved in percentage after all expenses: 30.0
Balance after expenses and savings: 2000.0

Share of total monthly expenses (in percent):

House rent as percentage: 23.809523809523807
Food expenses as percentage: 12.698412698412698
Transportation expenses as percentage: 15.873015873015872
Entertainment expenses as percentage: 15.873015873015872
Shopping expenses as percentage of total monthly expenses: 31.746031746031743

Final logic checks

Expenses exceeds 70 percent of income: False
Savings target achieved: True
Expenses exceeds monthly income: False
```

## Calculations Explained

**1. Total Monthly Expenses**

All expense categories are added together.

₹15,000 + ₹8,000 + ₹10,000 + ₹10,000 + ₹20,000 = ₹63,000

**2. Remaining Money After Expenses**

Monthly income minus total monthly expenses.

₹90,000 - ₹63,000 = ₹27,000

**3. Balance After Savings Target**

Remaining money after expenses minus the savings target.

₹27,000 - ₹25,000 = ₹2,000

**4. Income Spent Percentage**

(Total expenses / Monthly income) × 100

(63,000 / 90,000) × 100 = 70%

**5. Money Saved Percentage**

(Remaining money after expenses / Monthly income) × 100

(27,000 / 90,000) × 100 = 30%

## Logical Checks

| Condition | Result | Explanation |
|---|---|---|
| Expenses exceed 70% of income | False | Expenses are exactly 70%, not greater than 70%. |
| Savings target achieved | True | ₹27,000 remaining is greater than the ₹25,000 target. |
| Expenses exceed monthly income | False | ₹63,000 expenses are less than ₹90,000 income. |

## What I Learned

While building this project, I practised:

- Working with multiple user inputs.
- Breaking a larger calculation into smaller steps.
- Grouping related expenses into categories.
- Calculating percentages using arithmetic operators.
- Comparing financial values using relational operators.
- Using Boolean expressions to check different conditions.
- Organizing calculations and displaying a structured financial report.

## Future Improvements

- Add input validation to prevent negative values.
- Handle zero income and zero expenses safely.
- Format monetary values to two decimal places.
- Add conditional statements to provide better financial feedback.
- Improve the overall user experience.

---

**Project:** Q03 – Personal Monthly Budget Analyzer  
**Language:** Python  
**Level:** Beginner  
**Status:** Completed