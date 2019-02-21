import cv2

def get_value(pos):
    get_value.value = pos
get_value.value = 0

cv2.namedWindow("Control")
cv2.createTrackbar("Value","Control",0,255,get_value)


while True:
    img = cv2.imread("3.jpg")
    cv2.imshow("Control",img)

    ret, img = cv2.threshold(img,get_value.value,255,cv2.THRESH_TRUNC)
    cv2. imshow("Image",img)
    print(ret)

    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()