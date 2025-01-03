# Lab One: Display a map of 6 houses split between two rows with the house in the center
# of the top row being the user's house marked by a *.  All houses should display their #'s

# Ask for the users house and street address

user_house = int(input('\nenter house number:   '))
user_street = input('enter street address: \n')

# info
print(f"These are your neighbors' addresses on {user_street}")
print('You are at the *\n')

# house numbers
house_number = int(user_house)
house_left = int(user_house - 2)
house_right = int(user_house + 2)
house_below = int(user_house + 1)
house_corner_left = int(user_house - 1)
house_corner_right = int(user_house + 3)
# row one
print('  _       _       _')
print(' / \\     / \\     / \\')
print('/   \\   / * \\   /   \\')
print('|___|   |___|   |___|')
print(f' {house_left}     {house_number}     {house_right}\n')


# row two
print('  _       _       _')
print(' / \\     / \\     / \\')
print('/   \\   /   \\   /   \\')
print('|___|   |___|   |___|')
print(f' {house_corner_left}     {house_below}     {house_corner_right}\n')








