import string

dict = open("words.txt","r")
altDict = []
for word in dict:
    altDict.append(word)
    if(word.capitalize() not in altDict):
       altDict.append(word.capitalize())
print("Part 1 Done")
print(len(altDict))
newDict = open("passwords.txt","w")
dictList = []
for word in altDict:
    #if (len(word) == 1):
        #for word2 in altDict:
           # newDict.write(word + word2)
    #if (len(word) == 2):
     #   for word2 in altDict:
     #       newDict.write(word + word2)
    if (len(word) == 3 ):
        for word2 in altDict:
            if (word + word2 not in dictList and len(word + word2) > 7):
            	newDict.write(word + word2)
            	dictList.append(word + word2)
    	        print("Phase 1 Done")
    if (len(word) == 4 ):
    	for word2 in altDict:
            if (word + word2 not in dictList and len(word + word2) > 7):
            	newDict.write(word + word2)
            	dictList.append(word + word2)
    	        print("Phase 2 Done")
    if (len(word) == 5 ):
        for word2 in altDict:
            if (word + word2 not in dictList and len(word + word2) > 7):
            	newDict.write(word + word2)
            	dictList.append(word + word2)
    	        print("Phase 3 Done")
    if (len(word) == 6 ):
        for word2 in altDict:
            if (word + word2 not in dictList and len(word + word2) > 7):
            	newDict.write(word + word2)
            	dictList.append(word + word2)
    	        print("Phase 7 Done")
    if (len(word) == 7):
        for word2 in altDict:
            if (word + word2 not in dictList and len(word + word2) > 7):
            	newDict.write(word + word2)
            	dictList.append(word + word2)
            	print("phase done")
	        
    #print("Phase 1 Done")
    if (len(word) > 7 and word not in dictList):
        newDict.write(word)
        dictList.append(word)
