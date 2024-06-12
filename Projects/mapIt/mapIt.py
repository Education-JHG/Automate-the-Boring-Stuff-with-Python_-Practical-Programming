#! python3
# mapIt - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1: # Stores a list of the program's filename and command line argument. If this list has more than just the filename in it, then it evaluates to an integer greater than 1, meaning that command line arguments have been provided.
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)