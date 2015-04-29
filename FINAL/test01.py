#
# RWET FINAL ASSIGNMENT
# Apr 26, 2015
# Poem generated from Yelp reviews

# using nltk
# test with the part of speech
# and test with the pattern from midterm
###################################################

# http://www.yelp.com/biz/curry-ya-new-york?sort_by=rating_asc
import urllib
from bs4 import BeautifulSoup
import nltk
import random

# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# print tag


# adjective lists
goodListADJ = list()
badListADJ = list()

# noun lists
goodListNoun = list()
badListNoun = list()

# url endpoints
endPoint = 'http://www.yelp.com/biz/curry-ya-new-york?sort_by='
url_good = endPoint + 'rating_desc'
url_bad = endPoint + 'rating_asc'

def getTexts(url, adjList, nounList):
	data = urllib.urlopen(url).read()
	soup = BeautifulSoup(data)
	reviewWrapper = soup.select('.review-wrapper')

	# <p itemprop="description" lang="en">
	inputTag = soup.findAll("p", {"itemprop":"description"})
	# output = inputTag[0].getText()
	# print output

	# iterates all itemprop tags
	for idx, val in enumerate(inputTag):
		# looping only 5 reviews from the top
	    if idx < 4: 
	    	words = nltk.word_tokenize(val.getText()) #tokenize
	    	tagged = nltk.pos_tag(words) # part of speech
		
		# depends on the POS, added words to the list
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



# and pulling out adjective, nouns and make new lists out of it 
getTexts(url_good, goodListADJ, goodListNoun)
getTexts(url_bad, badListADJ, badListNoun)


print random.choice(goodListADJ) + " " + random.choice(badListNoun) + " " + random.choice(goodListADJ) + " " + random.choice(badListNoun)
print random.choice(badListADJ) + " " + random.choice(goodListNoun) + " " + random.choice(badListADJ) + " " + random.choice(goodListNoun)
print random.choice(badListADJ) + " " + random.choice(badListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(goodListNoun)
print random.choice(goodListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(badListADJ) + " " + random.choice(badListNoun)

print random.choice(badListADJ) + " " + random.choice(goodListNoun) + " " + random.choice(badListADJ) + " " + random.choice(goodListNoun)
print random.choice(goodListADJ) + " " + random.choice(badListNoun) + " " + random.choice(goodListADJ) + " " + random.choice(badListNoun)
print random.choice(goodListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(badListADJ) + " " + random.choice(badListNoun)
print random.choice(badListADJ) + " " + random.choice(badListADJ) + " " + random.choice(goodListADJ) + " " + random.choice(goodListNoun)
