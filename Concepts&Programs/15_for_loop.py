#execute a block of code for each time in the sequence (such as a list, tuple, string or range)

for i in 1, 2, 3, 4, 5: #for loop (i) hr ek number ke pass gya aur output bheja 
    print(i)

#for loop use with list
user_list = ['Karan', 'noni', 'puchi', 'Alex', 'Hani']
for user in user_list:
    print(user)

#for loop use with dictionaries.
marks = {
    'Hindi':80, 
    'English':75,
    'Math':45
}

for key, value in marks.items():
    print(f"subject is - {key}")
    print(f"marks is - {value}")

for key in marks.keys(): #when we need only key from dictionaries
    print(f"{key}")

for value in marks.values(): #when we need only value from dictinoroes
    print(f"{value}")

#----------------use case -------------------
#when we need to print 1-10000 number

for i in range(1, 100):#it will print 1-99 number 100 is range so it will not print it.
    print(i)
    
