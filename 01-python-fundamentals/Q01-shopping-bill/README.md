# Q01 – Smart Shopping Bill Calculator

**Difficulty:** Beginner (1/10)  
**Status:** Completed independently

## 1. Problem Statement

Imagine buying products from an electronics shop.

The task is to create a Python program that collects customer and product details, calculates the total bill, checks the remaining budget and determines whether the bill exceeds the customer's budget.

## 2. Requirements

- Take the customer's name and product details.
- Take the product price and quantity.
- Calculate the total cost.
- Take the customer's available budget.
- Calculate the remaining money.
- Check whether the bill exceeds the budget.
- Display a complete customer invoice.

## 3. Concepts Used

- Variables
- Data types (`str`, `int`, `bool`)
- User input (`input()`)
- Type conversion (`int()`)
- Arithmetic operators (`*`, `-`)
- Relational operators (`>`)
- Boolean values
- Comments and print statements

## 4. Sample Input

| Input | Value |
|---|---|
| Customer name | Rahul |
| Product name | Keyboard |
| Product price | ₹449 |
| Quantity | 12 |
| Customer budget | ₹7,500 |

## 5. Program Output

```text
customer invoice

your name: Rahul
product name: keyboard
product price: 449
quantity purchased: 12
total cost of products: 5388
customer total budget: 7500
remaining cash: 2112
Does the bill exceed the budget: False
```

## 6. Calculation Breakdown

- Total cost = 449 × 12 = ₹5,388
- Remaining money = 7,500 − 5,388 = ₹2,112
- Budget check = 5,388 > 7,500 → False

## 7. What I Learned

- How to collect information using `input()`.
- Why numerical inputs need type conversion.
- How to perform calculations using variables.
- How relational operators return Boolean values.
- How to organise program output using descriptive labels.

## 8. Future Improvement

Add a section to display the data types of important variables using Python's `type()` function.

---

**Project:** Python Logic Building Journey  
**Question:** Q01  
**Language:** Python