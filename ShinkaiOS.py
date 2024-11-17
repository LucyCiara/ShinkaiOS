import os, curses, time
os.system('cls' if os.name == 'nt' else 'clear')

# A function for displaying the text from the user manual
def UserManual(stdscr):
    # The program loop
    replyLoop = True
    while replyLoop:
        # Writes the user manual
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome!")
        stdscr.addstr(1, 0, "This program is a discovered, unreleased 'OS'.")
        stdscr.addstr(2, 0, "If you want to read a file or open a folder, you have to enter the file name.")
        stdscr.addstr(3, 0, "If you want to exit a file or move up a folder, you have to enter '..'")
        stdscr.addstr(4,0, ">")
        stdscr.refresh()

        # Reads input to check if the user has written '..', which will exit this function
        usrInput = stdscr.getstr()
        if usrInput == b'..':
            replyLoop = False

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

# The main function
def main(stdscr):
    # Variable preparations
    stdscr.clear()
    curses.curs_set(0)
    HEIGHT = curses.LINES
    WIDTH = curses.COLS
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    programVersion = "v1.0"

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
    curses.curs_set(2)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(0.5)
    curses.echo()


    # Program run-loop
    run = True
    while run:
        # Displays all the lines for all the "files"
        displayOrder = ["UserManual.TXT", "Map.COM", "Documents", "Quit", ">"]
        stdscr.clear()
        for i in range(len(displayOrder)):
            stdscr.addstr(i, 0, displayOrder[i])
        stdscr.refresh()

        # Awaits user input to see which "file" they want to execute/which "directory" they want to open, or if they want to quit the application
        usrInput = stdscr.getstr()
        if usrInput == b'UserManual.TXT':
            UserManual(stdscr)
        elif usrInput == b'Map.COM':
            Map(stdscr, HEIGHT, WIDTH)
        elif usrInput == b'Quit':
            run = False


        
curses.wrapper(main)