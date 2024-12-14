import os, curses, time, re, string, random, textwrap
os.system('cls' if os.name == 'nt' else 'clear')

# Checks if the string has japanese characters and returns a match
def checkJp(string: str) -> object:
    jpCharsPattern = re.compile(r'[\u3000-\u303f\u3040-\u30FF\u4E00-\u9FFF]')
    return jpCharsPattern.match(string) 

# Adds spaces after japanese letters because they take up twice the space in terminals, and otherwise they'll mesh together.
def displayOrderConvertion(displayOrder: list, WIDTH) -> list:
    wrapper = textwrap.TextWrapper(width=WIDTH)
    newDisplayOrder = []
    for i in range(len(displayOrder)):
        newDisplayString = ""
        for j in range(len(displayOrder[i])):
            if checkJp(displayOrder[i][j]):
                newDisplayString += f"{displayOrder[i][j]} "
            else:
                newDisplayString += displayOrder[i][j]
        
        newDisplayString = wrapper.wrap(text=newDisplayString)
        for line in newDisplayString:
            newDisplayOrder.append(line)

    return newDisplayOrder

# Takes lines of text and puts them on the screen
def TextFile(stdscr, displayOrder, HEIGHT):
    replyLoop = True
    while replyLoop:
        if len(displayOrder) < HEIGHT:
            # Writes the text file
            stdscr.clear()
            
            for i in range(len(displayOrder)):
                stdscr.addstr(i, 0, displayOrder[i])
            stdscr.refresh()


        else:
            # Splits the text into multiple pages if it's too long
            for x in range(len(displayOrder)//HEIGHT+1):
                stdscr.clear()
                
                for i in range(len(displayOrder[HEIGHT*x:HEIGHT*(x+1)])):
                    stdscr.addstr(i, 0, displayOrder[HEIGHT*x:HEIGHT*(x+1)][i])
                stdscr.refresh()
                
                if x != len(displayOrder)//HEIGHT:
                    stdscr.getkey()

        # Reads input to check if the user has written '..', which will exit this function
        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False


# A function for displaying the text from the user manual
def UserManual(stdscr, HEIGHT, WIDTH):
    displayOrder = displayOrderConvertion([
        "ようこそ！ (Welcome!)", 
        "このプログラムは、発見された未発表の「OS」です。(This program is a discovered, unreleased 'OS'.)", 
        "もしファイルを読みたかったら、ファイル名を入力しなくてはなりません。(If you want to read a file, you have to enter the file name.)", 
        "ディレクトリを移動したかったら、「..」を入力しなくてはなりません。 (If you want to exit a directory, you have to enter'..')", 
        ">"
        ], WIDTH)
    # The program loop
    TextFile(stdscr, displayOrder, HEIGHT)

# A function for displaying the map
def Map(stdscr, HEIGHT, WIDTH):
    # The program loop
    replyLoop = True
    while replyLoop:
        # Clears the screen and reads the map file
        stdscr.clear()
        with open("data/map.txt", mode="r") as datafile:
            map = datafile.readlines()
        
        # Records all the symbols of the map file and their coordinates
        mapCoords = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] != ' ':
                    mapCoords.append((i, j, map[i][j]))

        # Find out where how much to skew the text in order to center the ascii art in the terminal
        startY = (HEIGHT-len(map))//2
        startX = (WIDTH-len(map[0]))//2

        # Writes all the symbols onto the terminal, and the pointer at the bottom
        for item in mapCoords:
            stdscr.addstr(startY+item[0], startX+item[1], item[2])
        stdscr.addstr(HEIGHT-1, 0, ">")
        stdscr.refresh()

        # Checks to see if the user input is '..' so the function can conclude
        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False

# Writes the corrupted "牛頭" file
def CowHead(stdscr, HEIGHT, WIDTH):
    errorStr = "ERROR: CORRUPTED FILE"

    replyLoop = True
    while replyLoop:
        stdscr.clear()

        # Generates a random jumble of symbols according to how big the window is
        stringConstant = string.ascii_letters+string.digits+string.punctuation
        jumbleStr = ""
        for i in range(0, (HEIGHT-1)*(WIDTH)):
            jumbleStr += stringConstant[random.randint(0, len(stringConstant)-1)]
        stdscr.addstr(jumbleStr)
        
        # Adds the error message on top of the jumble as well as the pointer
        stdscr.addstr((HEIGHT-1)//2, (WIDTH-len(errorStr))//2, errorStr, curses.color_pair(2))
        stdscr.addstr(HEIGHT-1, 0, ">")
        stdscr.refresh()

        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False

# Displays the first log
def Log1(stdscr, HEIGHT, WIDTH):
    displayOrder = displayOrderConvertion([
        "If you're reading this, and you're not me, then I'm most likely dead... As if that's ever gonna happen LMAO.",
        "I've decided to write these log entries in case this program somehow gets into the hands of someone else, so that you'll have an easier time understanding things than me. (I'm gonna write this in english because my mom always gets on my ass for not doing well in school, and this is a good way to practice, right?)",
        "I can start by writing about how I found this program in the first place: It all started when I was going home from school (alone, as usual, because Nezuko and Haze are always too busy and also Nezuko is kinda annoying and Haze is an asshole and owes me a lot of money), when I saw it on my doorstep. At first I thought it was one of the- *ahem* videos I rented using the new rental bulletin board the video store has started using, but as I picked it up I saw it had '深海OS' written on it. The postal service must've just sent it to the wrong address or something, but I gotta say it's fucking creepy. It keeps telling me about some fucking 'blue text' at start up, and I found some corrupted file called 牛頭 (it sounds familiar, but I can't remember from where), as well as a map of the town with some locations written down. Is this some sort of terrorist or soviet spy program I got by mistake? I'm really scared of what might happen if they find out I recieved it instead...",
        ">"
        ], WIDTH)
    TextFile(stdscr, displayOrder, HEIGHT)

# Displays the second log
def Log2(stdscr, HEIGHT, WIDTH):
    displayOrder = displayOrderConvertion([
        "I've managed to somehow update the program by feeding it signals from some wonky stuff happening at the abandoned nuclear power plant. I was sneaking in while Haze was out doing her stuff, and sat up this device i saw in my dreams. It took me like a month of trying to build that thing, and I started coughing up some blood, but-like-I've been told that the radiation coming from those power plants are like a harmless X-Ray, so I'll be fine.",
        "It seems like it was some sort of test from the program to check if I was worthy to get the full use of it. I wonder if there'll be more updates in the future... Anyways I can now write in the names of the areas highlighted on the map and get some information about them. Their descriptions are really worrying and mentioning 'Ghosts' and 'Forbidden texts housing demons' and shit. I checked out one of these locations, and while I didn't see any ghosts and have never been the occult type, I felt like there was definitely something paranormal going on.",
        "I've also noticed some blue text popping up, and I'm not sure what that's about, but I feel like I've read the program talk about '青いテクスト' somewhere... Oh well it's probably not important LMFAO.",
        ">"
        ], WIDTH)
    TextFile(stdscr, displayOrder, HEIGHT)

# Displays the Logs directory
def Logs(stdscr, HEIGHT, WIDTH):
    displayOrder = displayOrderConvertion([
        "Log1",
        "Log2",
        ">"
        ], WIDTH)
    
    replyLoop = True
    while replyLoop:
        stdscr.clear()
        
        for i in range(len(displayOrder)):
            stdscr.addstr(i, 0, displayOrder[i])
        stdscr.refresh()

        # Reads input to check if the user has written '..', which will exit this function
        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False
        elif usrInput == b'Log1':
            Log1(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Log2':
            Log2(stdscr, HEIGHT, WIDTH)

# Writes the documents directory
def Documents(stdscr, HEIGHT, WIDTH):
    displayOrder = displayOrderConvertion([
        "牛頭.TXT", 
        "Logs", 
        ">"
        ], WIDTH)
    
    replyLoop = True
    while replyLoop:
        stdscr.clear()
        
        for i in range(len(displayOrder)):
            stdscr.addstr(i, 0, displayOrder[i])
        stdscr.refresh()

        # Reads input to check if the user has written '..', which will exit this function
        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False
        elif usrInput == '牛頭.TXT'.encode(encoding="utf-8") or usrInput == '牛 頭 .TXT'.encode(encoding="utf-8"):
            CowHead(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Logs':
            Logs(stdscr, HEIGHT, WIDTH)

# The main function
def main(stdscr):
    # Variable preparations
    stdscr.clear()
    curses.curs_set(0)
    HEIGHT = curses.LINES
    WIDTH = curses.COLS
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    programVersion = "v1.1"
    warningText = displayOrderConvertion([
        "端末の解像度を変えないでください。",
        "青いテクストを信用しないでください。"
        ], WIDTH)
    
    # Extracts the ascii art text from logo.txt
    logo = []
    with open("data/logo.txt", mode="r", encoding="utf-8") as dataFile:
        logo = dataFile.readlines()
    
    # Finds all the coordinates of '＃'s of the text extracted from logo.txt
    logoCoords = []
    for i in range(len(logo)):
        for j in range(len(logo[i])):
            if logo[i][j] == '＃':
                logoCoords.append((i, j))

    # Find out where how much to skew the text in order to center the ascii art in the terminal
    startY = (HEIGHT-len(logo))//2
    startX = (WIDTH-len(logo[0]))//2

    # Simulates a splash screen
    time.sleep(1)
    for item in logoCoords:
        if item[1] >= 32:
            stdscr.addstr(item[0]+startY, item[1]+startX, "＃", curses.color_pair(1))
        else:
            stdscr.addstr(item[0]+startY, item[1]+startX, "＃")
        if item == logoCoords[-1]:
            stdscr.addstr(item[0]+startY+5, (WIDTH-len(programVersion))//2, programVersion)  
    stdscr.refresh()
    time.sleep(3)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(0.5)
    
    # Simulates a warning screen
    warning = "警 告 "
    startY = (HEIGHT-1)//2
    startX = (WIDTH-len(warning))//2
    stdscr.addstr(startY, startX, warning, curses.color_pair(2))
    for i in range(len(warningText)):
        stdscr.addstr(startY+i+1, (WIDTH-len(warningText[i]))//2, warningText[i], curses.color_pair(3))
    stdscr.refresh()
    time.sleep(3)
    curses.curs_set(2)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(0.5)

    curses.echo()

    # Program run-loop
    run = True
    while run:
        # Displays all the lines for all the "files"
        displayOrder = displayOrderConvertion([
            "UserManual.TXT",
            "Map.COM", 
            "Documents", 
            "Quit", 
            ">"
            ], WIDTH)
        stdscr.clear()
        for i in range(len(displayOrder)):
            stdscr.addstr(i, 0, displayOrder[i])
        stdscr.refresh()

        # Awaits user input to see which "file" they want to execute/which "directory" they want to open, or if they want to quit the application
        usrInput = stdscr.getstr()
        if usrInput == b'UserManual.TXT':
            UserManual(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Map.COM':
            Map(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Documents':
            Documents(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Quit':
            run = False
        
curses.wrapper(main)