#Write a program that takes two numbers as input from the user and prints their sum, difference, product, and quotient.

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("sum",a+b)
print("difference", a-b)
print("Multiply", a*b)
if b == 0:
    print("Cannot Divide by Zero")
else:
    print("divide", a/b)
    
