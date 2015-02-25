#
# RWET Assignment #2
# Feb 25, 2015
# making digital cutup 

###################################################

import sys
import re

# arguments passed on command line
bestReview = sys.argv[1]
worstReview = sys.argv[2]

# make a blank list
bestList = list()
worstList = list()
mashUp = list()


# bestWords = bestList[::2] # only even number
# worstWords =  worstList[1::2] # only odd number


for line in open(bestReview):
	line = line.strip() # remove all white space
	words = re.split('\s+', line)
	bestList += words

# looping through bestList, put only even elements to the Mashups
for index, word in enumerate(bestList):
    # print index, word
    if index % 2 == 0 :
    	# print index # 0, 2, 4
    	mashUp.insert( index ,word)


######################################################

for line in open(worstReview):
	line = line.strip()
	words = re.split('\s+', line)
	worstList += words

# looping through worstList, put only odd elements to the Mashups
for index, word in enumerate(worstList):
	if index % 2  == 0 :
		print "there is nothing"
	else : 
		print index
		mashUp.insert(index, word)


print mashUp
