import cv2
import numpy as np

kernel1 = np.array([[1,1,1],
                               [1,1,1],
                               [1,1,1]])*(1/9)

kernel2 = np.array([[1,2,1],
                               [2,4,2],
                               [1,2,1]])*(1/16)
                                
img = cv2.imread('quote.jpg')
#dst1 = cv2.filter2D(img,-1,kernel1)
#dst2 = cv2.filter2D(img,-1,kernel2)
dst3 = cv2.blur(img,(3,3))
dst4 = cv2.blur(img,(11,11))

while True:
    cv2.imshow('Quote Image - Original',img)
    #cv2.imshow('Blur Image',dst1)
    #cv2.imshow('Gaussian Blur Image',dst2)
    cv2.imshow('Normal Blur Image',dst3)
    cv2.imshow('Normal Blur Image2',dst4)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()




