#Code for coursehero skip automation

import sys
import pyautogui as p
import time as t
import keyboard
p.FAILSAFE = True

## coursehero
def code():
    text = "Skip Question"
    p.hotkey('ctrl','f')
    t.sleep(1)
    p.typewrite(text)
    t.sleep(1)
    p.hotkey('ctrl','enter')
    t.sleep(1)
    p.click(658,467)
    t.sleep(1)
    p.click(1026,951)
    t.sleep(3)
    
while True:
    print("Loading...")
    k = keyboard.read_key()
    ## for skip
    if(k == "0"):
        code()
        p.click(1055,636)
    ## for change category
    elif(k == "c"):
        code()
        p.click(894,623)
    ## for answer you have to close the program execution
    elif(k == 'q' or k=='Q'):
        sys.exit()
        
    
