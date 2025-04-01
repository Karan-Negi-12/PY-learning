#Ques Write a program to find the maximum of two numbers. Take the numbers as input from the user.

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

if a>b:
    print(f"{a} a is Maximum")
elif a == b:
    print("both are eual")
else:
    print(f"{b} B is Maximum")
