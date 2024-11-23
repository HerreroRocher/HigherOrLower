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

        if self.number == "ace":
            self.value = 11 if aceIsEleven else 1
        elif self.number == "jack":
            self.value = 11 if kingsValueMorethan10 else 10
        elif self.number == "queen":
            self.value = 12 if kingsValueMorethan10 else 10
        elif self.number == "king":
            self.value = 13 if kingsValueMorethan10 else 10
        elif self.number == "joker":
            self.value = 0
        else:
            self.value = int(self.number)


class Deck:
    def __init__(self, jokers, aceIsEleven, kingsValueMorethan10):
        self.deck = []
        suits = ["hearts", "diamonds", "clubs", "spades"]
        for i in range(4):
            suit = suits[i]
            for i in range(1, 14):
                if i == 1:
                    number = "ace"
                elif i == 11:
                    number = "jack"
                elif i == 12:
                    number = "queen"
                elif i == 13:
                    number = "king"
                else:
                    number = i
                self.deck.append(Card(number, suit, aceIsEleven, kingsValueMorethan10))

        if jokers:
            self.deck.append(Card("joker", "red", aceIsEleven, kingsValueMorethan10))
            self.deck.append(Card("joker", "black", aceIsEleven, kingsValueMorethan10))

    def shuffle(self):
        random.shuffle(self.deck)

    def popTopCard(self):
        self.deck.pop(0)

    def getTopCard(self):
        return self.deck[0]


def change_cursor(event):
    canvas.config(cursor="hand2")  # Change cursor to a pointing hand


def reset_cursor(event):

    canvas.config(cursor="arrow")  # Reset cursor to default


def printSettings():
    setitingsStartWidth = 250
    global jokersTextOption, aceTextOption, kingsValueOption

    def makeSettingChanges():

        if settings[0]:
            canvas.itemconfig(jokersTextOption, text="There are jokers in the deck.")

        else:
            canvas.itemconfig(jokersTextOption, text="There are no jokers in the deck.")

        if settings[1]:
            canvas.itemconfig(aceTextOption, text="The value of the Ace is 11.")

        else:
            canvas.itemconfig(aceTextOption, text="The value of the Ace is 1.")

        if settings[2]:
            canvas.itemconfig(
                kingsValueOption,
                text="The Jack, Queen and King are of values 11, 12 and 13 respectively.",
            )

        else:
            canvas.itemconfig(
                kingsValueOption, text="The Jack, Queen and King all are of value 10."
            )

    def makeChanges(i):
        global settings
        settings[i] = not settings[i]
        makeSettingChanges()

    settingsIntro = canvas.create_text(
        25,
        200,
        text="Here are the current settings(click to change):",
        anchor="w",
        fill="white",
        font=font.Font(family="Arial", size=15, underline=True),
    )

    jokersTextOption = canvas.create_text(
        25,
        setitingsStartWidth,
        text="There are jokers in the deck.",
        anchor="w",
        fill="white",
        font=("Arial", 15),
    )
    aceTextOption = canvas.create_text(
        25,
        setitingsStartWidth + 50,
        text="The value of the Ace is 11.",
        anchor="w",
        fill="white",
        font=("Arial", 15),
    )
    kingsValueOption = canvas.create_text(
        25,
        setitingsStartWidth + 100,
        text="The Jack, Queen and King are of values 11, 12 and 13 respectively.",
        anchor="w",
        fill="white",
        font=("Arial", 15),
    )
    makeSettingChanges()

    canvas.tag_bind(jokersTextOption, "<Enter>", change_cursor)
    canvas.tag_bind(jokersTextOption, "<Leave>", reset_cursor)

    canvas.tag_bind(aceTextOption, "<Enter>", change_cursor)
    canvas.tag_bind(aceTextOption, "<Leave>", reset_cursor)

    canvas.tag_bind(kingsValueOption, "<Enter>", change_cursor)
    canvas.tag_bind(kingsValueOption, "<Leave>", reset_cursor)

    canvas.tag_bind(jokersTextOption, "<Button-1>", lambda event: makeChanges(0))

    canvas.tag_bind(aceTextOption, "<Button-1>", lambda event: makeChanges(1))

    canvas.tag_bind(kingsValueOption, "<Button-1>", lambda event: makeChanges(2))


def showRules():

    canvas.pack()
    introText = canvas.create_text(
        width / 2,
        25,
        text="Welcome to Daniel's Higher/Lower Game!",
        anchor="center",
        fill="white",
        font=("Arial", 20),
    )
    rulestext = canvas.create_text(
        width / 2,
        100,
        text="The goal of this game is to guess whether the next card to be shown from the deck will be higher or lower than the current card that's shown. After each guess the card will be revealed.",
        anchor="center",
        fill="white",
        font=("Arial", 15),
        width=width,
    )
    printSettings()


window = Tk()  # Creates instance of Tk class
width = 800
height = 600


def configureWindow(width, height):
    geometryInit = str(width) + "x" + str(height)
    window.configure(background="black")
    window.title("Higher or Lower")
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    xSpace = 0.5 * (screenWidth - width)
    ySpace = 0.5 * (screenHeight - height)
    window.geometry(geometryInit + "+" + str(int(xSpace)) + "+" + str(int(ySpace)))


configureWindow(width, height)

canvas = Canvas(window, bg="black", width=width, height=height)
settings = [
    True,
    True,
    True,
]  # First is True if we have jokers, second if the ace is value 11, third if kings value is not 13
points = 0
rounds = 0


def on_closing():
    window.destroy()
    exit()


def doBuildup():
    lets_go_text = canvas.create_text(
        width / 2,
        height / 2,
        text="Let's go!",
        anchor="center",
        fill="white",
        font=font.Font(family="Arial", size=150),
    )

    countdown = 3

    def update_countdown(i):
        if i == countdown + 1:
            canvas.after(
                1000, update_countdown, i - 2
            )  # Call update_countdown again after 1 second
        elif i == -1:
            canvas.delete(lets_go_text)
            global deck

            deck = Deck(settings[0], settings[1], settings[2])
            setUpGame(deck)

        else:
            canvas.itemconfig(lets_go_text, text=f"{i+1}")
            canvas.after(
                1000, update_countdown, i - 1
            )  # Call update_countdown again after 1 second

    update_countdown(countdown + 1)  # Start the countdown from 3


def getCardDimensions(max_height):
    global front_card_dimensions
    image = Image.open("Playing Cards/2_of_diamonds.png")
    original_width, original_height = image.size
    new_height = int(max_height)
    new_width = int((max_height / original_height) * original_width)

    front_card_dimensions = (new_width, new_height)


def create_back_card():
    global front_card_dimensions

    getCardDimensions(height * 5 / 8)

    const = 1.05
    image = Image.open("back_card.png")
    scaled_image = image.resize(
        (int(front_card_dimensions[0] * const), int(front_card_dimensions[1] * const)),
        Image.Resampling.LANCZOS,
    )
    back_card_photoimage = ImageTk.PhotoImage(scaled_image)
    window.back_card_photoimage = back_card_photoimage
    back_card = canvas.create_image(
        width * 2 / 3, height / 2, image=back_card_photoimage
    )

    height_error = 20

    return (front_card_dimensions[0], front_card_dimensions[1] - height_error), (
        width * 2 / 3,
        height / 2,
    )


def shuffle_deck():
    shuffle_text = canvas.create_text(
        width * 2 / 3,
        height / 2,
        text="Shuffling...",
        anchor="center",
        fill="gray",
        font=font.Font(family="Arial", size=20),
    )
    canvas.after(1000, lambda: (canvas.delete(shuffle_text), deck.shuffle()))


def present_card():

    top_card_inst = deck.getTopCard()
    if top_card_inst.number == "joker":
        top_card_image_path = "Playing Cards/" + top_card_inst.suit + "_joker" + ".png"
    else:
        top_card_image_path = (
            "Playing Cards/"
            + str(top_card_inst.number)
            + "_of_"
            + top_card_inst.suit
            + ".png"
        )
    image = Image.open(top_card_image_path)
    scaled_image = image.resize(front_card_dimensions, Image.Resampling.LANCZOS)
    top_card_image = ImageTk.PhotoImage(scaled_image)
    window.top_card_image = top_card_image
    top_card = canvas.create_image(width / 3, height / 2, image=top_card_image)


def flipCard():
    deck.popTopCard()
    present_card()


def updatePoints():
    global points, points_text
    points += 1
    canvas.itemconfig(points_text, text=f"Points: {points}")


def getEndGameText():
    if points / rounds >= 0.7:
        return "Congratulations, you played very well! Hope you enjoyed!"
    elif points / rounds >= 0.5:
        return "Okay...Decent score, maybe you can get more if you go again..."
    else:
        return "For your sake, I really hope you don't understand the rules."


def updateRound():
    global _round, round_text
    if _round != rounds:
        _round += 1
        canvas.itemconfig(round_text, text=f"Round: {_round}/{rounds}")
    else:
        canvas.create_text(
            width / 2,
            20,
            text=f"That's all of the rounds done! You got {points}/{rounds} points",
            font=("Arial", 20),
            fill="white",
            anchor="n",
        )
        canvas.delete(
            points_text,
            round_text,
            higher_button,
            lower_button,
            lower_text,
            higher_text,
        )
        reset_cursor(0)
        canvas.itemconfig(bottom_text, text=getEndGameText())


def handleGetJoker():
    flipCard()
    canvas.itemconfig(bottom_text, text="")
    updateRound()


def handleUserGuess(userGuessIsHigher):
    global points

    old_top_card = deck.getTopCard()
    flipCard()
    new_top_card = deck.getTopCard()

    if new_top_card.number == "joker":
        canvas.itemconfig(bottom_text, text="Joker means you lose this round!")
        canvas.after(5000, lambda: handleGetJoker())

    else:

        winner = (
            True
            if userGuessIsHigher
            and new_top_card.value > old_top_card.value
            or not userGuessIsHigher
            and new_top_card.value < old_top_card.value
            else False
        )
        drawer = True if new_top_card.value == old_top_card.value else False

        if drawer:
            canvas.itemconfig(bottom_text, text="You got lucky this round!")
            updatePoints()
        elif winner:
            canvas.itemconfig(bottom_text, text="Well done! You got it right!")
            updatePoints()
        else:
            canvas.itemconfig(bottom_text, text="Better luck next time!")

        updateRound()


def createHigherAndLowerButtons(back_card_location):
    global higher_button, lower_button, higher_text, lower_text
    button_x, button_y = back_card_location
    x_increase = 50
    y_decrease = 300
    y_offset = 70
    x1 = (button_x - back_card_dimensions_fixed[0] / 2) + x_increase / 2
    y1 = (button_y - back_card_dimensions_fixed[1] / 2) + (y_decrease / 2) - y_offset
    x2 = (button_x + back_card_dimensions_fixed[0] / 2) - x_increase / 2
    y2 = (button_y + back_card_dimensions_fixed[1] / 2) - (y_decrease / 2) - y_offset

    higher_button = canvas.create_rectangle(
        x1, y1, x2, y2, fill="black", outline="white"
    )

    higher_text = canvas.create_text(
        (x1 + x2) / 2, (y1 + y2) / 2, text="HIGHER", font=("Arial", 20), fill="white"
    )

    lower_y1 = y1 + 2 * y_offset
    lower_y2 = y2 + 2 * y_offset

    lower_button = canvas.create_rectangle(
        x1, lower_y1, x2, lower_y2, fill="black", outline="white"
    )

    lower_text = canvas.create_text(
        (x1 + x2) / 2,
        (lower_y1 + lower_y2) / 2,
        text="LOWER",
        font=("Arial", 20),
        fill="white",
    )

    canvas.tag_bind(higher_button, "<Button-1>", lambda event: handleUserGuess(True))
    canvas.tag_bind(lower_button, "<Button-1>", lambda event: handleUserGuess(False))

    canvas.tag_bind(higher_text, "<Button-1>", lambda event: handleUserGuess(True))
    canvas.tag_bind(lower_text, "<Button-1>", lambda event: handleUserGuess(False))

    canvas.tag_bind(higher_button, "<Enter>", change_cursor)
    canvas.tag_bind(lower_button, "<Enter>", change_cursor)

    canvas.tag_bind(higher_text, "<Enter>", change_cursor)
    canvas.tag_bind(lower_text, "<Enter>", change_cursor)

    canvas.tag_bind(higher_button, "<Leave>", reset_cursor)
    canvas.tag_bind(lower_button, "<Leave>", reset_cursor)

    canvas.tag_bind(higher_text, "<Leave>", reset_cursor)
    canvas.tag_bind(lower_text, "<Leave>", reset_cursor)


def continueExecution(deck, back_card_location):
    present_card()
    createHigherAndLowerButtons(back_card_location)


def create_bottom_text():
    global bottom_text
    bottom_text = canvas.create_text(
        width / 2, height * 11 / 12, text="", font=("Arial", 20), fill="white"
    )


def create_points_text():
    global points_text
    points_text = canvas.create_text(
        10, 10, text="Points: 0", anchor="nw", font=("Arial", 20), fill="white"
    )


def create_round_text():
    global round_text
    round_text = canvas.create_text(
        width - 10,
        10,
        text=f"Round: {_round}/{rounds}",
        anchor="ne",
        font=("Arial", 20),
        fill="white",
    )


def setUpGame(deck):
    global back_card_dimensions_fixed, rounds, _round
    rounds = 15
    _round = 1

    back_card_dimensions_fixed, back_card_location = create_back_card()
    create_bottom_text()
    create_points_text()
    create_round_text()
    shuffle_deck()
    canvas.after(1000, lambda: continueExecution(deck, back_card_location))

    canvas.pack()


def play():
    canvas.delete("all")
    doBuildup()


showRules()
window.protocol("WM_DELETE_WINDOW", on_closing)


def on_play(event):
    reset_cursor(event)
    play()


image = Image.open("play_button.png")

max_height = height / 4

original_width, original_height = image.size
new_height = int(max_height)
new_width = int((max_height / original_height) * original_width)

scaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

play_image = ImageTk.PhotoImage(scaled_image)
window.play_image = play_image

play_button = canvas.create_image(width / 2, height * 13 / 16, image=play_image)

canvas.tag_bind(play_button, "<Button-1>", on_play)
canvas.tag_bind(play_button, "<Enter>", change_cursor)
canvas.tag_bind(play_button, "<Leave>", reset_cursor)

canvas.pack()

window.mainloop()
