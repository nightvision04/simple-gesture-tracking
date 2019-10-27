

class Collector():

    def gather(stdscr):

        # Loop where k is the last character pressed
        k = 0
        d=''
        while (k != ord('q')):

            # Initialization
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            if k == curses.KEY_DOWN:
                d='DOWN'
            elif k == curses.KEY_UP:
                d='UP'
            elif k == curses.KEY_RIGHT:
                d='RIGHT'
            elif k == curses.KEY_LEFT:
                d='LEFT'

            # Rendering some text
            stdscr.addstr(0, 0, 'Collecting Features. Press q to quit')
            stdscr.addstr(1, 0, 'LAST KEY: '+d)

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()

        return
