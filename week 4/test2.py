#
# RWET Assignment #2
# Feb 25, 2015
# making digital cutup 

###################################################

import sys
import re

# make a blank list
bestList = list()
worstList = list()
mashUp = list()


# bestWords = bestList[::2] # only even number
# worstWords =  worstList[1::2] # only odd number

# function for making word lists
def addListofWords(inputs, newList):
	for line in open(inputs):
		line = line.strip() # remove all white space
		words = re.split('\s+', line)
		newList += words

addListofWords('review_best1.txt', bestList)
addListofWords('review_worst1.txt', worstList)


# looping through bestList, put only even elements to the Mashups
for index, word in enumerate(bestList):
    if index % 2 == 0 :
    	# print index # 0, 2, 4
    	mashUp.insert( index ,word)

# looping through worstList, put only odd elements to the Mashups
for index, word in enumerate(worstList):
	if index % 2  == 0 :
		print ""
	else : 
		mashUp.insert(index, word)

print " ".join(mashUp)
