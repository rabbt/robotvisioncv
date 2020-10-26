############## Importar modulos #####################

from tkinter import *
from PIL import Image, ImageTk 

import cv2
import numpy as np
import sys

  
def onClossing():
    
    print(f"Threshold value= {umbralValue.get()}")
    root.quit()                 #Salir del bucle de eventos.
    cap.release()               #Cerrar camara
    print("Ip Cam Disconected")
    root.destroy()              #Destruye la ventana tkinter creada


def thresholdValue(int):
    umbralValue.set(slider1.get())
    
def callback():  #codigo propio que se correra junto con el mainloop

        ################## Adquisición de la Imagen ############
        
        cap.open(url) # Antes de capturar el frame abrimos la url
        ret, frame = cap.read() # Leer Frame

        if ret:
            ################# Procesamiento de la Imagen ##########

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Convertir a BGR a grises

            t, binary = cv2.threshold(gray,umbralValue.get(),255, cv2.THRESH_BINARY)

            # Mostrar imagen en el HMI 
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img.thumbnail((400,400))
            tkimage = ImageTk.PhotoImage(img)
            label.configure(image = tkimage )
            label.image = tkimage
            
            img1 = Image.fromarray(binary)
            img1.thumbnail((400,400))
            tkimage1 = ImageTk.PhotoImage(img1)
            label1.configure(image = tkimage1 )
            label1.image = tkimage1
        
            root.after(10,callback)# Llamar a callback despues de 10 ms
            
        else:
            onClossing()


########################### Ip Cam ###########################
            
url='http://192.168.1.7:8080/shot.jpg'
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Ip Cam initializatized")
else:
    sys.exit("Ip Cam disconnected")
    
############################## HMI design #################     
root = Tk()
root.protocol("WM_DELETE_WINDOW",onClossing)
root.title("Vision Artificial") # titulo de la ventana

umbralValue = IntVar()

label=Label(root)
label.grid(row=0,padx=20,pady=20)

label1=Label(root)
label1.grid(row=0,column=1,padx=20,pady=20)

slider1 = Scale(root,label = 'Threshold value', from_=0, to=255, orient=HORIZONTAL,command=thresholdValue,length=400)   #Creamos un dial para recoger datos numericos
slider1.grid(row=1)

root.after(10,callback) # Llamar a callback despues de 10 ms
root.mainloop()

