from tkinter import *
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import sys

def onClossing():
    print(f"Threshold value= { umbral.value.get() }")
    root.quit()                     
    cap.release()
    print("Ip Camera Disconected")
    root.destroy()
    
    
# ---------------------------------- ip cam ---------------------------------- #

url = 'http://192.168.1.7:8080/shot.jpg'

cap = cv.VideoCapture(url)

if cap.isOpened():
    print("ip cam initialized")
else:
    sys.exit("ip cam disconnected")