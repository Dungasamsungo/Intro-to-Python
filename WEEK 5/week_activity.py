friends = []

print()
new_friend = ''
while new_friend != 'end':
    new_friend = input('Type the name of a friend: ').lower()
    
    if new_friend != 'end':
        friends.append(new_friend)

print('Your friend(s) are:')

for friend in friends:
    print(friend)
print()
   