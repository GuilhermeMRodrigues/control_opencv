import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while(True):
    #captura fram-por-frame
    ret, frame = cap.read()

    #operações nos frames 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #mostra os frames resultantes
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#quando terminar, fecha a captura
cap.release()
cv2.destroyAllWindows() 