
import sys,os
import curses

import cv2,time
import Features
import pandas as pd
import db

RESIZE_FACTOR = 0.02


def get_input(stdscr):

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

def get_feature_loop_from_video(stdscr):

    # Start video stream
    video=cv2.VideoCapture(0)
    df = pd.DataFrame()
    df['img_gray'] = []
    df['time'] = []
    df['shape'] = []
    df['label'] = []
    t1 = time.time()
    a = 0
    k = 0
    d=''
    while ( time.time() - t1 ) < 15:


        # Collect key pressed here -----
        stdscr.clear()

        if k == curses.KEY_DOWN:
            d='DOWN'
        elif k == curses.KEY_UP:
            d='UP'
        elif k == curses.KEY_RIGHT:
            d='RIGHT'
        elif k == curses.KEY_LEFT:
            d='LEFT'
        else:
            d='NONE'

        # Rendering some text
        stdscr.addstr(0, 0, 'Collecting Features. Press q to quit')
        stdscr.addstr(1, 0, 'LAST KEY: '+d)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
        # -------------

        # Show next video frame
        a+=1
        check,frame = video.read()
        # Convert to grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (0,0), fx=RESIZE_FACTOR, fy=RESIZE_FACTOR)
        cv2.imshow('Capturing',gray)
        time_ = time.time()*1000.0
        df = df.append({'img_gray': [x for x in gray.ravel()],
                        'label':d,
                        'time': time_,
                        'shape':gray.shape}, ignore_index=True)

        # Play stream
        key = cv2.waitKey(1)
        if key== ord('q'):
            break


    video.release()
    cv2.destroyAllWindows
    return df

def get_single_input(stdscr):

    # Wait for next input
    k = stdscr.getch()
    d=''

    # Initialization
    stdscr.clear()

    if k == curses.KEY_DOWN:
        d='DOWN'
    elif k == curses.KEY_UP:
        d='UP'
    elif k == curses.KEY_RIGHT:
        d='RIGHT'
    elif k == curses.KEY_LEFT:
        d='LEFT'
    else:
        d= 'NONE'


    # Refresh the screen
    stdscr.refresh()

    return d

class Collector():


    def gather(self):
        curses.wrapper(get_input)
        return

    def get_key(self):
        #d = curses.wrapper(get_single_input)
        df = curses.wrapper(get_feature_loop_from_video)
        return df
