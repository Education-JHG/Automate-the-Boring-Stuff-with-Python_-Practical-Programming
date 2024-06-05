#! python3
# phoneAndEmailFinder.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(
                        (\D{3}|\(\d{3}\))?                  # area code
                        (\s|-|\.)?                          # separator
                        (\d{3})                             # first 3 digits
                        (\s|-|\.)?                          # separator
                        (\d{4})                             # las 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2, 5}))?     # extension 
                        )'''. re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+                      # username
                        @                                      # @ symbol
                        [a-zA-Z0-9._%+-]+                      # domain name
                        (\.[a-zA-Z]{2, 4})                     # dot-something
                        )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = [] # List variable to store all the matches.
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TODO: Copy results to the clipboard