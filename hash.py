from PIL import Image
import hashlib
import cv2
import numpy as np
import random
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

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
        img_name = "opencv_frame.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("written!".format(img_name))
        md5hash = hashlib.md5(Image.open('opencv_frame.png').tobytes())
        print(md5hash.hexdigest())
        pogger = (md5hash.hexdigest())
        random.seed(pogger)
        y = input("start range ")
        x = input("send range ")
        print("First iteration  - ", random.randint(y, x)) 
cam.release()

cv2.destroyAllWindows()

