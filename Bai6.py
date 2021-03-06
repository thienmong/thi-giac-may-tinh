#khu nhieu
#thong so bong   3,88,0     150,255,83

#thong so xe 30, 15, 22     207, 78, 71


import cv2
import time
import numpy as np

def Min_Blue(pos):
    Min_Blue.value = pos;
Min_Blue.value = 3;
def Min_Green(pos):
    Min_Green.value = pos
Min_Green.value =88;
def Min_Red(pos):
    Min_Red.value = pos
Min_Red.value = 0;

def Max_Blue(pos):
    Max_Blue.value = pos;
Max_Blue.value = 150;
def Max_Green(pos):
    Max_Green.value = pos
Max_Green.value = 255;
def Max_Red(pos):
    Max_Red.value = pos
Max_Red.value = 83;

#6 thanh task 3
cv2.namedWindow("Control")
cv2.createTrackbar("Min blue","Control", 0,255,Min_Blue)
cv2.createTrackbar("Min green","Control", 0,255,Min_Green)
cv2.createTrackbar("Min red","Control", 0,255,Min_Red)

cv2.createTrackbar("Max blue","Control", 0,255,Max_Blue)
cv2.createTrackbar("Max green","Control", 0,255,Max_Green)
cv2.createTrackbar("Max red","Control", 0,255,Max_Red)

cap = cv2.VideoCapture("tracking.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

wait_time = 1000/fps
print(fps)

play = True;
while True:
    pre_time = time.time()

    if play:
        ret, img = cap.read()
    if ret == False:        #ktra video con ton tai hay ko
        break;
    cv2.imshow("Control",img)

#xu ly anh

    lower = np.array([Min_Blue.value,Min_Green.value,Min_Red.value])
    upper = np.array([Max_Blue.value, Max_Green.value, Max_Red.value])

    mask_sub = cv2.inRange(img,lower, upper)
    kernel = np.ones((3,3))
    mask_sub = cv2.erode(mask_sub,kernel)
    kernel = np.ones((5, 5))
    mask_sub = cv2.dilate(mask_sub,kernel)

    mask = cv2.merge((mask_sub,mask_sub,mask_sub))

    res = cv2.bitwise_and(img,mask)

    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)



    #dong bo thoi gian
    delta_time = (time.time() - pre_time)*1000

    if delta_time > wait_time:
        delay_time = 1
    else:
        đelay_time = wait_time - delta_time

    key = cv2.waitKey(int(wait_time))
    if key == ord('q'):
        break
    if key == ord(' '):
        play = not play

cv2.destroyAllWindows()


