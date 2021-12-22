import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,30,(640, 480))

while True:
    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)

    if cv2.waitKey(10) == 13:
        break

cap.release()
out.release()
cv2.destroyAllWindows()