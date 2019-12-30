# Importing opencv
import cv2
# Importing operating system functionality
import os
# Import image utility library
from imutils import paths
import face_finder
def harr(path,path1):
  # path specifies the location of the photo that is to be analysed.

  # For each photo's path in the path specified, read 'image' as t
  for imagePath in paths.list_images(path):
      # IMREAD_IGNORE_ORIENTATION implies that there is no change in orientation of the photo
      # IMREAF_COLOR implies to the system that it ought to be read in color
      image = cv2.imread(imagePath, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)

      # COLOR_BGR2GRAY implies to the system that it ought to convert it to grayscale
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Create faceCascade classifier object and load pre-trained Haar-Cascade Model into it.
      faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
      
      # Detects objects of different sizes in the image, and returns them in the form of boxes.
      faces = faceCascade.detectMultiScale(
          # gray is the image in which the converted greyscale image resides.
          gray,

          # Changes the scale of the each image, thus making the resized image more visible to the algorithm.
          scaleFactor=1.3,
          
          # Tweaking this value up decreases the number of false positives, but if too overset, then gets rid of true positives
          minNeighbors=3,
          #Objects smaller than x*x pixels in minsize=(x,x) are ignored.
          minSize=(20,20)
      )
      face_finder.face_finder(faces,image,path1)
