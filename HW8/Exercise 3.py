numbers = [12, 75, 151, 108, 147, 324, 30]
for item in numbers:
    if item > 120:
        continue
    elif item > 300:
        break
    elif item % 3 == 0:
        print(item)