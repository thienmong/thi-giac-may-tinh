import cv2
import time

cap = cv2.VideoCapture("AMV.MP4")
fps = cap.get(cv2.CAP_PROP_FPS)

wait_time = 1000/fps
print(fps)


while True:
    pre_time = time.time()
    ret, img = cap.read()
    img = cv2.medianBlur(img,3)
    cv2.imshow("videp",img)

    #dong bo thoi gian
    delta_time = (time.time() - pre_time)*1000

    if delta_time > wait_time:
        delay_time = 1
    else:
        đelay_time = wait_time - delta_time


    if cv2.waitKey(int(wait_time)) == ord('q'):
        break

cv2.destroyAllWindows()


