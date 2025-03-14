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

user_list.sort()
print(user_list)

user_list.sort(reverse=True)
print(user_list)






