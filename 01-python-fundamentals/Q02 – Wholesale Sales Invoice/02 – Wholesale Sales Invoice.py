#collecting information:

name = input("enter reatailer's name: ")
product_name = input("enter product name: ")
unit_price = float(input("enter price per unit: "))
quantity_ordered = int(input("quantity ordered: "))
discount_percent = float(input("enter discount in percentage: "))
GST = float(input("enter percentage of gst: "))
delivery_charges = float(input("enter delivery charges: "))
total_budget = float(input("enter reatailer's total budget: "))

#performing calculations:

subtotal = unit_price * quantity_ordered
discount_amount = subtotal * (discount_percent / 100)
taxable_amount = subtotal - discount_amount
GST_amount = taxable_amount * (GST/100)
final_bill = GST_amount + taxable_amount + delivery_charges
remaining_budget = total_budget - final_bill

#logic test

minimum_quantity = quantity_ordered >= 5
mimimum_subtotal = subtotal >= 5000

bulk_order = minimum_quantity and mimimum_subtotal

#checking if the final bill is within the retailer's budget or not

within_budget = total_budget >= final_bill

#creating gap between above information and invoice

print("")

#printing invoice

print("TAX INVOICE")

print("")

print("retailer:", name)
print("product:", product_name)
print("unit price:", unit_price)
print("quantity:", quantity_ordered)
print("discount:", discount_percent)
print("GST rate:", GST)
print("delivery charges:", delivery_charges)
print("total budget:", total_budget)

print("")

print("subtotal:", subtotal)
print("discount amount:", discount_amount)
print("taxable amount:", taxable_amount)
print("GST amount on subtotal:", GST_amount)
print("final bill:", final_bill)
print("remaining budget:", remaining_budget)

print("")

print("bulk order:",bulk_order)

print("within retailer's budget:",within_budget)