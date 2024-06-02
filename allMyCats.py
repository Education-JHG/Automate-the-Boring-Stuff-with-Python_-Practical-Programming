catNames = []

while True:
    print('Please enter the name of your cats.')
    name = input()
    if name == '':
        break
    else:
        catNames.append(name)
print('The cat names are: ')
for name in catNames:
    print(' ' + name)
