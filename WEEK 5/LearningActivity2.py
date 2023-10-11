
names = []
ages = []

name = ''
age = 0
count = 0
while name != 'end' and age != 'end':
    input('Add a name: ')
    input('Add his / age: ')
    count += 1

    if name != 'end' and age != 'end':
        names.append(name)
        ages.append(age)
    continue
        

for i in range(len(names)):
    name = names[i]
    age = ages[i]
print('The names and ages of your friends are: ')
print(f'Name: {name} Age: {age}')
print()
