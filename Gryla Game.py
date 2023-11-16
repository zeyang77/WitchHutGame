import os.path
import sys
import random

scene = 'gscenario.txt'
settingOff = 'gsettingoff.txt'
encounter = 'gencounter.txt'
enter = 'enterhut.txt'
table = 'gtable.txt'
kitchen = 'gkitchen.txt'
bedroom = 'gbedroom.txt'
meetGryla = 'ggryla.txt'

infile1 = open(scene, 'r')
infile2 = open(settingOff, 'r')
infile3 = open(encounter, 'r')
infile4 = open(enter, 'r')
infile5 = open(table, 'r')
infile6 = open(kitchen, 'r')
infile7 = open(bedroom, 'r')
infile8 = open(meetGryla, 'r')

readFile1 = infile1.read()
readFile2 = infile2.read()
readFile3 = infile3.read()
readFile4 = infile4.read()
readFile5 = infile5.read()
readFile6 = infile6.read()
readFile7 = infile7.read()
readFile8 = infile8.read()

#scenario and setting off texts
print(readFile1 + '\n')
print(readFile2 + '\n')

havingLooked = False
print('--Look inside?\n')
print('[OPTIONS]: "yes"  "no"  "leave"\n')
while havingLooked != True:
    
    option1 = input('[Your move]: ')

    #peers into window
    if option1 == 'yes':
        havingLooked = True
        print('\n' + readFile3 + '\n')
        input('[Press Enter to continue]')
        
    elif option1 == 'no':
        havingLooked = False
        print('\nPlease look.\n')
        input('[Press Enter to continue]\n')
        
    elif option1 == 'leave':
        print('\n[GAME OVER]')
        sys.exit()

    else:
        print('\n[PLEASE ENTER]: "yes"  "no"  "leave"')
        input('\n[Press Enter to continue]\n')

enteredHut = False
print('\n--Go inside the hut?\n')
print('[OPTIONS]: "yes"  "no"  "leave"\n')
while enteredHut != True:
    
    option2 = input('[Your move]: ')

    #enters hut here
    if option2 == 'yes':
        enteredHut = True
        print('\n' + readFile4 + '\n')
        input('[Press Enter to continue]')
        
    elif option2 == 'no':
        enteredHut = False
        print('\nYou must.')
        input('\n[Press Enter to continue]\n')

    #can flee if player chooses    
    elif option2 == 'leave':
        print('\n[GAME OVER]')
        sys.exit()

    else:
        print('\n[PLEASE ENTER]: "yes"  "no"  "leave"\n')
        input('[Press Enter to continue]\n')

print('\n--There is an object on the table.\n')
print('[OPTIONS]: "search"  "skip"  "leave"\n')

tableSearched = False
amulet = False

while tableSearched != True:
    
    option3 = input('[Your move]: ')

    #can search table and acquire item
    if option3 == 'search':
        tableSearched = True
        amulet = True
        print('\n' + readFile5 + '\n')
        input('[Press Enter to continue]')

    #can choose to skip and not get anything    
    elif option3 == 'skip':
        tableSearched = True
        amulet = False
        print('\n[You moved on].\n')
        input('[Press Enter to continue]')
        
    elif option3 == 'leave':
        print('\n[GAME OVER]')
        sys.exit()

    else:
        print('\n[PLEASE ENTER]: "search"  "skip"  "leave"\n')
        input('[Press Enter to continue]\n')

print('\n--Where to next?\n')
print('[OPTIONS]: "left"  "right"  "leave"\n')

kitchenEntered = False
bedroomEntered = False

grylaDefeated = False
chestUnlocked = False

while kitchenEntered != True:

    option4 = input('[Your move]: ')

    #can enter bedroom + text
    if option4 == 'right':
        kitchenEntered = False
        bedroomEntered= True
        print('\n' + readFile7 + '\n')
        input('[Press Enter to continue]\n')

        print('--What will you do now?\n')
        print('[OPTIONS]: "open"  "back"\n')

        while bedroomEntered == True and chestUnlocked != True:

            bedOption = input('[Your move]: ')

            if grylaDefeated == False and bedOption == 'open':
                print('\n[The chest is locked.]\n')
                input('[Press Enter to continue]\n')

            elif grylaDefeated == True and bedOption == 'open':
                print('\n[YOU WIN!]')
                sys.exit()

            #can search bedroom
            elif bedOption == 'search':
                print('\n[You search the bedroom but find nothing].\n')
                input('[Press Enter to continue]\n')

            #ability to leave bedroom
            elif bedOption == 'back':
                bedroomEntered = False
                print('\n[You leave the bedroom(4).]\n')
                input('[Press Enter to continue]\n')
                print('[OPTIONS]: "left"  "right"  "leave"\n')

            else:
                print('\n[PLEASE ENTER]: "enter"  "back"  "search"\n')
                input('[Press Enter to continue]\n')

    #can enter kitchen + text    
    elif option4 == 'left':
        kitchenEntered = True
        bedroomEntered = False
        print('\n' + readFile6 + '\n')
        input('[Press Enter to continue]')
        
        print('\n--What will you do now?')
        print('\n[OPTIONS]: "enter"  "search"  "back"\n')

        cellarEntered = False
        
        while kitchenEntered == True and cellarEntered != True:
            
            option5 = input('[Your move]: ')

            #can enter cellar to meet Gryla
            if option5 == 'enter':
                cellarEntered = True
                print('\n' + readFile8 + '\n')
                
                print('--What will you do now?\n')
                print('[OPTIONS]: "attack"  "persuade"  "consider"  "back"\n')
                print('[REQUIREMENTS]: Attack - 12 | Persuade - higher | Consider - higher\n')

                while cellarEntered == True and grylaDefeated != True:
                    
                    encounterOption = input('[Your move]: ')
                
                    if encounterOption == 'attack':
                        print(' ')
                        #dice rolling time
                        diceRoll = int(1)
                        diceSides = int(20)

                        for i in range(diceRoll):
                            randomDice = random.randrange(diceSides)+1
                            print(randomDice)
                            if randomDice == 20:
                                print('\n[CRITICAL HIT!]\n')
                            if randomDice == 1:
                                print('\n[CRITICAL FAIL!]\n')

                        if randomDice >= 12:
                            print('[You\'ve struck a blow!]\n')
                        if randomDice == 20:
                            print('[Enemy Slain!]')
                        #UNFINISHED

            #can search the kitchen    
            elif option5 == 'search':
                print('\n[You search the kitchen but find nothing].\n')
                input('[Press Enter to continue]\n')

            elif option5 == 'back':
                kitchenEntered = False
                print('\n[You leave the kitchen(3)]\n')
                input('[Press Enter to continue]\n')
                print('[OPTIONS]: "left"  "right"  "leave"\n')
                #ability to leave kitchen
                
            else:
                print('\n[PLEASE ENTER]: "enter"  "back"  "search"\n')
                input('[Press Enter to continue]\n')

    elif option4 == 'leave':
        print('\n[GAME OVER]')
        sys.exit()

    else:
        print('\n[PLEASE ENTER]: "left"  "right"  "leave"\n')
        input('[Press Enter to continue]\n')

#I was unable to finish the game in time.
        
#I got to the section where the player can decide on how to deal with Gryla.
        
#I spend a lot of time going over and polishing the player's ability to
#navigate around in the hut.
        
#There were a few road blocks that I struggled with such as figuring out
#how the player can move backwards, or how to keep track of items/actions like the amulet,
#as well as the dice rolling.

#Even though this project is so much larger than anything we have done so far,
#I had a blast figuring things out and how I went about the logic of my code.

#All I needed to do left was finish the dice rolling options to deal with Gryla, then
#allow the player to go back and open the chest to win the game.

#https://github.com/zeyang77/WitchHutGame
