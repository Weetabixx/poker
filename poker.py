#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Poker
#
# Author:      Robin
#
# Created:     29/11/2014
# Copyright:   (c) Robin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random


def main(): # i will put my code here
    def setdeck(): # sets/resets deck
        deck = ["2-Diamonds","3-Diamonds","4-Diamonds","5-Diamonds","6-Diamonds","7-Diamonds","8-Diamonds","9-Diamonds","10-Diamonds","J-Diamonds","Q-Diamonds","K-Diamonds","A-Diamonds","2-Hearts","3-Hearts","4-Hearts","5-Hearts","6-Hearts","7-Hearts","8-Hearts","9-Hearts","10-Hearts","J-Hearts","Q-Hearts","K-Hearts","A-Hearts","2-Clubs","3-Clubs","4-Clubs","5-Clubs","6-Clubs","7-Clubs","8-Clubs","9-Clubs","10-Clubs","J-Clubs","Q-Clubs","K-Clubs","A-Clubs","2-Spades","3-Spades","4-Spades","5-Spades","6-Spades","7-Spades","8-Spades","9-Spades","10-Spades","J-Spades","Q-Spades","K-Spades","A-Spades"]
        return deck

    def setmenu(): #displays menu and gets input
        valid = ["1","2","3","4","5","6","7","9"]
        print ("--------------------------------------------")
        print ("MENU:")
        print ("type numbers 1-7 depending on how many players or 9 to end")
        print ("--------------------------------------------")
        choice = str(input())
        if choice in valid:  # makes sure that the input is valid
            return int(choice)
        else :
            print ("that number isn't valid, please choose again")
            return setmenu()

    def chooserandmon(bacon): # will choose a randomn card and remove it
        c = random.choice(bacon)
        bacon.remove(c)
        return c

    def deal(hand, cards): # this will deal x cards
        global deck
        for i in range(0, cards):
            hand.append(chooserandmon(deck))
        return hand

    def round():  # this will be how a round will happen
        global hands
        global players
        players = len(chips)
        for i in range(0,players):
            deal(hands[i], 2)
        blind()
        bet()
        deal(table, 3)
        bet()
        deal(table, 1)
        bet()
        deal(table, 1)
        bet()
        award()
        newround()
        removeplayer()

    def equalbets(): # will test if bets are equal
        largest = 0
        for i in playerbets:
                    if i > largest:
                        largest = i
        well = True
        for h in names:
            index = int(names.index(h))
            if hands[index] != [] and (playerbets[index] != largest) and (chips[index] != 0) :
                well = False
        return well

    def bet(): # will iterate through each player and make bets
        global players
        betpos = blindpos
        for i in range(betpos,players):
            bet1(i)
        for i in range(0,betpos):
            bet1(i)
        while equalbets() == False:
            bet1(betpos)
            if betpos < players:
                betpos += 1
            else :
                betpos = 0

    def bet1(betpos): # makes bets, call and folds
        global pot
        global hands
        global playerbets
        global chips
        allin = False
        turn = True
        print ("type anything to start your turn, " + names[betpos]) # list error index out of range
        nothing = input()
        display(hands[betpos])
        print ("Pot is: " + str(pot))
        print ("you have bet: " + str(playerbets[betpos]))
        print ("your chips: " + str(chips[betpos]))
        print ("everyone's bets:")
        for i in names:
            if i != names[betpos]:
                nameindx = int(names.index(i))
                print (i + " has bet " + str(playerbets[nameindx]) + " chips")
                print ("and has " + str(chips[nameindx]) + " chips left")
                if hands[nameindx] == []:
                    print (",but has folded")
        largest = 0
        for i in playerbets:
            if i > largest:
                largest = i
        if playerbets[betpos] + chips[betpos] < largest + 1:
            allin = True
        else :
            allin = False
        if hands[betpos] == []:
            print ("you have already folded, next players turn")
        elif chips[betpos] < 1:
            print ("you are all in already, next players turn")
        else :
            while turn:
                print ("to call/all in type call, to fold type fold or raise by typing how much you would like to bet")
                letters = False
                response = input()
                abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                for i in str(response):
                    if i in abc:
                        letters = True
                if str(response) == "call":
                    if allin:
                        pot += chips[betpos]
                        playerbets[betpos] += chips[betpos]
                        chips[betpos] = 0
                        turn = False
                    else :
                        tocall = largest - playerbets[betpos]
                        pot += tocall
                        playerbets[betpos] += tocall
                        chips[betpos] -= tocall
                        turn = False
                elif str(response) == "fold": # removes hand if fold
                    hands[betpos] = []
                    turn = False
                elif letters or str(response) == "":
                    print ("that is not a valid value")
                elif int(response) < chips[betpos] + 1 and int(response) + 1 > largest - playerbets[betpos] : #cheks to see if bet is larger than call and less than chips
                    pot += int(response)
                    playerbets[betpos] += int(response)
                    chips[betpos] -= int(response)
                    turn = False
                else :
                    print ("that value was not valid")
            print ("type anything to end your turn")
            nothing = input()
        for i in range(0,50):
            print ("-")
        print ("end of " + names[betpos] + "'s turn")


    def award(): # in progress
        global pot
        global chips
        lookingforwinner = True
        print ("the table is: ")
        print (table)
        print ("the player hands are: ")
        for i in names:
            index = int(names.index(i))
            if hands[index] != []:
                print (i + "-- " + str(hands[index][0]) + " and " + str(hands[index][1]))
        while lookingforwinner:
            print ("who won that round?")
            winner = str(input())
            for i in names:
                if i == winner:
                    lookingforwinner = False
                    index = int(names.index(i))
                    chips[index] += pot
                    pot = 0
        print ("everyones chips:")
        for i in names:
            index = int(names.index(i))
            print (i + "--" + str(chips[index]))

    def display(player):
        print ("your hand is: ")
        print (player)
        print ("the table is: ")
        print (table)
    def blind(): # places the blinds and changes its position
        global blindpos
        global playerbets
        global pot
        global chips
        bigpos = blindpos
        if blindpos == 0:
            smallpos = -1
            for i in names:
                smallpos += 1
        else :
            smallpos = blindpos - 1
        pot = smallblind + bigblind
        chips[bigpos] = chips[bigpos] - bigblind
        playerbets[bigpos] = bigblind
        chips[smallpos] = chips[smallpos] - smallblind
        playerbets[smallpos] = smallblind
        if blindpos < len(chips):
            blindpos += 1
        else :
            blindpos = 0

    def getnames(): # this sets up the game names and chips per player and their bets
        global bigblind
        global smallblind
        for i in range(0,menu):
            print ("what is player%s's name?" % (i+1))
            name = str(input())
            names.append(name)
        print ("the players are : ")
        for i in names:
            print ("- " + i)
        print ("how many chips per player?")
        chips_tot = int(input())
        for i in range(0,menu):
            chips[i] += chips_tot
            playerbets.append(0)
        nums = [6,5,4,3,2,1,0]
        for i in nums:
            if chips[i] < 1:
                hands.pop(i)
                chips.pop(i)
        bigblind = int(chips_tot / 50)
        smallblind = int(bigblind / 2)
        print ("big is: " + str(bigblind))
        print ("small is: " + str(smallblind))

    def removeplayer():
        global hands
        global chips
        global names
        global places
        global playerbets
        global blindpos
        for i in chips:
            if i < 1:
                index = chips.index(i)
                hands.pop(index)
                chips.remove(i)
                places.insert(0,names[index])
                print (names[index] + " is out of chips and no longer playing")
                names.pop(index)
                playerbets.pop(index)
                if not blindpos < len(chips):
                    blindpos = 0

    def newround():
        global players
        global hands
        global playerbets
        global pot
        global table
        for i in range(0,players):
            hands[i] = []
            playerbets[i] = 0
        table = []
        pot = 0

    def game():
        global menu
        global places
        global players
        global chips
        menu = setmenu()
        players = menu
        if menu == 9:
            exit()
        getnames()
        while players > 1:
            round()
            players = len(chips)
        print ("the places are as follows :")
        print ("1st --" + names[0])
        p = 2
        for name in places:
            if p == 2:
                print ("2nd --" + name)
            elif p == 3:
                print ("3rd --" + name)
            else :
                print (str(p) + "th --" + name)
            p = p  + 1
        print ("--------------------------------------------------")
        print ("            THE END OF THE GAME")
        print ("--------------------------------------------------")





    global players
    players = 0
    global bigblind
    bigblind = 0
    global smallblind
    smallblind = 0
    global blindpos
    blindpos = 0
    global pot
    pot = 0
    chips_tot = 0
    global chips
    chips = [0,0,0,0,0,0,0]
    largest = 0
    global hands
    hands = [[],[],[],[],[],[],[]]
    global table
    table = []
    global names
    names = []
    global playerbets
    playerbets = [0,0,0,0,0,0,0]
    global deck
    deck = setdeck()
    global menu
    menu = 0
    global places
    places = []
    game()





if __name__ == '__main__':
    main()
