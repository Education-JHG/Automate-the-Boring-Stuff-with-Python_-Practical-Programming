def createDictionary(dictionaryName):
    while True:
        print('Type in the name of your new dictionary: ')
        dictionaryName = input()
        if dictionaryName == '':
            break

        dictKey = input()
        dictionaryName[dictKey] = input()
        
    print(dictionaryName)
