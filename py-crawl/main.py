import random

from shopping import *

# i wrote this for about 23 hours only one thing was borrowed and that was the art because im bad at that lol but i
# hope you like my project as of writing this i am struggling to perfect comments because of how much code there is
# but i will try i have failed to find bugs yet but let me know after this i shall continue adding support to this
# game and updating over on my personal github yes i know this is quite simple in terms of full fledged games but all
# ive had time for as of right now
run = True  # This needs to be true to run
playertypes = ('warrior', 'mage', 'archer')
yestrue = ('yes', 'Yes', 'YES', 'Y', 'y', 'yea', 'Yea', 'YEA')
notrue = ('no', 'NO', 'No', 'N', 'n', 'na', 'Na', 'NA')
checktrue = (yestrue + notrue)
rounds = 0
coins = 0

def chest():
    global playerhealth, playerspeed, playerdamage
    chest = random.randint(1, 4)  # You have a 3 in four chance to get a chest
    if chest == 1:  # This is the worst type of chest
        print('!CHEST ALERT!')
        print('Lesser chest')
        print()
        if image in yestrue:
            print('⠀⠀⠀╔══════╗')
            print('╔══╝⠀⠀⠀⫯⠀⠀╚══╗')
            print('╠════════════╣')
            print('║⠀⠀⠀Lesser⠀⠀⠀║')
            print('║⠀⠀⠀Chest⠀⠀⠀⠀║')
            print('╚════════════╝')
            print()
        chestout = random.randint(1, 3)
        check2 = ''
        if chestout == 1:
            print('You got a lesser health potion.')
            print('This will increase your maxamum health points by 2.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerhealth = playerhealth + 2
        elif chestout == 2:
            print('You got a lesser sword increase.')
            print('This will increase your attack points by 2.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerdamage = playerdamage + 2

        elif chestout == 3:
            print('You got a pair of lesser speed boots.')
            print('This wil increase your speed points by 2.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerspeed = playerspeed + 2
        # medium chest code below
    elif chest == 2:  # This is the medium chest.
        print('!CHEST ALERT!')
        print('Medium chest')
        print()
        if image in yestrue:
            print('⠀⠀⠀╔══════╗')
            print('╔══╝⠀⠀⠀⫯⠀⠀╚══╗')
            print('╠════════════╣')
            print('║⠀⠀⠀Medium⠀⠀⠀║')
            print('║⠀⠀⠀Chest⠀⠀⠀⠀║')
            print('╚════════════╝')
            print()
        chestout = random.randint(1, 3)
        if chestout == 1:
            print('You got a medium health potion.')
            print('This will increase your maxamum health points by 3.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerhealth = playerhealth + 3

        if chestout == 2:
            print('You got a medium sword increase.')
            print('This will increase your attack points by 3.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerdamage = playerdamage + 3

        if chestout == 3:
            print('You got a pair of medium speed boots.')
            print('This wil increase your speed points by 3.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerspeed = playerspeed + 3
    # chest code starts here i beleive lol idk anymore 🤣
    elif chest == 3:  # This is the best type if chest
        print('!CHEST ALERT!')
        print('Great chest')
        print()
        if image in yestrue:
            print('⠀⠀⠀╔══════╗')
            print('╔══╝⠀⠀⠀⫯⠀⠀╚══╗')
            print('╠════════════╣')
            print('║⠀⠀Greater⠀⠀⠀║')
            print('║⠀⠀⠀Chest⠀⠀⠀⠀║')
            print('╚════════════╝')
            print()
        chestout = random.randint(1, 3)
        if chestout == 1:
            print('You got a greater health potion.')
            print('This will increase your maxamum health points by 4.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerhealth = playerhealth + 4

        if chestout == 2:
            print('You got a greater sword increase.')
            print('This will increase your attack points by 4.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerdamage = playerdamage + 4

        if chestout == 3:
            print('You got a pair of greater speed boots.')
            print('This wil increase your speed points by 4.')
            check = input('Do you wish to use it? ')
            while check not in checktrue:
                print('Incorect input')
                check = input('Do you wish to use it? ')
            if check in notrue:
                print('Are you sure? This will mean that you loose this upgrade.')
                check2 = input('Do you want to use it? ')
                while check2 not in checktrue:
                    print('Incorrect input')
                    check2 = input('Do you want to use it? ')
            if check in yestrue or check2 in yestrue:
                playerspeed = playerspeed + 4
    else:  # The message thats sent when you dont get a chest
        print('Sadly you got no chest this time, maybe next time you can get lucky.')


def playerattack():  # Creating the player attck script
    global enemyhealth
    speed = random.randint(1, 20)
    if enemyspeed == speed or enemyspeed > speed:
        print('The enemy dodged your attack with its speed.')
    else:
        damage = random.randint(1, 20)
        if playerdamage == damage or playerdamage > damage:
            print('CRITICAL HIT!')
            print('You deal double damage!')
            enemyhealth = enemyhealth - 2
        else:
            print('You dealt your normal amount of damage.')
            enemyhealth = enemyhealth - 1
    if enemyhealth < 0:
        enemyhealth = 0
    print('The enemy now has', enemyhealth, 'health left.')


def enemyattack():  # Creating the enemy attack script
    global ingamehealth
    speed = random.randint(1, 20)
    if playerspeed == speed or playerspeed > speed:
        print('You dodged the enemy attack with your speed.')
    else:
        damage = random.randint(1, 20)
        if enemydamage == damage or enemydamage > damage:
            print('CRITICAL HIT!')
            print('The enemy deals double damage.')
            ingamehealth = ingamehealth - 2
        else:
            print('The enemy dealt its normal amount of damage.')
            ingamehealth = ingamehealth - 1
    if ingamehealth < 0:
        ingamehealth = 0
    print('You now have', ingamehealth, 'health left.')


def create_enemy():  # Creation of the enemy here
    global enemyhealth, enemyspeed, enemydamage, enemytype, elitecheck
    enemy = random.randint(1, 2)  # Type of enemy
    if enemy == 1:  # Skeleton
        enemybh = 3  # Base health of 4
        enemybd = 5  # Base damage of 6
        enemybs = 5  # Base speed of 6
        enemyclass = random.randint(1, 3)
        if enemyclass == 1:  # Warrior (+1, +1, 0)
            enemyhealth = enemybh + 1
            enemydamage = enemybd + 1
            enemyspeed = enemybs
            enemytype = 'Skeleton Warrior'
        if enemyclass == 2:  # Mage (0, +2, 0)
            enemyhealth = enemybh
            enemydamage = enemybd + 2
            enemyspeed = enemybs
            enemytype = 'Skeleton Mage'
        if enemyclass == 3:  # Archer (0, 0, +2)
            enemyhealth = enemybh
            enemydamage = enemybd
            enemyspeed = enemybs + 2
            enemytype = 'Skeleton Archer'
    if enemy == 2:  # Zombie
        enemybh = 5  # Base health of 6
        enemybd = 5  # Base damage of 6
        enemybs = 3  # Base speed of 4
        enemyclass = random.randint(1, 3)
        if enemyclass == 1:  # Warrior (+1, +1, 0)
            enemyhealth = enemybh + 1
            enemydamage = enemybd + 1
            enemyspeed = enemybs
            enemytype = 'Zombie Warrior'
        if enemyclass == 2:  # Mage (0, +2, 0)
            enemyhealth = enemybh
            enemydamage = enemybd + 2
            enemyspeed = enemybs
            enemytype = 'Zombie Mage'
        if enemyclass == 3:  # Archer (0, 0, +2)
            enemyhealth = enemybh
            enemydamage = enemybd
            enemyspeed = enemybs + 2
            enemytype = 'Zombie Archer'
    elitecheck = random.randint(1, 75)
    if playerhealth > 14:
        elitecheck = elitecheck + 6
    elif playerhealth > 9:
        elitecheck = elitecheck + 3
    if playerdamage > 14:
        elitecheck = elitecheck + 6
    elif playerdamage > 9:
        elitecheck = elitecheck + 3
    if playerspeed > 15:
        elitecheck = elitecheck + 6
    elif playerspeed > 9:
        elitecheck = elitecheck + 3
    if elitecheck > 70:
        enemyhealth = enemyhealth + 4
        enemydamage = enemydamage + 4
        enemyspeed = enemyspeed + 4
        elitecheck = True
    else:
        elitecheck = False


def balancestats():
    global playerhealth, playerspeed, playerdamage
    if playerhealth > 15:
        print()
        print('Your health has gone above 15.')
        print('For balancing reasons we have to keep it at 15.')
        playerhealth = 15
    if playerdamage > 10:
        print()
        print('Your damage has gone above 10.')
        print('For balancing reasons we have to keep it at 10.')
        playerdamage = 10
    if playerspeed > 10:
        print()
        print('Your speed has gone above 10.')
        print('For balancing reasons we have to keep it at 10.')
        playerspeed = 10


# intro text is here and explanation
print('Welcome to a basic text adventure')
print('This text adventure is a dungeon crawler game.')
print()
print('You will get a choice of three different characters, a warrior, a mage, and an archer.')
print('Each of these classes has set stats and each of these stats has something that it does.')
print('Your health is the number of hits you can take before you die.')
print('Your damage is how often you can get a critical hit.')
print("Your speed is how often you will dodge the enemy's attck")
print('You can increase these stats by getting items out of chests that you get from the end of each level.')
print('The stats are capped off at 10 exept for health which caps at 15 to make the game fair.')
print("The dungeon is randomised so don't try to cheat.")
print()
image = input('Do you wish to have some low level graphics in the game? ')
while image not in checktrue:
    print('Incorrect input.')
    image = input('Do you wish to have some low level graphics in the game? ')
print()
print('Great, have Fun!')
print()

while run:  # Actual game loop
    playertype = input('What class do you wish to be? warrior, mage, or archer. ')  # Asking what class they want to be
    while playertype not in playertypes:
        print('Incorrect input')
        playertype = input('What class do you wish to be? warrior, mage, or archer. ')
    playing = True
    while playing:
        print('You are now the', playertype,
              'class.')  # Telling them what that class does and letting them choose again if they want
        if playertype == 'warrior':
            print('You now have 8 health points.')
            playerhealth = 8
            print('You now have 8 attack points.')
            playerdamage = 8
            print('You now have 4 speed points.')
            playerspeed = 4
        if playertype == 'mage':
            print('You now have 4 health points.')
            playerhealth = 4
            print('You now have 10 attack points.')
            playerdamage = 10
            print('You now have 6 speed points.')
            playerspeed = 6
        if playertype == 'archer':
            print('You now have 6 health points.')
            playerhealth = 6
            print('You now have 6 attack points.')
            playerdamage = 6
            print('You now have 8 speed points.')
            playerspeed = 8
        check = input('Do you wish to continue? ')
        while check not in checktrue:
            print('Incorrect input')
            check = input('Do you wish to continue? ')
        if check in notrue:
            print('Ok')
            playing = False
            continue
        print()
        print('Great!')
        print('Now we can start the game.')
        ingame = True
        while ingame:  # Battling the enemys in here
            ingamehealth = playerhealth
            print()
            if image in yestrue:
                print('⠀⠀╔═══╗⠀⠀⠀⠀⠀⠀╔═══╗⠀⠀⠀⠀⠀⠀╔═══╗⠀⠀      or 4 for shop')
                print('╔═╝⠀⠀⠀╚═╗⠀⠀╔═╝⠀⠀⠀╚═╗⠀⠀╔═╝⠀⠀⠀╚═╗')
                print('║⠀Door⠀⠀║⠀⠀║⠀Door⠀⠀║⠀⠀║⠀Door⠀⠀║')
                print('║⠀⠀⠀1⠀⠀⠀║⠀⠀║⠀⠀⠀2⠀⠀⠀║⠀⠀║⠀⠀⠀3⠀⠀⠀║')
                print('║⠀⠀⠀⠀⠀⬝⠀║⠀⠀║⠀⠀⠀⠀⠀⬝⠀║⠀⠀║⠀⠀⠀⠀⠀⬝⠀║')
                print('║⠀⠀⠀⠀⠀⠀⠀║⠀⠀║⠀⠀⠀⠀⠀⠀⠀║⠀⠀║⠀⠀⠀⠀⠀⠀⠀║')
                print('║⠀⠀⠀⠀⠀⠀⠀║⠀⠀║⠀⠀⠀⠀⠀⠀⠀║⠀⠀║⠀⠀⠀⠀⠀⠀⠀║')
                print('╚═══════╝⠀⠀╚═══════╝⠀⠀╚═══════╝')
                print()
            door = input('What door do you wish to go through? 1, 2, 3 or 4? ')
            while door == ('4'):
                shop()
                break

            while door not in ('1', '2', '3', '4'):
                print('Incorrect input')
                door = input('What door do you wish to go through? 1, 2 or 3? ')
            create_enemy()  # Creates your enemy
            print('You are now fighting a', enemytype + '.')
            if elitecheck:
                print(
                    'This is an Elite enemy, it has buffed stats and attacks twice, it will be harder to kill. Good luck!')
            print()
            print('It has', enemyhealth, 'health points.')
            print('It has', enemydamage, 'attack points.')
            print('It has', enemyspeed, 'speed points.')
            print()
            print('You have', playerhealth, 'health points.')
            print('You have', playerdamage, 'attack points.')
            print('You have', playerspeed, 'speed points.')
            print()
            while enemyhealth > 0 and ingamehealth > 0:
                if ingamehealth > 0 and enemyhealth > 0:
                    playerattack()
                    input('Press enter to continue.')
                    print()
                if enemyhealth > 0 and ingamehealth > 0:
                    enemyattack()
                    input('Press enter to continue.')
                    print()
                doubleattack = random.randint(1, 3)
                if enemyhealth > 0 and ingamehealth > 0 and elitecheck and doubleattack == 1:
                    enemyattack()
                    input('Press enter to continue.')
                    print()
            if ingamehealth > 0:
                coinadd = random.randint(1, 20)
                coins = coins + coinadd
                print('you killed the ', enemytype, ' you now have',  coins,  " coins! ")
                print('so far you have passed ',  rounds,  " Rounds! ")
                input('press enter to continue: ')
                chest()
                balancestats()
                rounds = rounds + 1
            else:
                print("I'm sorry but you have died.")
                print("Whether this is due to bad luck or a bad decision I do not know.")
                print("You survived", rounds, "rounds. Good job!")
                retry = input('Do you want to try again to attempt to get better stats? ')
                while retry not in checktrue:
                    print('Incorrect input.')
                    retry = input('Do you want to try again to attempt to get better stats? ')
                if retry in yestrue:
                    print('Thats awesome!')
                    run = True
                    playing = False
                    ingame = False
                    continue
                elif retry in notrue:
                    print('Aww. Thats ok.')
                    print('We might see you again later.')
                    print('Bye for now and Thanks for playing!')
                    run = False
                    playing = False
                    ingame = False
                    continue
