import random
messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

while True:
    print('Type in your question: ')
    question = input()
    if question == '':
        break
    else:
        print('The answer to your question ' + str.lower(question) + ' is: ')
        print(messages[random.randint(0, len(messages) - 1)])
