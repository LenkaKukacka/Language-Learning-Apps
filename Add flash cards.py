from googletrans import Translator
import os.path
import ast

cards = []
translator = Translator()
file_name = "flashcards.txt" #vychytavka s filem
def read_file():
    global cards
    if os.path.exists(file_name): #zeptat se, jestli soubor existuje prvne
        with open (file_name, "r") as f:
            #cards = list(dict.fromkeys(cards)) #duplicity as nemusim resit, protoze se to vypise-prida-prepise
            cards = ast.literal_eval(f.read()) #tohle mi napoprve nefungovalo kdyz jsem dala list a ne ten read
    return cards
def display_cards(cards):
    print("The current cards contain " + str(len(cards)) + " words.")
    for i, card in enumerate(cards):        #enumerate! for, card/s
        print(str(i + 1) + "." + card[0] + " : " + card[1]) #pozor str!
def translate_word (word_en):
    word_fr = translator.translate(word_en, src="en", dest='fr').text
    return word_fr
def create_new_card():
    global cards
    word_en = input("Write down a word in English to get Frech translation:  ")
    word_fr = translate_word(word_en)
    new_card = (word_en, word_fr) #tuple
    print(new_card)
    answer = input("Do you want to save this card? (yes/no)")
    if answer == "yes":
        cards.append(new_card)
        cards = list(dict.fromkeys(cards)) #melo by odstranit duplikaty, ale nevim co to udela s listem
        print("New card " + str(cards) +" is saved")
    else:
        print("The " + str(new_card) + " was not saved.")
def save_file():
    global cards
    with open (file_name, "w") as f:
        f.write(str(cards))


read_file()
display_cards(cards)
adding_cards = True
while adding_cards:
    create_new_card()
    check = input("Continue in adding card? (yes/no)")
    if check == "yes":
        adding_cards = True
    else:
        adding_cards = False
        saving = input("Would you like to save this cards to file? (yes/no)")
        if saving == "yes":
            save_file()
            print("Saving cards...")
        else:
            print("You have not saved this cards to the file.")
else:
    print("End of programme")
    exit()









