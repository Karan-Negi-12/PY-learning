#Ques Write a program to calculate the simple interest. Take the principal, rate, and time as input from the user.
#A = P (1 + rt)

print("This program will calculate Simple Intrest")
principal = float(input("Enter Principle Amount: "))
rate = float(input("Enter Rate: "))
Time = float(input("Enter Time: "))

final =  principal *(1 + rate*Time)

print(f"Simple Intrest ={final}")
