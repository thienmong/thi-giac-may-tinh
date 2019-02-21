import cv2
img = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",img)
cv2.imshow("image2",img2)
cv2.waitKey()
cv2.destroyAllWindows();
