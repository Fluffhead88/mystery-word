
# Word guessing game, similar to hang man
import random

#def choose_word:
with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()

print (answer)

print ("This word has", len(answer), "letters.")

#print ("_" * len(answer))

letter_guessed = []
guessed_letters = []

def guess(answer):
    letter_guessed = str(input("Guess a letter > ")).lower()
    if letter_guessed in answer:
        return True, guessed_letters
    else:
        return False, guessed_letters

def check():
    for letter in range(len(answer)):
        if guess(answer):
            word_guessed[letter] = letter_guessed


def print_letter(answer):
    turns = 8
    blank_word = ("_" * len(answer))
    while turns > 0:
        #correct_guess, letter = []
        if guess(answer):
            print (correct_guess.append(letter_guessed)) # append to list of correct guesses
        else:
            turns -=1
        return blank_word

print_letter(answer)



"""def display():
    blanks = print ("_" * len(answer))
    if guess():
        blanks.append(letter)
    else:
        print_letter()

display()


def game():
    while turns > 0:
        printing()
game()


def game():
    turns = 8


    while num_turns > 0:
        print(num_turns)"""





#keep track of letters guessed store correct and incorrect, store all correct
# incorrect and if they're correct print the letter, if incorrect print _
