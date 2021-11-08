quantity = int(input("Enter quantity: "))
if quantity * 100 > 1000:
  print("Cost is", ((quantity * 100) - (.1 * quantity * 100)))
else:
  print("Cost is", quantity * 100)