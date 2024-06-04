#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.


# This script will get the text from the clipboard, add a star and space to the biginning of each line, and then paste this new text to the clipboard.
# Main tasks:
#   1. Paste text from the clipboard
#   2. Add star to each line
#   3. Copy the new text to the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n') #creates a list
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
print('Your text has been copied to the clipboard.')

""" Even if you dont need to automate this specific task, you might want to
automate some other kind of text manipulation, such as removing trailing
spaces from the end of lines or converting text to uppercase or lowercase.
Whatever your needs, you can use the clipboard for input and output. """