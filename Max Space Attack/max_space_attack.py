import os
from itertools import product
from string import ascii_lowercase
import threading

def fillSpace(list,f):
        for word in list:
                for word2 in list:
                        f.write(word.capitalize()+word2+"\n")
                        f.write(word+word2+"\n")




def main():
	
	words = []

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	words = ["".join(i) for i in product(ascii_lowercase, repeat = 4)]

	f = open("/home/testaccount2/passwords","w")
	fillSpace(words,f)


main()
