
# Word guessing game, similar to hang man
import random

with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()



print ("This word has", len(answer), "letters.")

print ("_" * len(answer))

def letter_guess(letter):
    letter = input("Guess a letter" ).lower()
    if letter in answer:
        return True
    else:
        return False
        print (letter)
letter_guess()


"""def play(letter, turns):
    while turns <= 8:
        if letter_guess(letter) not in (answer):
            turns -= 1
        else:
            turns = 8
            return letter, turns
play()

def main():
    turns = 8


    while num_turns > 0:
        print(num_turns)
        input_letter = input("Guess a letter ").lower()

main()"""
