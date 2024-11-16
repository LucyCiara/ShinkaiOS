from curses import wrapper

def main(stdscr):
    stdscr.clear()
    
    stdscr.addstr("深海OS")
    
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)