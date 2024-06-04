def printPicnic(itemsDict, leftWidth, rightWidth):
    """ This function will will take in a dictionary of information and use center(), ljust(), and rjust()  to display that information in a neatly aligned table-like format. """
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-')) # Prints the header of the table
    for k, v in itemsDict.items():
        # take each key (k) and corresponding value (v) in the dictionary
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth)) # Aligns each element to its corresponding side. The width of each column will be established in the parameters when the funcion is called.

# Create dictiorany before calling the function
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# Examples:
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
