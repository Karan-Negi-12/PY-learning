#ordered sequence of different type of values

user_list = ['Karan', 'Hani', 'Amit', 'Gaurav']

print(user_list)
print(user_list[0])
print(user_list[-2])

#modify user list
user_list.append('Paul') #to add on list
print(user_list)

user_list.insert(2, 'Sham') #by this we can add value on a specific place on a list.
print(user_list)

user_list.remove('Paul') #to remove value on list
print(user_list)

del user_list[2] #To delete value with index number.
print(user_list)

user_list[2] = 'Alex' #to change value with another new value on list 
print(user_list)

print(len(user_list)) #to find the length of list.


#------------------------Sorting of list------------------------------

user_list.sort() #this will sort the whole list
print(user_list)

user_list.sort(reverse=True) #this will sort the list in reverse order.
print(user_list)

user_list.reverse() #will reverse all the values with in a list
print (user_list)

user_list.pop() #Pop remove last/recent added value from the list
print(user_list)
#diff btw Remove&Pop when we use remove with in print it will give us eror but Pop provide us the value as well as we can use pop witn in a variable to retrive something 
'''
exampple of Pop 
removed_value = user_list.pop()
print(removed_value)
'''
user_list.pop(2)
print(user_list)

#-----------Numeric list ---------------------

marks = [23, 3, 343, 34, 65, 87, 843, 90, 243, 13]
print(marks)
print(min(marks))
print(max(marks))
print(sum(marks))

#----List--

Mix_list = ['karan', 23, 43.45]


