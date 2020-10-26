import cv2
import sys

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("usb cam initialized")
else:
    sys.exit("usb cam disconnected")
    
while True:#obtener el frame
    ret, frame = cap.read() #verdadero o falso
    
    if ret:
        cv2.imshow('visual', frame)
    else:
        print("usb cam disconnected")
        break
    if (cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()