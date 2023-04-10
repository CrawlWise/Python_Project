'''import the module to work with, where globe is a module
 that allow us to access all diferent files in our folder'''
import cv2, glob

'''Fetch all my images by giving the file exact name and location
the module globe has a function called globe which takes the patch of the particular file we want to fetch)
* means all file format that ends with jpeg'''
all_pics = glob.glob("*.jpeg")

'''the haarcascade_frontalface_default.xml file is used to detect faces,
shearch for other haarcascade filetype if you need to do other things like detect smile, eye etc'''
getpics = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

'''a for loop to select image from the created variable to detect faces'''
for image in all_pics:
    '''read/detect the frame from the particular picture, store the result in a variable img'''
    img = cv2.imread(image)
    '''convert the picture into grayscale image'''
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''we will now do the actual face detection'''
    faces = getpics.detectMultiScale(gray_img, 1.1, 5)

    '''extract the data using a for loop'''
    for (x, y, w, h) in faces:
        '''draw a rectangle on detected faces with 4inh border lines and 275, 275, 255 are border colors, store the
        final result in a variable name final_pics'''
        final_pics = cv2.rectangle(img, (x,y), (x+w,y+h), (275, 275, 255), 4)

    '''show my pictures, '''
    cv2.imshow("ManyFacesDetect", final_pics)

    '''The waitKey is a function that hold the picture for specified time e,g 1500 milliseconds'''
    cv2.waitKey(1500)
    '''destroy or close all opened windows'''
    cv2.destroyAllWindows