import os, curses, time
os.system('cls' if os.name == 'nt' else 'clear')

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
    with open("logo.txt", mode="r", encoding="utf-8") as dataFile:
        logo = dataFile.readlines()
    
    # Finds all the coordinates of '＃'s of the text extracted from logo.txt
    logoCoords = []
    for i in range(len(logo)):
        for j in range(len(logo[i])):
            test = logo[i][j]
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

    # Program run-loop
    run = False
    while run:
        stdscr.clear()
        stdscr.refresh()
        


curses.wrapper(main)


# logo = []
# with open("logo.txt", mode="r", encoding="utf-8") as dataFile:
#     logo = dataFile.readlines()
# print(logo)
# for item in logo:
#     print(item)