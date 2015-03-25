#
# RWET MIDTERM ASSIGNMENT
# Mar 23, 2015
# Poem from Amazon comments

###################################################
import sys
import random
import nltk


# arguments passed on command line
positiveReview = sys.argv[1]
negativeReview = sys.argv[2]

# make a blank list
goodList = list()
badList = list()

# adjective lists
goodListADJ = list()
badListADJ = list()

# noun lists
goodListNoun = list()
badListNoun = list()

#####
## add noun list..

# function for making word lists
def addListofWords(inputs, newList):
	for line in open(inputs):
		words = nltk.word_tokenize(line)
		newList += words

addListofWords(positiveReview, goodList)
addListofWords(negativeReview, badList)


# looping through with index number
# and pulling out adjective and make new lists out of it 
def makePosList(list, adjList, nounList):
	tagged = nltk.pos_tag(list)
	for index, pos in enumerate(tagged):
		if tagged[index][1] == 'JJ': # if it finds adjectives
			# print tagged[index][0] # print out adjectives
			adjList.append(tagged[index][0])
		if tagged[index][1] == 'JJR':
			adjList.append(tagged[index][0])
		if tagged[index][1] == 'JJS':
			adjList.append(tagged[index][0])

		if tagged[index][1] == 'NN':
			nounList.append(tagged[index][0])
		if tagged[index][1] == 'NNS':
			nounList.append(tagged[index][0])

# make the list of the words from good and bad reviews
makePosList(goodList, goodListADJ, goodListNoun)
makePosList(badList, badListADJ, badListNoun)

# print goodListADJ
# print goodListNoun

# pick the random word out of them
print random.choice(goodListADJ) + " " + random.choice(badListNoun) + " " + random.choice(goodListADJ) + " " + random.choice(badListNoun)
print random.choice(badListADJ) + " " + random.choice(goodListNoun) + " " + random.choice(badListADJ) + " " + random.choice(goodListNoun)
print random.choice(badListADJ) + " " + random.choice(badListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(goodListNoun)
print random.choice(goodListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(badListADJ) + " " + random.choice(badListNoun)

print random.choice(badListADJ) + " " + random.choice(goodListNoun) + " " + random.choice(badListADJ) + " " + random.choice(goodListNoun)
print random.choice(goodListADJ) + " " + random.choice(badListNoun) + " " + random.choice(goodListADJ) + " " + random.choice(badListNoun)
print random.choice(goodListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(badListADJ) + " " + random.choice(badListNoun)
print random.choice(badListADJ) + " " + random.choice(badListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(goodListNoun)
