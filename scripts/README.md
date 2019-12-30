## About The Haar-Cascade Face Detection Algorithm

The Haar-Cascade Face Detection Algorithm is a sliding-window type of algorithm that detects objects based upon its features.

### Haar Face Features

The Haar-Cascade model, employs different types of feature recognition that include the likes of
- Size and location of certain facial features. To be specific, nose bridge, mouth line and eyes.
- Eye region being darker than upper-cheek region.
- Nose bridge regio being brighter than eye region.

### Intel's 'haarcascade_frontalface_default.xml'

This 'XML'  [file](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) contains a pre-trained model that was created through extensive training and uploaded by Rainer Lienhart on behalf of Intel in 2000. 

Rainer's model makes use of the Adaptive Boosting Algorithm (AdaBoost) in order to yield better results and accuracy.


## Image-Related Functions of OpenCV

- ```cv2.imread(fileName, flag)```
  - Parameters
    - ```fileName``` (```str```) –
    - ```flag``` (```int```) – Option.
      - ```cv2.IMREAD_COLOR : Color ```
      - ```cv2.IMREAD_GRAYSCALE : Grayscale ```
      - ```cv2.IMREAD_UNCHANGED : alpha channel ```
  - Returns image
  - Return type ```numpy.ndarray```

- ```cv2.imwrite(fileName, image)```
  - Parameters
    - ```fileName``` (```str```) 
    - ```image```

- ```cv2.imshow(title, image)```
  - Parameters
    - ```title``` (```str```)
    - ```image``` (```numpy.ndarray```)
    
- ```cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)```
  - Parameters
    - ```src ```- (path of the source)
    - ```COLOR_BGR2GRAY``` - ```COLOR_BGR2GRAY``` implies to the system that it ought to convert it to grayscale
  - Returns greyscale image 
  - Return type ```numpy.ndarray```
  
- ```cv2.detectMultiScale(image, cascade, scale_factor, min_neighbors, flags, min_size)```
    - Parameters:	
      - ```cascade``` – Haar classifier cascade (OpenCV 1.x API only). It can be loaded from XML or YAML file using Load(). When the cascade is not needed anymore, release it using cvReleaseHaarClassifierCascade(&cascade).
      - ```image``` – Matrix of the type CV_8U containing an image where objects are detected.
      - ```objects``` – Vector of rectangles where each rectangle contains the detected object.
      - ```scaleFactor``` – Parameter specifying how much the image size is reduced at each image scale.
      - ```minNeighbors``` – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
      - ```flags``` – Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.
      - ```minSize``` – Minimum possible object size. Objects smaller than that are ignored.
      - ```maxSize``` – Maximum possible object size. Objects larger than that are ignored.
    - Returns faces
    - Return type ```numpy.ndarray```
 
 - ```cv2.rectangle(img,pt1,pt2,rec,color,thickness,lineType,shift)```
    - Parameters:
      - ```img``` – Image.
      - ```pt1``` – Vertex of the rectangle.
      - ```pt2``` – Vertex of the rectangle opposite to pt1 .
      - ```rec``` – Alternative specification of the drawn rectangle.
      - ```color``` – Rectangle color or brightness (grayscale image).
      - ```thickness``` – Thickness of lines that make up the rectangle. Negative values, like CV_FILLED , mean that the function has to draw a filled rectangle.
      - ```lineType``` – Type of the line. See the line() description.
      - ```shift``` – Number of fractional bits in the point coordinates.

  - ```cv2.addWeighted(src1, alpha, src2, beta, gamma, dst)```
    - Parameters:	
      - ```src1``` – first input array.
      - ```alpha``` – weight of the first array elements.
      - ```src2``` – second input array of the same size and channel number as src1.
      - ```beta``` – weight of the second array elements.
      - ```dst``` – output array that has the same size and number of channels as the input arrays.
      - ```gamma``` – scalar added to each sum.
      
# References

https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html
https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html
