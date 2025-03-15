#block of code which perform some task and run when it is called
#can be reuse many times in our program whcih lessen our lines of code
#we can pass arguments to the method.

#creatinng a function 
def greeting(User= "user", age= None, *hobbies): #in User Varible we are setting default value which is user. || none is use for none value || *hobbies{Dynamic Argument} after all the values of raju for example will conclude as a list.
    print('*'*20)
    print(f"welcome {User}")
    print(f"age is - {age}")
    print("Hobies are :-")
    for hobby in hobbies:
        print(f"- {hobby}")
    print("Thanks for signing in")
    print('*'*20)

#for calling a function
greeting ("Raju", 23, "Reading", "Dancing")
greeting("", '', "Dancing", "Singing")
greeting("")
greeting('Karan', 43)
#adding mutliple values in a variable


#when we dont know about the info 
#info should be in key:value pair

def Welcome(name, **name_info):#we only can use ** at the last 
    print('*'*20)
    print(f"welcome {name}")
    for key, value in name_info.items(): #now the additional info is added in a discotinary and we are retriving info from it.
        print(f"{key} is {value}")
    print("Thanks for signing in")
    print('*'*20)


Welcome("karan", age=18, city="delhi", email="k@wdwsd")


#we can strore function output into a variable

def add(num1, num2):
    return num1 + num2

result = add(10, 20 )
print(f"{result}")


#function as modules.
#when we created a code in other file and we want to retrive it or want to use it, then we take help of this.


