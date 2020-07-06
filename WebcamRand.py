from PIL import Image
import hashlib
import cv2
import numpy as np
import random

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
trim = input("number of digits eg. if you input 5 the value could be 00000 to 99999 ")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png".format()
        cv2.imwrite(img_name, frame)
        BLOCKSIZE = 65536
        hasher = hashlib.sha3_512()
        with open('opencv_frame.png' , 'rb') as image:
            buf = image.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = image.read(BLOCKSIZE)
                print(hasher.hexdigest())
                n = int(hasher.hexdigest(), base = 16)
		numstring = str(n)
		trunk = (numstring[:(int(trim))])
		print (trunk)

                
cam.release()

cv2.destroyAllWindows()
