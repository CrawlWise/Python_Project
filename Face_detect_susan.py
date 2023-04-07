import cv2
#from cv2 import Videocapture
#from cv2 import waitkey
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_ing = cv2.VideoCapture("Beyonces.jpg")

res, img = imp_ing.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,255, 0), 2)
cv2.imshow("Beyonces image", img)

cv2.waitKey(0)
imp_ing.release()
cv2.destroyALLWindows()
