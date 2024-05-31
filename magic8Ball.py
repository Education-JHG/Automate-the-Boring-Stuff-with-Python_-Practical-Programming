# Import random library
import random, sys

def getAnswer(answerNumber):
    """ Compares a random number simulating an 8-Ball toy """
    if answerNumber == 1:
        return 'It is certain'
    if answerNumber == 2:
        return 'It is decidedly so'
    if answerNumber == 3:
        return 'Yes'
    if answerNumber == 4:
        return 'Reply hazy try again'
    if answerNumber == 5:
        return 'Ask again later'
    if answerNumber == 6:
        return 'Concentrate and ask again'
    if answerNumber == 7:
        return 'Outlook not so good'
    if answerNumber == 8:
        return 'Very doubtful'


# Ask the user to enter a question
print('Please enter your question: ')
question = input()

# Generate a random number
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)