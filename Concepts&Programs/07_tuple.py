#same as list but we cant modify the values in Tuple.
#1- its immutable
#2- its ordered

days = ('mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun')
print(type(days))
print(days)
print(days[1]) 
print(days.count('mon')) #this is use to count the number of repetation of a particluar value. 
#days[0] ='hi'
print(days.index('tue')) #this is use to count the index of a value.


