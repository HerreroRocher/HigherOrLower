import random, time
import tkinter as tk
from tkinter import Tk, Canvas, PhotoImage, font
from PIL import Image, ImageTk

class Card:
    def __init__(self, number, suit, aceIsEleven, kingsValueMorethan10):
        self.number = number
        self.suit = suit
        self.generateValues(aceIsEleven, kingsValueMorethan10)
    
    def generateValues(self, aceIsEleven, kingsValueMorethan10):

            if self.number == 'Ace':
                self.value = 11 if aceIsEleven else 1
            elif self.number == 'Jack':
                self.value = 11 if kingsValueMorethan10 else 10
            elif self.number == 'Queen':
                self.value = 12 if kingsValueMorethan10 else 10
            elif self.number == 'King':
                self.value = 13 if kingsValueMorethan10 else 10
            elif self.number == 'Joker':
                self.value = 0
            else:
                self.value = int(self.number)
            

    

class Deck:
    def __init__(self, jokers, aceIsEleven, kingsValueMorethan10):
        self.deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for i in range(4):
            suit = suits[i]
            for i in range(1,14):
                if i == 1:
                    number = 'Ace'
                elif i == 11:
                    number = 'Jack'
                elif i == 12:
                    number = 'Queen'
                elif i == 13:
                    number = 'King'
                else:
                    number = i
                self.deck.append(Card(number,suit, aceIsEleven, kingsValueMorethan10))

        if jokers:
            self.deck.append(Card('Joker', 'Red', aceIsEleven, kingsValueMorethan10))
            self.deck.append(Card('Joker', 'Black', aceIsEleven, kingsValueMorethan10))
    
    def shuffle(self):
        print("Shuffling...")
        random.shuffle(self.deck)
        time.sleep(1)

    def showTopCard(self):
        print("Revealing card...")
        time.sleep(1)
        print(f"The revealed card is the {self.deck[0].number} of {self.deck[0].suit}!")
        self.deck.pop(0)

    def getTopCard(self):
        return self.deck[0]


def change_cursor(event):
    global jokersTextOption
    canvas.config(cursor="hand2")  # Change cursor to a pointing hand

def reset_cursor(event):

    canvas.config(cursor="arrow")  # Reset cursor to default



def printSettings():
    setitingsStartWidth = 250


    def makeSettingChanges(jokersTextOption, aceTextOption, kingsValueOption):
        canvas.pack() 

        if settings[0]:
            canvas.itemconfig(jokersTextOption, text="There are jokers in the deck.")

        else:
            canvas.itemconfig(jokersTextOption, text="There are no jokers in the deck.")

        if settings[1]:
            canvas.itemconfig(aceTextOption, text="The value of the Ace is 11.")

        else:
            canvas.itemconfig(aceTextOption, text="The value of the Ace is 1.")

        if settings[2]:
            canvas.itemconfig(kingsValueOption, text="The Jack, Queen and King are of values 11, 12 and 13 respectively.")

        else:
            canvas.itemconfig(kingsValueOption, text="The Jack, Queen and King all are of value 10.")



    def makeChanges(i, jokersTextOption, aceTextOption, kingsValueOption):
        global settings
        print(f"Old values {settings[0]}, {settings[1]}, {settings[2]} )")
        settings[i] = not settings[i]
        print(f"New values {settings[0]}, {settings[1]}, {settings[2]} )")
        makeSettingChanges(jokersTextOption, aceTextOption, kingsValueOption)

    canvas.pack()

    settingsIntro = canvas.create_text(25,200, text="Here are the current settings(click to change):", anchor="w",fill="white",font=font.Font(family="Arial", size=15, underline=True))

        
    jokersTextOption = canvas.create_text(25,setitingsStartWidth, text="There are jokers in the deck.", anchor="w",fill="white",font=("Arial", 15))
    aceTextOption = canvas.create_text(25,setitingsStartWidth + 50, text="The value of the Ace is 11.", anchor="w",fill="white",font=("Arial", 15))
    kingsValueOption = canvas.create_text(25,setitingsStartWidth + 100, text="The Jack, Queen and King are of values 11, 12 and 13 respectively.", anchor="w",fill="white",font=("Arial", 15))
    makeSettingChanges(jokersTextOption, aceTextOption, kingsValueOption)

    canvas.tag_bind(jokersTextOption, "<Enter>", change_cursor)
    canvas.tag_bind(jokersTextOption, "<Leave>", reset_cursor)


    canvas.tag_bind(aceTextOption, "<Enter>", change_cursor)
    canvas.tag_bind(aceTextOption, "<Leave>", reset_cursor)


    canvas.tag_bind(kingsValueOption, "<Enter>", change_cursor)
    canvas.tag_bind(kingsValueOption, "<Leave>", reset_cursor)

    canvas.tag_bind(jokersTextOption, "<Button-1>", lambda event: makeChanges(0, jokersTextOption, aceTextOption, kingsValueOption))

    canvas.tag_bind(aceTextOption, "<Button-1>", lambda event: makeChanges(1, jokersTextOption, aceTextOption, kingsValueOption))

    canvas.tag_bind(kingsValueOption, "<Button-1>", lambda event: makeChanges(2, jokersTextOption, aceTextOption, kingsValueOption))

    


 
    


    


def showDeck():
    for card in deck.deck:
        print(f"{card.number} of {card.suit}")



def playRound(roundNum):
    global last_value 
    global points
    print("--------------------")
    print(f"Round {roundNum}:")
    HigherOrLower = input("Guess if the next card to be revealed will be Higher or Lower: ").upper()
    winner = True if HigherOrLower == "HIGHER" and deck.getTopCard().value > last_value or HigherOrLower == "LOWER" and deck.getTopCard().value < last_value else False
    drawer = True if deck.getTopCard().value == last_value else False
    last_value = deck.getTopCard().value
    deck.showTopCard()
    if drawer:
        print("You got lucky this round!")
        points += 1
    elif winner:
        print("Well done! You got it right!")
        points += 1
    else:
        print("Better luck next time!")

def endGame():
    print(f"That's all of the rounds done! You got {points}/{rounds} points")
    if points/rounds > 0.7:
        print("Congratulations you played very well! Hope you enjoyed!")
    elif points/rounds > 0.4:
        print("Okay...Decent score, maybe you can get more if you go again...")
    else:
        print("Oh no...You need to practice. For your sake, I'm going to assume you don't understand the rules. Play again!")



def showRules():

    canvas.pack()
    introText = canvas.create_text(width/2,25, text="Welcome to Daniel's Higher/Lower Game!", anchor="center",fill="white",font=("Arial", 20))
    rulestext = canvas.create_text(width/2,100, text="The goal of this game is to guess whether the next card to be shown from the deck will be higher or lower than the current card that's shown. After each guess the card will be revealed.", anchor="center",fill="white",font=("Arial", 15), width=width) 
    global rounds
    # while not (rounds > 0 and rounds < 20):
    #     rounds = int(input("How many rounds would you like to play? (1-20) ")) 
    rounds = 5
        
    printSettings()



window = Tk() #Creates instance of Tk class
width = 800
height = 600

def configureWindow(width, height):
    geometryInit = str(width)+"x"+str(height)
    window.configure(background="black")
    window.title("Higher or Lower")
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    xSpace = 0.5*(screenWidth-width)
    ySpace = 0.5*(screenHeight-height)
    window.geometry(geometryInit+"+"+str(int(xSpace))+"+"+str(int(ySpace)))
    
configureWindow(width, height)



#Creating a canvas
canvas = Canvas(window, bg="black", width=width, height=height)
settings = [True, True,True] #First is True if we have jokers, second if the ace is value 11, third if kings value is not 13
points = 0
rounds = 0



def on_closing():
    window.destroy()  
    exit()      





showRules()
window.protocol("WM_DELETE_WINDOW", on_closing)





def on_play(event):
    print("Play button clicked!")


image = Image.open("play_button.png") 

max_height = height/4

original_width, original_height = image.size
new_height = int(max_height)
new_width = int((max_height / original_height) * original_width)

scaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

play_image = ImageTk.PhotoImage(scaled_image)
window.play_image = play_image

play_button = canvas.create_image(width / 2, height*13 / 16, image=play_image)

canvas.tag_bind(play_button, "<Button-1>", on_play)
canvas.tag_bind(play_button, "<Enter>", change_cursor)
canvas.tag_bind(play_button, "<Leave>", reset_cursor)

canvas.pack()















window.mainloop() 

deck = Deck(settings[0], settings[1], settings[2])




print("Let's go!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")


deck.shuffle()
last_value = deck.getTopCard().value
deck.showTopCard()


    



for i in range(rounds):
    playRound(i+1)

endGame()


# showDeck()
            

