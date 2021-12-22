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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge1 = cv2.Canny(frame,50,100)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge',edge1)
    out.write(frame)

    if cv2.waitKey(10) == 13:
        break

cap.release()
out.release()
cv2.destroyAllWindows()