#AND = both condition should true
#or = one of them should true.

age = int(input('Enter your age - '))
voter_id = input("Do you have voter id -")

if age>= 18 and voter_id == "yes":
    print('You can vote')
else:
    print('you cant vote')

AGE = int(input('Enter your age - '))
voter_ID = input("Do you have voter id -")

if age>= 18 or voter_id == "yes":
    print('You can vote')
else:
    print('you cant vote')
