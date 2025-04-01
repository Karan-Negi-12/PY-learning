#Ques Write a program to extract a substring from a given string. Take the start and end indices as input from the user.

text = input("enter a string: \n")

s_len = len(text)
print(s_len)

a = int(input("enter start index: "))
b = int(input("enter end index: "))

sub_string = text[a:b] #String slicing in Python uses the syntax [start:end] || It extracts the portion of the string from the character at start_index up to (but not including) the character at end_index
print(sub_string)
