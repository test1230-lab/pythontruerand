import hashlib
import numpy
import random

x = input("input the file name if it is located in the same dir as the py file or input the image dir if not ")
BLOCKSIZE = 65536
hasher = hashlib.sha3_512()
with open((x) , 'rb') as image:
	buf = image.read(BLOCKSIZE)
	hasher.update(buf)
	buf = image.read(BLOCKSIZE)
	n = int(hasher.hexdigest(), base = 16)
	print (n)
