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
    printSettings()
    
deck = Deck(settings[0], settings[1], settings[2])


def showDeck():
    for card in deck.deck:
        print(f"{card.number} of {card.suit}")


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




deck.shuffle()
showDeck()
            

