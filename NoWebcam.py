import hashlib
import numpy
import random
#if given the EXACT same image file it will give the same number. 
#This is why a webcam is recommended. The webcam has noise from the sensor that helps randomize the number, as well as moving objects in the frame.
x = input("input the file name if it is located in the same dir as the py file or input the image dir if not ")
BLOCKSIZE = 65536
hasher = hashlib.sha3_512()
with open((x) , 'rb') as image:
	buf = image.read(BLOCKSIZE)
	hasher.update(buf)
	n = int(hasher.hexdigest(), base = 16)
	print (n)
