
# Word guessing game, similar to hang man
import random

with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()



print ("This word has", len(answer), "letters.")

print ("_" * len(answer))


def guess():
    letter = input("Guess a letter" ).lower()
    if letter in answer:
        return True
    else:
        return False



def playing(letter, turns):
    while turns <= 8:
        if guess():

        else:

            


"""def game():
    turns = 8


    while num_turns > 0:
        print(num_turns)
        input_letter = input("Guess a letter ").lower()

game()"""
