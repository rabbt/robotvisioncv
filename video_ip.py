import cv2
import sys

url = 'http://192.168.1.7:8080/shot.jpg'

cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("ip cam initialized")
else:
    sys.exit("ip cam disconnected")

while True:
    
    cap.open(url)#antes de capturar el frame abrimos la url
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow('img',frame)  
    else:
        print("ip cam disconnected")
        break
    
    if(cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()