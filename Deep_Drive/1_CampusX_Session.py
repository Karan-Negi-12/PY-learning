#x() this whole{x()} is a function in python we input some data and then we will recive the output


#-----------------python  Output-----------------------------------
#python is a cse sensitive Language || print is a function in python. || bulit in fuunctions are the function which are already present in python. 
print("Hello World!") #these "" are used to tell python that this is a string || print in lower-csaetive || print is a function in python.
print(7)
print(7.77)
print(True)
#print function print output seprated by a space. || how to change this behaviour.
print("karan", 7, 7.7, sep="\n") #this sep perameter gives a speace seprate within a fuction.
print("Karan", end = "-") #End parameter goes to a new line after every print function 
print("Karan")

type(7) #type is a function in python which is used to find the type of the data.


#-------------------Data Types-----------------------------------
#1. Interger 
print(8)
print(1e308) #this is a interger || the largest number that can be stored in a interger is 1e308 or 10^308

#2. Float/Decimal
print(7.77)
print(1e-308) #this is a float || the smallest number that can be stored in a float is 1e-308 or 10^-308 
print(1.7e308) #this is a float || the largest number that can be stored in a float is 1.7e308 or 1.

#3. String/text
print("karan")
print("7") #this is a string || string is a collection of characters || string is a collection of characters

#4. Boolean
print(True)
print(False) #this is a boolean || boolean is a data type which can be either

#5. None
print(None) #this is a none || none is a data type which can be either
#it is use to declare a variable which is not assigned any value. || for future use

#6 complex Number
print(5+6j) 

#7. List
print([1,2,3,4,5,6,7,8,9])

#8. Tuple
print((1,2,3,4,5,6,7,8,9))

#9. Dictionary
print({"name":"karan", "age":19})

#10. Set
print({1,2,3,4,5,6,7,8,9})

#11. Frozenset
print(frozenset({1,2,3,4,5,6,7,8,9}))

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType


#-------------------Variables-----------------------------------
#Variables are containers for storing data values. || Variables are created when you assign a value to it. || Variables do not need to be declared with any particular type, and can even change type after they have been set. || Variables are containers. 
#they are containers for future use. 
name = "karan" #this is a variable || name is a variable || karan is a value. 
age = 19 
a = 4
b = a
print(b) 
#dynamic typing || dynamic typing is a type of programming language where the type of a variable can change during the execution of the program. || here we dont tell about the data type of the variable.
num = 987
print(num) 

#staic typing || static typing is a type of programming language where the type of a variable must be declared before the use of the
#int a = 7;

#dynamic binding || dynamic binding variable can change during the execution of the program.
c = 5
print(c)
c = "karan"
print(c)

a,b,c, = 1,2,3 
print(a,b,c)

x=y=z = 10 #when we need to assign the same value to multiple variables we can use this method.
print(x,y,z)

#-------------------Key words and Identifiers-----------------------------------
#keywords are the reserved words in python || we cannot use these keywords as a variable name. 
#False, True, None, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield || there are 32 keywords in python.

#identifiers are the names given to variables, functions, classes, and other user-defined objects.
#identifiers are case sensitive. || never start with number || never use special character except _|| cannot be key words.

#-------------------USer Input-----------------------------------
input('Enter your mail')


#-------------------Ques 1 Add two number by user input-------------------
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum = num1 + num2 #This will add intergers like a string becoze the input function takes the input as a string.|| string is a univrsal format of data. || we can store diff data type in string. 
K = int(input("Enter the first number: ")) #this is type conversion || we can convert the data type of a variable.
f = int(input("Enter the first number: "))
sum = K + f 
print(sum)
print(type(K))
# K is int
#if we do {sum = int(k) + int(f)} then it will give error because we cant add a string to a int.}
#K is still a str || we can convert it to int by using int() function. || whenver we do type converstion it create a new object or value || its just for the manipulation of data. || type coneverstion do not change the data type of the variable. its just create a new object. 


#-------------------Type conversion-------------------
#its a way to convert one data type to another data type. || does not made permane change in the data type. || original one remain same and we just work on that new one.

#implict type conversion || this is done by python itself. || this have limitation like cannot add string and intrger.
print(5+5.6)

#explicit type conversion || this is done by the user.
#strng into int
type(int("5"))
#int into string
type(str(5)) #cannot convert complex number into the integer


#----------------------literals----------------------
#literals are the raw values that are used in the program. || literals are the constants that are used in the program. || the value which we store in the variable is called literal.

h = 5344 #here h is variable || = is an assignment operator || 5344 is a literal.
bianry_set_krne_ke_liye = 0b1010 
octal_repersation = 0o12
hexadecimal_repersation = 0x12c

float_1 = 10.5
float_2 = 1.5e2 # 1.5 * 10^2

complex_repersation = 56j


#----------------------Boolen---------------------
#true is 1 || false is 0
t = True + 4
f = False + 10
print(t,f)
#python treat boolen as int || true is 1 || false is 0 for methametical operation.


