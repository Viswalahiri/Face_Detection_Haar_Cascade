# Importing opencv
import cv2
# Importing operating system functionality
import os

from os import path
# Import image utility library
from imutils import paths

# Import harr.py
import harr

if __name__ == "__main__":
  print("Enter Path Where Images Exists.")
  o = input()
  # Check if o exists
  if (not path.exists(o)):
    print("Path doesn't exist.")
  else:
    print("Enter Path Where You Would Like to Push.")
    p = input()
    # Check if p exists
    if (not path.exists(p)):
      print("Path doesn't exist.")
    else:
      # Use function harr from harr.py
      harr.harr(o,p)
