# Exercise 4:

x = float(input("Enter principal amount: $ "))
y = float(input("Enter annual interest rate %"))
n = float(input("Enter number of times per year interest has compounded: "))
t = float(input("Enter number of years account will be left to earn interest: "))

y /= 100
A = x * ((1 + (y / n))**(n * t))

print("After ", t, " years, $", format(A, ',.2f'), " will be in the account. ", sep="")