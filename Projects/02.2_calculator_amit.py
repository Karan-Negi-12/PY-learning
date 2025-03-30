n1 = int(input("Enter first num: "))
n2 = int(input("Enter Second num: "))

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1//n2
  
choice = (input("Select the operation: \n+\n-\n*\n/\n"))
total = 0
while(choice != 'n'):
    if(choice == '+'):
        total = add(n1,n2)
        print(f"Result of {n1} {choice} {n2} is {total}")
        choice = input(f"Continue the operation with {total}? y/n: ")
        if(choice == 'n'):
            break
        else:
            n1 = total
            n2 = int(input("Enter the next number"))
            choice = (input("Select the operation: \n+\n-\n*\n/\n"))
            
        
    elif(choice == '-'):
        total = sub(n1,n2)
        print(f"Result of {n1} {choice} {n2} is {total}")
        choice = input(f"Continue with {total}? y/n: ")
        if(choice == 'n'):
            break
        else:
            n1 = total
            n2 = int(input("Enter the next number"))
            choice = (input("Select the operation: \n+\n-\n*\n/\n"))
    elif(choice == '*'):
        total = mul(n1,n2)
        print(f"Result of {n1} {choice} {n2} is {total}")
        choice = input(f"Continue with {total}? y/n: ")
        if(choice == 'n'):
            break
        else:
            n1 = total
            n2 = int(input("Enter the next number"))
            choice = (input("Select the operation: \n+\n-\n*\n/\n"))
    elif(choice == '/'):
        total = divide(n1,n2)
        print(f"Result of {n1} {choice} {n2} is {total}")
        choice = input(f"Continue with {total}? y/n: ")
        if(choice == 'n'):
            break
        else:
            n1 = total
            n2 = int(input("Enter the next number"))
            choice = (input("Select the operation: \n+\n-\n*\n/\n"))