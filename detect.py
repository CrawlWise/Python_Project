import cv2, glob

#Load the images
all_images = glob.glob("*.jpg")

# Load the face detector
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detects many faces of different sizes in the input image
for image in all_images:
     img = cv2.imread(image)

# Convert to grayscale
     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
     faces = detect.detectMultiScale(gray_img, 1.1, 5)

     for (x, y, w, h) in faces:
# To draw rectangle around different faces
         final_img = cv2.rectangle(img, (x,y), (x+w,y+h), (0, 280, 0), 3)

#Show the result
     cv2.imshow("Face Detection", final_img)
     cv2.waitKey(2000)

# Close the window
     cv2.destroyAllWindows