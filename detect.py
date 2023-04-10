import cv2, glob

all_images = glob.glob("*.jpg")
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_images:
 # Detects many faces of different sizes in the input image
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray_img, 1.1, 5)

    for (x, y, w, h) in faces:
# To draw rectangle in the different faces
        final_img = cv2.rectangle(img, (x,y), (x+w,y+h), (500, 500, 0), 2)

    cv2.imshow("Face Detection", final_img)
    cv2.waitKey(2000)

# Close the window
    cv2.destroyAllWindows