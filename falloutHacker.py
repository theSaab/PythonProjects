from random import *

# this program mimics a fallout terminal you can hack
# lol
def help():
    print("The way it works is that you chose a dificulty, and you are presented ")
    print("with a cluster of characters.You must type an available word in those ")
    print("characters to guess the password It then presents you with a likeness ")
    print("counter,which is determined by how many letters of your guess are the ")
    print("same as the password.")

    print("for example:")
    print("    password = 'BATH'")
    print("    guess = 'DATA'")
    
    print("Likeness = 2")
    print("Because A and T are in the same spot.")
    print("Use this to eliminate words and gain access to the")
    print(" information in the terminal.")



# this is where you chose the dificulty of your guesser
def intro():
    print('Good luck hacking this terminal')
    difficulty = input('Choose your level with a number. \n1: Novice \n2: Advanced \n3: Expert \n4: Master\n')

    # will not allow letters or other numbers
    while difficulty not in ['1', '2', '3', '4'] or difficulty == '':
        print('Restart and chose a real difficulty.')
        difficulty = input('Choose your level. \n1: Novice \n2: Advanced \n3: Expert \n4: Master\n')

    # uses the difficulty for the interface part
    return int(difficulty)

# this is used to determine how similar your guess is to the real word
def likeness(password, input):
    # start a counter
    likeness = 0
    input = input.upper()

    # determines if characters are the same
    for i in range(len(input)-1):
        if input[i] == password[i]:
            likeness += 1
    # if the word is correct
    if likeness==len(password)-1:
        return True
    # if your guess is wrong
    else:
        print('Likeness = ' + str(likeness))
        return False

# this is the fake UI made for the game.
# made to mimic the terminal in fallout.
def interface(difficulty):

    #used as junk to sift through
    filler = ['[([&%$)++@!#$%%^', '^&^#%^$*!$$*', '~!!)%&+$#@#+', '#^#$*(@%$&&%', '#^%*$%*!!#$&"{$', ':"{}@#%(@%(%']

    # this is the word bank for each difficulty,
    # the higher the difficulty, themore letter in the words used
    novice_words = ['LAKE', 'MEAL', 'MATH', 'ROAD', 'BATH', 'DATA', 'CITY',
                    'MENU', 'DEBT', 'GOAL', 'MOOD', 'YEAR', 'BEER', 'USER', 'IDEA', 'DESK',
                    'EXAM', 'POEM', 'MEAT', 'WIFE', 'WOOD', 'MODE', 'GIRL', 'SONG', 'GATE',
                    'GENE', 'UNIT', 'LOSS', 'LOVE', 'FACT', 'NEWS', 'FOOD', 'LADY', 'POET',
                    'BIRD', 'DISK', 'ROLE', 'SOUP', 'CELL', 'AREA', 'MALL', 'OVEN', 'DIRT',
                    'ARMY', 'WEEK', 'HAIR', 'TOWN', 'TALE', 'KING', 'HALL']

    advanced_words = ['MONTH', 'UNION', 'WOMAN', 'RIVER', 'DRAMA', 'TOOTH', 'SKILL',
                      'HEART', 'PIANO', 'QUEEN', 'CHEEK', 'VIRUS', 'ACTOR', 'CHILD', 'BONUS',
                      'PHOTO', 'MUSIC', 'MEDIA', 'EVENT', 'BASIS', 'SHIRT', 'APPLE', 'POWER', 'YOUTH',
                      'CHEST', 'BLOOD', 'BUYER', 'HOTEL', 'HONEY', 'PIZZA', 'UNCLE', 'TRUTH', 'THING',
                      'VIDEO', 'ENTRY', 'ERROR', 'NIGHT', 'WORLD', 'RATIO', 'OWNER', 'PHONE', 'MOVIE',
                      'PAPER', 'DEATH', 'SCENE', 'STORY', 'BREAD', 'DEPTH', 'SALAD', 'STEAK']

    expert_words = ['SECTOR', 'MEMORY', 'TONGUE', 'ESTATE', 'EFFORT',
                    'NATION', 'THROAT', 'FLIGHT', 'WRITER', 'POTATO', 'WEALTH', 'BREATH',
                    'ENERGY', 'PERSON', 'MOMENT', 'FAMILY', 'ORANGE', 'DEALER', 'CANCER',
                    'PLAYER', 'MEMBER', 'SERIES', 'VOLUME', 'NATURE', 'THANKS', 'GUITAR',
                    'METHOD', 'SINGER', 'DINNER', 'COUSIN', 'OFFICE', 'REGION', 'INJURY',
                    'BASKET', 'CAMERA', 'AGENCY', 'SAFETY', 'EXTENT', 'LEADER', 'SYSTEM',
                    'ADVICE', 'WINNER', 'SPEECH', 'PEOPLE', 'LENGTH', 'RECIPE', 'POLICY',
                    'COUNTY', 'GROWTH', 'COFFEE']

    master_words = ['ROMANTIC', 'DELICATE', 'SEPARATE', 'CRITICAL', 'FOOTBALL', 'BASEBALL',
                    'ROTATION', 'RESOURCE', 'PRESENCE', 'MOUNTAIN', 'APPROVAL', 'STRENGTH',
                    'EQUATION', 'ORGANIZE', 'LOCATION', 'QUANTITY', 'OFFICIAL', 'DELIVERY',
                    'SPECTRUM', 'FOLKLORE', 'DETECTOR', 'HELPLESS', 'MOMENTUM', 'SANDWICH',
                    'SUPERIOR', 'NONSENSE', 'OPPOSITE', 'RAILROAD', 'MAGAZINE', 'LITERACY',
                    'HUMANITY', 'RHETORIC', 'DISTINCT', 'MERCHANT', 'CEMETERY', 'HESITATE',
                    'DOMINANT', 'INCIDENT', 'TRAINING', 'SKELETON', 'ADOPTION', 'DISCLOSE', 
                    'MEMORIAL', 'DISASTER', 'CALENDAR', 'CONTEMPT', 'SUNSHINE', 'MATERIAL', 
                    'PARTICLE', 'TALENTED']

    # used for the randomizer
    levels = [novice_words, advanced_words, expert_words, master_words]

    level = levels[difficulty-1]
    
    # determin the password beforehand
    password = level[randint(0, 49)]

    # these are the available configurations you can receive to guess through
    # the password is inserted in a position available
    available_lines =   [password+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+                        
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)],

                        level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+                        
                        filler[randint(0, 5)]+level[randint(0, 49)]+password+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)],

                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+password+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)],

                        level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+password,
                        
                        level[randint(0, 49)]+filler[randint(0, 5)]+password+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)],

                        level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+level[randint(0, 49)]+filler[randint(0, 5)]+level[randint(0, 49)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+password+filler[randint(0, 5)]+'\n'+
                        filler[randint(0, 5)]+filler[randint(0, 5)]+filler[randint(0, 5)]+level[randint(0, 49)]]
                        
    # presents the words and filler
    print(available_lines[randint(0,5)])
    # strike visual counter
    strikes = ''
    # guess counter
    guesses_num = 4
    # iterates as long as there are available guesses
    while guesses_num > 0:
        word_guess = input('\nYou have ' + str(guesses_num) + ' chances. What is the password? ')
        # uses the likeness function to determine next step
        a = likeness(password, word_guess)
        if a == True:
            print('USER AUTHORIZATION ACCEPTED')
            break
        else:
            guesses_num -= 1
            strikes += ' x'
            print(strikes)
    # once you have no more guesses. I brick your computer
    if guesses_num == 0:
        print('YOU HAVE BEEN LOCKED OUT OF THE SYSTEM. LEAVE.')
        # exe_execute(order_66.exe).exe
    
# function that runs the game simulation
def terminal():
    help()
    interface(intro())

# run
terminal()