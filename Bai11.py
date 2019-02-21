#bam theo do sang

import cv2
import time
import numpy as np

def Mouse_event(event, x, y, f, img):

    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.draw = True
    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        min_y = min(Mouse_event.y0,Mouse_event.y1)
        max_y = max(Mouse_event.y0,Mouse_event.y1)
        min_x = min(Mouse_event.x0,Mouse_event.x1)
        max_x = max(Mouse_event.x0,Mouse_event.x1)
        Mouse_event.img = img[min_y:max_y,min_x:max_x]

    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x
        Mouse_event.y = y


Mouse_event.img = None
Mouse_event.x0 = 0
Mouse_event.yo = 0
Mouse_event.x1 = 0
Mouse_event.x2 = 0
Mouse_event.x = 0
Mouse_event.y = 0
Mouse_event.draw = False

cap = cv2.VideoCapture(1)
fps = cap.get(cv2.CAP_PROP_FPS)

wait_time = 1000.0/fps
print(fps)

play = True;
while True:
    pre_time = time.time()

    if play:
        ret, img = cap.read()
    if ret == False:  # ktra video con ton tai hay ko
        break;
#Mount_Event
    img_copy = img.copy()
    if Mouse_event.draw:
        img = cv2.rectangle(img_copy,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is None:
        img_clone = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
    else:
        img_clone = cv2.cvtColor(Mouse_event.img,cv2.COLOR_BGR2HSV)
        cv2.imshow("test",Mouse_event.img)
#xy ly anh 
    h = np.mean(img_clone[:, :, 0])
    s = np.mean(img_clone[:, :, 1])
    v = np.mean(img_clone[:, :, 2])

    l = np.array([h - 20, s - 20, v - 32])
    u = np.array([h + 20, s + 20, v + 20])
    mask = cv2.inRange(cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV), l, u)

    _, contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contour) > 0:
        dt = []
        for c in contour:
            dt.append(cv2.contourArea(c))
        max_i = np.argmax(dt)

        max_c = contour[max_i]
        cv2.polylines(img_copy, [max_c], True, (0, 0, 255), 2)



    cv2.imshow("Video",img_copy)
    cv2.setMouseCallback("Video",Mouse_event,img)







    #dong bo thoi gian
    delta_time = (time.time() - pre_time) * 1000

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

