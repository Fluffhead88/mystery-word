
# Word guessing game, similar to hang man
import random

with open(`/usr/share/dict/words`) as infile:
    word = infile.read()

answer = random.word(word)

print ("This work has" len(answer) " letters.")

#def letter_guess(answer):
#    letter = input("Guess a letter" )
#    if letter in answer:
#        return True
#    else:
#        return False

guess = input("Guess a letter ")
turns = 8

def play(letter):
    while turns < 8:
        if letter_guess in answer:
            print (letter)
        else:
            turn -= 1
        print ("_")
