import random, time
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
    

jokers = True
aceIsEleven = True
kingsValueMorethan10 = True

settings = [jokers, aceIsEleven, kingsValueMorethan10]

def printSettings():
    print("Here are the current settings:")

    if settings[0]:
        print("There are jokers in the deck. [1]")
    else:
        print("There are no jokers in the deck. [1]")

    if settings[1]:
        print("The value of the Ace is 11. [2]")
    else:
        print("The value of the Ace is 1. [2]")

    if settings[2]:
        print("The Jack, Queen and King are of values 11, 12 and 13 respectively. [3]")
    else:
        print("The Jack, Queen and King all are of value 10. [3]")

    userinput = input("Enter the number of the setting you would like to change(empty if none): ")
    if userinput != '':
        if userinput in ['1','2','3']:
            settings[int(userinput) - 1] = not settings[int(userinput) - 1]
            printSettings()

        

    


        
    
def showRules():
    print("The goal of this game is to guess whether the next card to be shown from the deck will be higher or lower than the current card thats shown. After each guess the card will be revealed.")
    global rounds
    while not (rounds > 0 and rounds < 20):
        rounds = int(input("How many rounds would you like to play? (1-20) ")) 
    printSettings()
    


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






    
rounds = 0
deck = Deck(settings[0], settings[1], settings[2])
print("Welcome to Daniel's Higher/Lower Game!")
time.sleep(0.5)
showRules()
print("Let's go!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

points = 0

deck.shuffle()
last_value = deck.getTopCard().value
deck.showTopCard()


    



for i in range(rounds):
    playRound(i+1)

endGame()
# showDeck()
            

