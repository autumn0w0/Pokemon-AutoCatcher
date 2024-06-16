import time
import random
import pytesseract
import keyboard
import pyautogui
import pygetwindow as gw
import numpy as np
import cv2

# Configuration
poke = ['pawniard', 'scyther', 'larvesta']
ability = ['defiant', 'scyther', 'flame body']
capture_x = 500  # X-coordinate of the top-left corner
capture_y = 250  # Y-coordinate of the top-left corner
capture_width = 900  # Width of the region to capture
capture_height = 550  # Height of the region to capture

# Initialize variables
pokeballCount = 140
pokemoveCount = 50
pcf = 0
pmf = 0
key_flag = 1
ocrString=""



# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(1)
app_window = gw.getWindowsWithTitle("PROClient")
if len(app_window) == 0:
    print("Window not found.")
else:
    app_window = app_window[0]
    app_window.activate()

#movement function
def movement(key_flag):
    key_to_hold = "right" if key_flag == 1 else "left"
    keyboard.press(key_to_hold)
    time.sleep(random.randint(0, 1))
    keyboard.release(key_to_hold)


#check function
def checkIfExists(stat, string):
    return any(s.lower() in string.lower() for s in stat)


#getProcessedImage function
def getProcessedImage(img):
    img=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    thresh,im_bw = cv2.threshold(img,90,255,cv2.THRESH_BINARY)
    return im_bw

#catchPoke function
def catchPoke(pokemoveCount,pokeballCount):
 # Switch to Smeargle code
    ocrString="test"
    time.sleep(1)
    keyboard.press_and_release('y')
    time.sleep(1)
    keyboard.press_and_release('u')
    time.sleep(11)
    # Use False Swipe code
    keyboard.press_and_release('t')
    time.sleep(1)
    keyboard.press_and_release('t')
    time.sleep(10)
    pokemoveCount -= 1
    while 'success' not in ocrString.lower():
        if len(ocrString) == 0:
            break
        time.sleep(1)
        # Throw pokeball code
        keyboard.press_and_release('u')
        time.sleep(1)
        keyboard.press_and_release('t')
        time.sleep(14)
        pokeballCount -= 1
        if pokeballCount == 0:
            break
        # Wait for success or repeat from throw if failed
        img = pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
        ocrString = pytesseract.image_to_string(getProcessedImage(img))
        img.close()    
    return pokemoveCount,pokeballCount

try:
    while True:
        # Movement
        while 'wild' not in ocrString.lower() :
            movement(key_flag)
            key_flag = 1 - key_flag
            img = pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
            ocrString = pytesseract.image_to_string(getProcessedImage(img))
            img.close()
        
        time.sleep(5)

        img = pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
        time.sleep(0.5)
        ocrString = pytesseract.image_to_string(getProcessedImage(img))
        img.close()
        
        if 'encounter' in ocrString.lower():
            # Switch to Smeargle code
            while 'encounter' in ocrString.lower():
                time.sleep(1)
                img = pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
                ocrString = pytesseract.image_to_string(getProcessedImage(img))
                img.close()
            pokemoveCount,pokeballCountt=catchPoke(pokemoveCount,pokeballCount)
            print("-------------------------------------------------")
            print("\n rareform reencountered")
            print("\n-----------------------------------------------")
            # Add alert
            continue

        if checkIfExists(poke, ocrString):
            if checkIfExists(ability, ocrString):
                pokemoveCount,pokeballCountt=catchPoke(pokemoveCount,pokeballCount)
            else:
                # Run away key
                keyboard.press_and_release('i')
        else:
            # Run away key
            keyboard.press_and_release('i')
        if pokeballCount == 0 or pokemoveCount == 0:
            print("pokemon or moveset over")
            break

except KeyboardInterrupt:
    print("Script interrupted.")
