# This program counts all the character in the input of the user. It stores the information in a dictionary in which keys are each character and values are the times used.

import pprint # Helps print dictionaries in a more readable way. Useful for Dictionaries and lists within dictionaries.

while True:
    print('Type in your text: (blank to exit)')
    message = str(input())
    if message == '': # Starts by checking if input has a character, if not, terminates execution.
        # 
        print('Do you really want to quit? y/n')
        confirmation = input()
        if confirmation == 'y':
            break
        else:
            continue

    count = {} # Creates an empty dictionary to keep track of characters and their counts.

    for character in message: # Loops through each character of the user's input.
        count.setdefault(character, 0) # Ensures that the key is in the count dictionary (with a default value of 0) so the program doesn't throw a keyError error when count[character] = count[character] + 1 is executed.
        count[character] = count[character] + 1 # Adds one instance everytime a character is found in the string.

    pprint.pprint(count) # This prints out the dictionary with all characters and their corresponding count.
