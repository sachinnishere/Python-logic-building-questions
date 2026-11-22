# taking input from the customer

name = input("what is your name: ")
product_name = input("enter product name: ")
product_price = int(input("enter product price: "))
quantity_purchased = int(input("enter the quantity of the product: "))
total_cost = product_price * quantity_purchased
customer_budget = int(input("enter your budget: "))
remaining_money = customer_budget - total_cost
bill_exceeds_budget = total_cost > customer_budget

# creating a gap between customer invoice and user input

print("")

# customer invoice

print("customer invoice")

# creating a gap between bill and customer invoice

print("")

# printing the bill with lables

print("your name:", name)
print("product name:", product_name)
print("product price:", product_price)
print("quantity purchased:", quantity_purchased)
print("total cost of products:", total_cost)
print("customer total budget:", customer_budget)
print("remaining cash:", remaining_money)
print("Does the bill exceed the budget:", bill_exceeds_budget)