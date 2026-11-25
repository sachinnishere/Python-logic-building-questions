# Q02 – Wholesale Sales Invoice

## Project Overview
A beginner-friendly Python project that generates an invoice for an electronics wholesale business.

The program collects retailer and product details, calculates the discount, GST, delivery charges and final bill. It also checks whether the order qualifies as a bulk order and whether the retailer has enough budget.

## Features

- Collects retailer and product information.
- Calculates subtotal using price and quantity.
- Calculates discount amount.
- Calculates taxable amount after discount.
- Calculates GST amount.
- Adds delivery charges to the final bill.
- Calculates remaining budget.
- Checks bulk order eligibility.
- Checks whether the final bill is within the retailer's budget.

## Concepts Used

- `input()` and `print()`
- Variables and data types (`str`, `int`, `float`)
- Type conversion
- Arithmetic operators
- Relational operators
- Logical operator (`and`)
- Percentage calculations
- Reusing variables in multiple calculations

## Sample Input

| Information | Value |
|---|---:|
| Retailer name | Rahul Enterprises |
| Product | Keyboard |
| Unit price | ₹899 |
| Quantity | 8 |
| Discount | 12% |
| GST | 12% |
| Delivery charges | ₹200 |
| Available budget | ₹10,000 |

## Output

| Calculation | Result |
|---|---:|
| Subtotal | ₹7,192 |
| Discount amount | ₹863.04 |
| Taxable amount | ₹6,328.96 |
| GST amount | ₹759.4752 |
| Final bill | ₹7,288.4352 |
| Remaining budget | ₹2,711.5648 |

**Logical checks:**
- Bulk order: `True`
- Within retailer's budget: `True`

## What I Learned

While working on this project, I learned how multiple calculations can be connected using variables.

I also practised percentage calculations and using logical operators to check multiple conditions.

Initially, I struggled to understand discount and GST calculations, but after understanding the percentage logic, I was able to implement them independently.

## Future Improvements

- Improve invoice formatting.
- Display monetary values up to two decimal places.
- Add input validation.
- Explore more Python concepts in future projects.

## Difficulty
Beginner – 1.2/10

## Technologies Used
- Python 3
- VS Code