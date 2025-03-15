#for making a continuous loop we use while

print("Programe to check if the number is even or Not")


#for exting from a while loop 
user_input = ""
while user_input != "q":

    user_input = input("enter a number or press q for quit: ")
    if user_input.isdigit():
        if int(user_input) % 2 ==0:
            print("Number is Even")
        else:
            print("Number is odd")

# while True:
#     Num1 = int(input("Enter a number -"))
#     if Num1 % 2 ==0:
#         print("Number is Even")
#     else:
#         print("Number is odd")


