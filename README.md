Name of group:   Project group 1
Team Members:  Susan Owoeye
		  	 Damilola Olufisayo
		           Bolurin Falola
		          Kayode Folorunso
		          Ofomiyuaju Elizabeth
Assignment: 
	Create a branch and name it.
	Face detection
	Pulling and Pushing to our deliverables to main branch.

Creating a branch in a GitHub repository
To create a branch in a GitHub repository, the following steps need to be taken:
	Navigate to the repository where you want to create the branch at the top left hand corner of the system.
	Locate and click on the "Branch master" dropdown menu that is located near the top left of the repository page.
	Give a descriptive matching or fitting name for your new branch in the "Find or create a branch" field of the page.
	Then click "Create branch" and click Enter to create the new branch.
	Once the new branch is created, switch to it by using the dropdown menu
	Changes can be made to the code.
	Commit the changes and 
NOTE: All the above is better done on the local Machine
	then push changes to the new branch using the git push command in your terminal.
FACE DETECTION: This is a simple Python coding that demonstrates how to detect faces in an image using the OpenCV library.
There is need to have Python and OpenCV installed on the machine. 
This (OpenCV)can be installed using pip: OpenCV-python

WAYS TO PERFORM FACE DETECTION
There are several ways to perform face detection.. Some of the popular approaches for face detection are:
1.	Convolutional Neural Networks (CNNs): CNNs are deep learning-based algorithms that have shown impressive results in face detection tasks. They can be trained to detect faces in images with high accuracy and robustness.
2.	HOG (Histogram of Oriented Gradients) + SVM (Support Vector Machine): HOG is a feature extraction algorithm that extracts local features from an image. SVM is a machine learning-based algorithm that can classify these features as face or non-face. Together, these algorithms can be used for face detection.
3.	Dlib: Dlib is a popular open-source library that provides a face detection algorithm based on a combination of HOG and SVM. It is known for its high accuracy and real-time performance.
4.	DeepFace: DeepFace is a deep learning-based face recognition system developed by Facebook. It uses a multi-layer neural network to perform face detection and recognition with high accuracy.
5.	MTCNN (Multi-Task Cascaded Convolutional Networks): MTCNN is a deep learning-based algorithm that detects faces by first locating the bounding box of the face in the image and then refining the box to accurately localize the face. It can detect faces at different scales and orientations.
6.	Haar Cascade classifier approach
These are just a few examples of the different approaches available for face detection. The choice of the algorithm depends on the specific requirements of your application, such as accuracy, speed, and complexity.
import cv2

Load the cascade classifier which is
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Return the bounding boxes of the detected faces
    return faces
You can then call this function from your own Python script to detect faces in an image:
from face detection, import detect_faces

# Detect faces in an image
faces = detect_faces('image.jpg')

# Print the bounding boxes of the detected faces
for (x, y, w, h) in faces:
    print(f"Found a face at ({x}, {y}) with width {w} and height {h}."

