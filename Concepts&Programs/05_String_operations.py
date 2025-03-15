f_nmae = "Karan"
l_name = "Negi"
#strings are immutable

full_name = f_nmae + " " + l_name

print (full_name)
#functions 
print (full_name.upper())
print (full_name.lower())

msg = "My name is karan am a DevOps enginner"
print (msg.title()) #make it look like a title
print (msg.split()) #seprate after space
print (msg.split("am")) #seprate after am 

print (msg[0]) #Indexing 
print (msg[1:4]) #Range start from 1 and print values till 3.
print (msg[-1]) #negative indexing
print (msg[-1:-5]) 