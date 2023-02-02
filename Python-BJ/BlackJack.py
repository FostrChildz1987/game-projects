from random import *
import turtle as t

cardTypes = (" of Clubs", " of Spades", " of Hearts", " of Diamonds")

def setRoyal(num):
    if(num == 11):
        royal = "Jack"
    elif(num == 12):
        royal = "Queen"
    elif(num == 13):
        royal == "King"
    else:
        royal = ""
    return royal

class Card:
    def __init__(self):
        self.isAce = False
        self.royal = ""
        self.isRoyal = False
        
        self.num = randint(2, 14)
        if(self.num > 10 and self.num != 14):
            self.royal = setRoyal(self.num)
            self.isRoyal = True
            self.num = 10
        elif(self.num == 14):
            self.isAce = True
            self.num = 1
        
        self.cardType = cardTypes[randint(0,3)]

    def name(self):
        if(self.isRoyal == True):
            cardName = self.royal + self.cardType
        elif(self.isAce == True):
            cardName = "Ace" + self.cardType
        else:
            cardName = str(self.num) + self.cardType
        return cardName


def initializeGame():
    global diff

    print("Welcome to Bigus Dickus Blackjack!")
    print()
    print("Standard Rules - Blackjack Pays 3 to 5 - No Insurance")
    print()
    print("Get as close to 21 as you can without going over!")
    print("Royal cards (King, Queen, Jack) are worth 10 points!")
    print("Aces are worth 1 or 11 points!")
    print("All other cards are worth face value!")
    print()
    
    loop = True
    while loop:
        print("Select difficulty to begin [(e), (m), (h)] (Difficulty determines starting payroll):")
        diff = input()
        if(diff == "e" or diff == "m" or diff == "h"):
            loop = False
        else:
            print("Please enter a valid input!")
            print()

def mainGame(difficulty)