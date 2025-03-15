age = int(input('Enter your age - '))
voter_id = input("Do you have voter id -")
if age>= 18:
    if voter_id == "yes":
        print('You can vote')
    else:
        print("Plesase create one")
else:
    print('you cant vote')