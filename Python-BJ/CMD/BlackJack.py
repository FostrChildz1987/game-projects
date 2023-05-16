from random import *
import turtle as t
from time import sleep

cardTypes = (" of Clubs", " of Spades", " of Hearts", " of Diamonds")
playerDict = {}
dealerDict = {}
turnCount = 0
survival = False

def setRoyal(num):
    if(num == 11):
        royal = "Jack"
    elif(num == 12):
        royal = "Queen"
    elif(num == 13):
        royal = "King"
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
            self.num = 11
        
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
    global turnCount

    choiceLoop = True
    while choiceLoop:
        sleep(0.5)
        choice = input("Would you like to (h)it or (s)tand (e to exit)?: ")
        if choice == "h":
            choiceLoop = False
        elif choice == "e":
            quit()
        elif choice == "s":
            choiceLoop = False
        else:
            print("Enter a valid value!")
    if choice == "h":
        turnCount += 1
        playerDraw(turnCount)
    elif choice == "s":
        dealerTurn()

def playerDraw(count):
    playerDict[count] = Card()
    pList.append(playerDict[count].num)

    if playerDict[count].isAce:
        if sum(pList) + 10 <= 21:
            playerDict[count].num = 11
            pList[-1] = 11
        else:
            playerDict[count].num = 1
            pList[-1] = 1

    sleep(0.5)
    print("You drew: " + playerDict[count].name())
    sleep(0.5)
    print("Your total is: " + str(sum(pList)))
    print()

    if sum(pList) > 21:
        # Check if there are Aces in the hand
        if 11 in pList:
            # Find the first Ace and change its value to 1
            index = pList.index(11)
            pList[index] = 1
            sleep(0.5)
            print("Changing Ace value to 1.")
            print("Your new total is: " + str(sum(pList)))
            print()
            choiceLoop()
        else:
            sleep(0.5)
            print("You went over 21! You Lose!")
            print()
            loss()
    else:
        choiceLoop()


def dealerTurn():
    global dealerCount
    dealerCount = 2
    
    sleep(0.5)
    print("Dealer's Turn!")
    sleep(0.5)
    print("Dealer's Cards are : " + dealerDict[1].name() + ", " + dealerDict[2].name() + " Total: " + str(sum(dList)))
    print()

    if(sum(dList) < 17):
        while (sum(dList) < 17):
            dealerCount += 1
            dealerDraw(dealerCount)
    if(sum(dList) > 21):
        sleep(0.5)
        print("Dealer went over 21! You Win!")
        print()
        win()
    else:
        checkWin()

def dealerDraw(count):
    dealerDict[count] = Card()
    dList.append(dealerDict[count].num)

    sleep(0.5)
    print("Dealer drew: " + dealerDict[count].name())
    sleep(0.5)
    print("Dealer's total is: " + str(sum(dList)))
    print()


def checkWin():
    if(sum(dList) < sum(pList)):
        sleep(0.5)
        print("You have the better hand! You Win!\n")
        print()
        win()
    elif(sum(dList) == sum(pList)):
        sleep(0.5)
        print("You both have an equal hand! Push!\n")
        print()
        push()
    else:
        sleep(0.5)
        print("The Dealer has the better hand! You Lose!\n")
        print()
        loss()

def win():
    global payroll
    if(len(pList) == 2 and sum(pList) == 21):
        payroll = payroll + payroll * 1.5
    else:
        payroll += bet
    
    if(payroll >= 100000 and survival == False):
        sleep(0.5)
        print("You survived! Most people are so ungrateful to be alive, but not you, not anymore!")
        print("You beat the House!")
        survivalMode = input("Enter Endless Mode (y/n): ")
        if(survivalMode == "n"):
            quit()
        else:
            survival = True
            mainGame()
    else:
        mainGame()

def loss():
    global payroll
    payroll -= bet
    if (payroll <= 0):
        sleep(0.5)
        print("You have went Bankrupt! GAME OVER!")
    else:
        mainGame()

def push():
    mainGame()


def initializeGame():
    global diff
    global payroll

    print("Welcome to Bigus Dickus Blackjack!")
    print()
    print("Standard Rules - Blackjack Pays 3 to 2 - No Insurance")
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
    mainGame()

def mainGame():
    global pList
    global dList
    global turnCount

    turnCount = 2

    betLoop(payroll)
    print("You have bet:", bet, "chips!\n")
    print()

    dealerDict[1] = Card()
    dealerDict[2] = Card()
    playerDict[1] = Card()
    playerDict[2] = Card()
    pList = [playerDict[1].num, playerDict[2].num]
    dList = [dealerDict[1].num, dealerDict[2].num]

    sleep(0.5)
    print("The Dealer's face card is:", dealerDict[1].name(), "Total:", dealerDict[1].num)
    print()

    sleep(0.5)
    print("Your cards are:", playerDict[1].name(), "and", playerDict[2].name(), "- Total:", str(sum(pList)))
    print()
    
    choiceLoop()


initializeGame()