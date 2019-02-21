import cv2
import time


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

cap = cv2.VideoCapture("tracking.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

wait_time = 1000/fps
print(fps)


while True:
    pre_time = time.time()
    ret, img = cap.read()
    img_copy = img.copy()

    if Mouse_event.draw:
        img = cv2.rectangle(img_copy,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is not None:
        cv2.imshow("Object",Mouse_event.img)
    cv2.imshow("Video",img)

    cv2.setMouseCallback("Video",Mouse_event,img)

    #dong bo thoi gian
    delta_time = (time.time() - pre_time)*1000

    if delta_time > wait_time:
        delay_time = 1
    else:
        đelay_time = wait_time - delta_time


    if cv2.waitKey(int(wait_time)) == ord('q'):
        break

cv2.destroyAllWindows()


