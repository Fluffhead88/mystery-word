
# Word guessing game, similar to hang man
import random

with open(`/usr/share/dict/words`) as infile:
    words = infile.read()

answer = random.word(words)

guess = input("Guess a letter" )

turns = 8

while turns < 8:
    wrong = 0
    for letter in word:
        if letter in answer:
            print (letter)
        else:
            print ("_")
            wrong +=1

if guess not in answer:
    turn -= 1
