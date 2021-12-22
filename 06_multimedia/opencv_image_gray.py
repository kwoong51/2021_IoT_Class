import cv2

img = cv2.imread('um.jpg')
img2 = cv2.resize(img, (400,400))
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('um.jpg', img2)
cv2.imshow('um_gray.jpg', gray)

while True:
    if cv2.waitKey(0) == 13:
        break

cv2.imwrite('um_gray.jpg',gray)

cv2.destroyAllWindows()