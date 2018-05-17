
# Word guessing game, similar to hang man
import random

with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()

print (answer)

print ("This word has", len(answer), "letters.")

print ("_" * len(answer))


def guess():
    letter = input("Guess a letter" ).lower()
    if letter in answer:
        return True
    else:
        return False
    
guess()

#keep track of letters guessed store correct and incorrect, store all correct
# incorrect and if they're correct print the letter, if incorrect print _
