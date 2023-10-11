#LIST

clients = []

new_client = ''
while new_client != 'done':
    new_client = input('Add a new cleint: ')
    
    if new_client != 'done':
        clients.append(new_client)

print('Your clients are: ')

for client in clients:   
    print(client)
    print()


tips = [21, 56.65, 10.50, 56.6]
total_tip = 0

print('Total Tip is: ')
for tip in tips:
    total_tip += tip

print (total_tip)



