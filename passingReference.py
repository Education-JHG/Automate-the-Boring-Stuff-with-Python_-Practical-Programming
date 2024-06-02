def eggs(someParameter):
    """ Function appends the string 'Hello' to the parameter """
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)
