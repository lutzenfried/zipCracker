#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Author : ### lutzenfried ###
#Use only for educational purpose

#Modify zip_file : Put zip file path /home/user/documents/file.zip
#Modify password_file : Put password file path /home/user/documents/wordlist.txt
#Modify path : Put output file path /home/user/documents/output.txt

from zipfile import ZipFile

zip_file = '%ZIP_FILE_PATH%'
password_file = '%PASSWORD_FILE_PATH%'

content = []
listWithoutN = []
 
with open(password_file, encoding="utf8") as f:
	content = f.readlines()
	listWithoutN = list(map(lambda x:x.strip(),content))
	
	for i in listWithoutN:
		try:
			with ZipFile(zip_file) as zf:
				zf.extractall(path='%PATH_TO_EXTRACT%', pwd=bytes(i,'utf-8'))
				print ("+++++++++++++++ Valid password found: ", i, "+++++++++++++++")
				validPassword =  i
		
		except:
			print ("Attempt failed with password : ", i)
			pass
			                                               
print ("Correct password for decrypt ZIP file is ------>", validPassword)
