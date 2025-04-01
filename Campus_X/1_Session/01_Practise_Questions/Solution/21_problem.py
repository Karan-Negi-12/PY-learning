#Ques Write a program to find the minimum of two numbers. Take the numbers as input from the user.

num1 = float(input("Enter First: "))
num2 = float(input("Enter Second: "))

if num1>num2:
    print(f"{num2} Second is Smallest")
elif num1 == num2:
    print("Both are same")
else:
    print(f"{num1} First is smallest")
