# Exercise 1:
# Local tax rate (10%)
# Tips (18%)

meal = float(input("Cost of a meal: "))
tax_amount = meal * 0.1
tip_amount = meal * 0.18
total_cost = meal + tax_amount + tip_amount

print(f"Your tax amount: ${tax_amount:0.2f}")
print(f"Your tip amount: ${tip_amount:0.2f}")
print(f"Total cost of a meal: ${total_cost:0.2f}")