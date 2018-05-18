
# Word guessing game, similar to hang man
import random

#def choose_word:
with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower()

print (answer)



#print ("_" * len(answer))

letter_guessed = []
guessed_letters = []
game_word = []
len_word = len(answer)

def get_word():
    for char in answer:
        guess_word.append("_")
    print("This word has ", len_word, "letters")
    return(game_word)



"""def guess(answer):
    letter_guessed = str(input("Guess a letter > ")).lower()
    if letter_guessed in answer:
        return True, guessed_letters
    else:
        return False, guessed_letters"""


def play():
    turns = 8
    print (turns)
    while turns < 8
    letter_guessed = str(input("Guess a letter > ")).lower()
    if letter_guessed in guessed_letters:
        print ("You already guessed that letter.")
    else:
        guessed_letters.append(guess)
    if guess in answer:
        print("Correct!")
        # Do something to replace "_" with letters
        for letter in range(0, len_word):
            if answer[letter] == letter_guessed:
                game_word[letter] = letter_guessed
        if not '_' in game_word:
            print("You win!")
    else:
        turn -= 1

get_word()
play()


"""def print_letter(answer):
    turns = 8
    blank_word = ("_" * len(answer))
    while turns > 0:
        #correct_guess, letter = []
        if guess(answer):
            print (correct_guess.append(letter_guessed)) # append to list of correct guesses
        else:
            turns -=1
        return blank_word"""


#print_letter(answer)



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
