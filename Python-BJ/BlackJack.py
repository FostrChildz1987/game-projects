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

def betLoop(payroll):
    global bet
    betLoop = True
    while betLoop:
        try:
            print("You have:", payroll, "chips")
            bet = float(input("Enter your bet amount: "))
        except:
            print("Please enter a valid number!")
        else:
            if(bet <= payroll):
                betLoop = False
            else:
                print("You must enter a valid bet!")

def choiceLoop():
    global choice
    choiceLoop = True
    while choiceLoop:
        choice = input("Would you like to (h)it or (s)tand?: ")
        if(choice == "h"):
            choiceLoop = False
        elif(choice == "s"):
            choiceLoop = False
        else:
            print("Enter a valid value!")

def playerDraw():
    pass

def dealerTurn():
    pass

def dealerDraw():
    pass

def win():
    pass

def loss():
    pass







def initializeGame():
    global diff
    global payroll

    print("Welcome to Bigus Dickus Blackjack!")
    print()
    print("Standard Rules - Blackjack Pays 3 to 5 - No Insurance")
    print()
    print("Get as close to 21 as you can without going over!")
    print("Royal cards (King, Queen, Jack) are worth 10 points!")
    print("Aces are worth 1 or 11 points!")
    print("All other cards are worth face value!")
    print("Earn 100,000 Chips to win!")
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
    
    if(diff == "e"):
        payroll = 20000.0
    elif(diff == "m"):
        payroll = 10000.0
    elif(diff == "h"):
        payroll = 5000.0

def mainGame(difficulty):
    betLoop(payroll)
    print("You have bet:", bet, "chips!\n")

    d1 = Card()
    d2 = Card()
    p1 = Card()
    p2 = Card()
    pList = [p1.num, p2.num]
    dList = [d1.num, d2.num]

    print("The dealer's face card is:", d1.name())

    print("Your cards are:", p1.name(), "and", p2.name(), "Total:", str(sum(pList)))
    print()
    
    choiceLoop()
    if(choice == "h"):
        playerDraw()
    elif(choice == "s"):
        dealerTurn()

    