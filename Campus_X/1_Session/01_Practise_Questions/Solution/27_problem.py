#ques Write a program to replace a character in a string with another character. Take the original string, character to replace, and the new character as input from the user.

s = input("Enter a String:\n")
r = input("Enter a char to reove: ")
n = input("enter a new char to add: ")

modified = s.replace(r, n)#replace is used to replace a old chr with new.

print(modified)
