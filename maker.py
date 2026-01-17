import cv2
import pyautogui
import time

time.sleep(10)
photographia= cv2.imread('ex.jpg')
if photographia is None :
     print('den yparxei,doesnt exist')
     exit()

photographia = cv2.rotate(photographia,cv2.ROTATE_90_COUNTERCLOCKWISE)
gri = cv2.cvtColor(photographia, cv2.COLOR_BGR2GRAY)
ipsos , fardos = gri.shape 
allagh = 500 / max(ipsos , fardos)
gri = cv2.resize(gri, (int(fardos * allagh), int(ipsos * allagh)))
ipsos , fardos = gri.shape
iarxh =  -50
jarxh = 250
for i in range(ipsos):
     for j in range(fardos):
          xroma = gri[i,j]
          if xroma < 100: 
           othonix = iarxh + i
           othoniy = jarxh + j 
           pyautogui.click(othonix , othoniy ,duration=0)

pyautogui.moveTo(430,930)
pyautogui.click(430,930)