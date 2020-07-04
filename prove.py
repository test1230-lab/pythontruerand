from PIL import Image
import hashlib
import cv2
import numpy as np
import random

x = input("file name if it is located in the same dir as the py file or the image dir if not ")
BLOCKSIZE = 65536
hasher = hashlib.sha3_512()
with open((x) , 'rb') as image:
	buf = image.read(BLOCKSIZE)
	while len(buf) > 0:
		hasher.update(buf)
		buf = image.read(BLOCKSIZE)
		print(hasher.hexdigest())
                
