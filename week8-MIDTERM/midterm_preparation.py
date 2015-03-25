#
# RWET MIDTERM ASSIGNMENT
# Mar 23, 2015
# Poem from Amazon comments

###################################################
import sys
import re
import random
import nltk


# arguments passed on command line
positiveReview = sys.argv[1]
negativeReview = sys.argv[2]

# make a blank list
goodList = list()
badList = list()

goodListADJ = list()
badListADJ = list()

# function for making word lists
def addListofWords(inputs, newList):
	for line in open(inputs):
		words = re.split('\s+', line)
		newList += words

addListofWords(positiveReview, goodList)
addListofWords(negativeReview, badList)


# print tagged[0] # print out part of speech- first

# looping through with index number
# and pulling out adjective and make new lists out of it 
def makeADJList(list, adjList):
	tagged = nltk.pos_tag(list)
	for index, pos in enumerate(tagged):
		if tagged[index][1] == 'JJ':
			print tagged[index][0]
			adjList.append(tagged[index][0])

# taggedGood = nltk.pos_tag(goodList)
# taggedBad = nltk.pos_tag(badList)
makeADJList(goodList, goodListADJ)

print goodListADJ
