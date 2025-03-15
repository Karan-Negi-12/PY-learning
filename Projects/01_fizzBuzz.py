print("Program for FizzBuzz")
Number = int(input("Enter Number in a Range of 1-100 = "))

My_list = []

for Num in range(1, Number+1): #use of for loop
    result = "" #This is a empty variable 
    if Num % 3 == 0:
        result = result + "Fizz"
        if Num % 5 == 0:
            result = result + "Bizz"
    elif Num % 5 == 0:
        result = result + "Bizz"
    else:
        result = Num

    My_list.append(result) #adding result in list.
    
print(My_list)
