#use to store data 
#store data in key:value pair
#more readable, no need indexing

marks = {
    'Hindi':80, 
    'English':75,
    'Math':45
}
print(marks)
print(marks["Hindi"])
#print(marks["Science"]) This will through a error
print(marks.get("Science"))#by .get we will not recive a error if we do not have the desired key value pair.

marks['Science'] = 100 #To add something new in dictionary
print(marks) 

del marks['Science'] #to delete something from dixtionary
print(marks)
 

 