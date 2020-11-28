from tkinter import *
import pyautogui as pag
from time import sleep
import threading
import signal
import os 
# import ttk
# from ttk import *

# THIS TUTORIAL SHOWS HOW TO USE CX_FREEZE TO BUILD THE EXECUTABLE FILE WITH IMAGES AND DEPENDENCIES https://www.youtube.com/watch?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&v=HosXxXE24hA&feature=emb_logo&ab_channel=sentdex

class noSleep:
    def __init__(self, master):
        self.frame = Frame(master, width=300, height=250)
        self.frame.pack()

        l1 = Label(self.frame, text="noSchleep")
        l1.pack()

        self.pid = os.getpid()
        self.active_thread = threading.get_ident()

        print("original PID: ", self.pid, "ThreadID: ", self.active_thread)

        self.b_start = Button(self.frame, text="Start", command=self.start, bg="black")
        self.b_start.pack()

        self.b_stop = Button(self.frame, text="Quit", command=self.stop, fg="red") 
        self.b_stop.pack()


    def start(self):
        print("starting...")
        self.active_thread = threading.Thread(target=self.motionThread)
        self.active_thread.daemon = True
        self.active_thread.start()


    def stop(self):
        print("Attempting to stop the program... \nSIGINT sent to tid: ", self.active_thread)
        os.kill(self.pid, signal.SIGINT)


    def motionThread(self):
        self.pid = os.getpid()
        print("SET THE PID TO: ", self.pid)
        print("motionThread ID: ", self.active_thread)
        while True:
            try:
                print("...")
                pag.scroll(-1)  
                sleep(15)
                pag.scroll(1)  
            except KeyboardInterrupt:
                print("KEYBOARD INTRPT")
                break

#------------------------------------------------------

root = Tk()
ns = noSleep(root)

# -- replace the feather icon with my own --
# photo = PhotoImage(file = "example.ico")
# root.iconphoto(False, photo)

# -- Create a menu for top of program https://www.youtube.com/watch?v=PSm-tq5M-Dc&ab_channel=thenewboston --

#----------------------------------

try:
    root.mainloop()
except KeyboardInterrupt:
    os.kill(ns.pid, signal.SIGINT)
