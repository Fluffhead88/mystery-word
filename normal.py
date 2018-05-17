
# Word guessing game, similar to hang man
import random

with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()

print (answer)

"""print ("This work has" len(answer) " letters.")

print ("_" * len(answer))

def letter_guess(answer):
    letter = input("Guess a letter" ).lower()
    if letter in answer:
        return True
    else:
        return False

turns = 8

def play(letter, turns):
    while turns <= 8:
        if letter_guess(letter):
            return (letter)
        else:
            turn -= 1"""
