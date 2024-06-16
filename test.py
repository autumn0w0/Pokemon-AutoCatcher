import cv2
import pytesseract
import time
import pygetwindow as gw
import pyautogui
import numpy as np

img_path ='C:/Users/Circle/OneDrive/Pictures/Screenshots/poke2.png'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app_window = gw.getWindowsWithTitle("PROClient")
if len(app_window) == 0:
    print("Window not found.")
else:
    app_window = app_window[0]
    app_window.activate()
time.sleep(2)
capture_x = 500  # X-coordinate of the top-left corner
capture_y = 250  # Y-coordinate of the top-left corner
capture_width = 900  # Width of the region to capture
capture_height = 550  # Height of the region to capture
#img_path=pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
#img_path.show()
img=cv2.imread()
img=cv2.cvtColor(np.array(img_path),cv2.COLOR_BGR2GRAY)
#inverted_image = cv2.bitwise_not(img)
thresh,im_bw = cv2.threshold(img,90,255,cv2.THRESH_BINARY)
cv2.imshow("img",im_bw)
ocrString=pytesseract.image_to_string(im_bw)


print(ocrString)

cv2.waitKey(0)