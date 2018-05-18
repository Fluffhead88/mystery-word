
# Word guessing game, similar to hang man
import random

with open('/usr/share/dict/words') as infile:
    word = infile.readlines()

answer = random.choice(word).lower().replace("\n", "")
used_letters = []
game_word = []
len_word = len(answer)
print (answer)

def display():
    for char in answer:
        game_word.append('_')
    print("This word has ", len_word, "letters")
    return game_word



def play():
    turns = 8
    print (turns)
    while turns > 0:
        print(game_word)
        if '_' not in game_word:
            print("You win!")
            break
        letter_guessed = (input("Guess a letter > ")).lower()
        if letter_guessed in used_letters:
            print ("You already guessed that letter.")
        else:
            used_letters.append(letter_guessed)
            if letter_guessed in answer:
                print("Correct!")
            else:
                turns -= 1
            for letter in range(0, len_word):
                if answer[letter] == letter_guessed:
                    game_word[letter] = letter_guessed



display()
play()
