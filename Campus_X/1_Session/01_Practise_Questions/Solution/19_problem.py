#Ques Write a program to check if a number is even or odd. Take the number as input from the user.

num = int(input("Enter a Nmber: "))

if num %2 == 0: #calculates the remainder when num is divided by 2.
    print("Number is even")
else:
    print("Number is odd")
