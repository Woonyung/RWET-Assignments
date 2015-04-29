#
# RWET FINAL ASSIGNMENT
# Apr 26, 2015
# Poem generated from Yelp reviews

# test with TextBlob
# instructify thing + recipe verbs

###################################################

# http://www.yelp.com/biz/curry-ya-new-york?sort_by=rating_asc
import urllib
from bs4 import BeautifulSoup
from textblob import TextBlob
import random
import sys


# empty lists
recipeVerbs = list()

verbs = list()
nounPhrases = list()


# recipe verbs from the text file
myFile = open('RecipeverbList.txt')
r_verbs = myFile.readlines()

for r_verb in r_verbs:
	recipeVerbs.append(r_verb.replace('\n', ''))


# url endpoints
# restaurant = 'http://www.yelp.com/biz/curry-ya-new-york'
restaurant = sys.argv[1] # take the yelp url argument 
url_good = restaurant +'?sort_by=rating_desc'
url_bad = restaurant +'?sort_by=rating_asc'

##########
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# print tag

def getTexts(url):

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
	    if idx < 9: 
	    	blob = TextBlob(val.getText())

	    	###  APPEND NOUN PHRASES
	    	# print blob.noun_phrases[0]
	    	for i in xrange(1,len(blob.noun_phrases)): 
	    		nounPhrases.append(blob.noun_phrases[i])

	    	###  VERB
	    	for word, tag in blob.tags:
	    		if tag == 'VB':
	    			# print word
	    			verbs.append(word.lemmatize())
	# print nounPhrases
	# print verbs

	for i in range(1, 11):
		print str(i) + ". " + random.choice(recipeVerbs).title() + " " +
				random.choice(nounPhrases)

# getTexts(url_bad)
getTexts(url_bad)