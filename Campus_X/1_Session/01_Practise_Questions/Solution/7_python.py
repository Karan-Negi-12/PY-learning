#Ques Write a program to swap the values of two variables, a and b.

a = 4
b = "Karan"

print("Before Swaping")
print (a, b)

a, b = b, a 

print("After Swaping")
print (a, b)

#Alternatives
# a = 10
# b = 5

# 1. Using a temp variable
# temp = a
# a = b
# b = temp

# 2. Pythonic way
# a, b = b, a  