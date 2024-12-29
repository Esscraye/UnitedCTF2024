#!/usr/bin/python3

# python 7z_bruteforce.py rockyou.txt test.7z

import concurrent.futures
import os
import subprocess
import sys

FNULL = open(os.devnull, 'w')
found = False

def try_password(aPassword, aFile):
	global FNULL, myExecutor, found
	try:
		if not found:
			print(aPassword)
			myRet = subprocess.call(["7z", "t", "-p" + aPassword, aFile], stdout=FNULL, stderr=subprocess.STDOUT) 
			if myRet == 0:
				print ("The password is: " + aPassword)
				found = True
				# TODO: kill process
	except Exception as ex:
		print(str(ex))

myFilename = sys.argv[2]
myPasswordFile = sys.argv[1]

print ("File to crack: " + myFilename)
print ("Password list: " + myPasswordFile)

myFile = open(myPasswordFile, "rt")
myExecutor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

# Test a Password
#myExecutor.submit(try_password, "123456", myFilename)

try:
	for myLine in iter(myFile):
		myPassword = myLine.strip('\n')
		myExecutor.submit(try_password, myPassword, myFilename)
except Exception as ex:
	print(str(ex))