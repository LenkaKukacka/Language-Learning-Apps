import os
import time
import random
import ast
import math

cards = []
file_name = "flashcards.txt"
def retrieve_cards():
    global cards
    if os.path.exists(file_name):
        with open (file_name, "r") as f:
            cards = ast.literal_eval(f.read())
            print("The current cards list contains " + str(len(cards)) + " words.")
            for i, card in enumerate(cards):
                print(str(i + 1) + ". " + str(card[0] + " : " + card[1]))
    else:
        print("File with cards does not exist!")

def quiz_game ():
    global cards
    while not len(cards) == 0:
        card = random.choice(cards)
        print("\nHere is the english word to translate: " + str(card[0]))
        guess = input("What is the translation to French? ")
        if guess == card[1]:
            print("\nBravo. This is correct!")
            cards.remove(card)
            #print(cards) #jen pro kontrolu
        else:
            print("Wrong. We will try it once again later...")

retrieve_cards()
input("Are you ready for quiz? Press Enter. ")
start = time.time()
quiz_game()
end = time.time()
print("You have guessed all the words from cards list in " + str(math.ceil(end - start)) + " seconds.\nGood Job!")
exit()

