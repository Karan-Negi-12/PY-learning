#----------Calculator---------------------
#print("*"*10 |"calculator")
print("*****Calculator*****")
N1 = int(input("Enter first Number -"))
N2 = int(input("Enter Second Number -"))

operation_list = ["+", "-", "*", "/"] #creating a list whcih contain Arthmetic Operation

print("Chose Operation:-")
for chose in operation_list:
    print(chose)

#function = [Add, Sub, Multiply]

input("= ")
# for result in function:
#     if result == Add:
#         print()
    
     
#Creating Arthmetic functions
def Add(N1, N2):
    return N1 + N2

def Sub(N1, N2):
    return N1 - N2
    
def Multiply(N1, N2):
    return N1 * N2

def Divide(N1, N2):
    return N1 // N2
   

    

