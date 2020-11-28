#!usr/bin/python3
from time import sleep
import pyautogui as pag
import os 

def motion():
    print("...")
    pag.scroll(-1)  
    sleep(20)
    pag.scroll(1)  

#------------------------------------------------------
while True:
    motion()

