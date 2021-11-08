import math

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = math.ceil(weight / (height)**2)

if BMI <= 18.5:
    print(f"You BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI <= 25:
    print(f"You BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI <= 30:
    print(f"You BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI <= 35:
    print(f"You BMI is {BMI}, you are obese.")
elif 35 < BMI:
    print(f"You BMI is {BMI}, you are clinically obese.")
