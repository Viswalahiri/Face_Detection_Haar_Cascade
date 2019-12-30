# Importing opencv
import cv2
# Importing operating system functionality
import os
# Import image utility library
from imutils import paths

def face_finder(faces,image,path1):
  counter = 0
  for (x, y, w, h) in faces:
  # Defining alpha as a transparency factor.
    alpha = 1 

    # Create overlay, which is a copy of the colored image.
    overlay = image.copy()

    # Draw rectangle of green color with border width 1px
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), 1)

    alpha = 0  # Transparency factor.

    # Following line overlays transparent rectangle over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    
    # Add transparency to the rectangle that's been added onto origninal image.
    cv2.addWeighted(overlay, alpha, image, 1 - alpha,0, image)

    # Following line overlays transparent rectangle over the image

    # image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    roi_color = image_new[y:y + h, x:x + w]

    # Change Path
    os.chdir(path1)
    if(cv2.imwrite(str(w) + str(h)  +'_faces.jpg', roi_color)):
        counter+=1
  if(counter == 0):
    print("No faces were detected and pushed.")
  elif(counter==1):
    print("A face has been detected and pushed.")
  else:
    print("Faces have been detected and pushed.")
