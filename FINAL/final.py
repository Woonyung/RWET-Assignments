#
# RWET FINAL ASSIGNMENT
# Apr 28, 2015
# Poem generated from Yelp reviews

# test with TextBlob
# make weird recipe with bad reviews of the restaurant

###################################################

import urllib
from bs4 import BeautifulSoup
from textblob import TextBlob
import random
import sys

# empty lists
recipeVerbs = list()
myFile = open('RecipeverbList.txt')
r_verbs = myFile.readlines()

for r_verb in r_verbs:
	recipeVerbs.append(r_verb.replace('\n', ''))

amountList = ['1/2', '1', '2', '4', '8']
measurementWord = [ 'teaspoon','cup', 'gallon']

verbs = list()
adjectives = list()
nounPhrases = list()

###
ingredientList = list()

###################################################

# url endpoints
# baseURL = 'http://www.yelp.com/biz/curry-ya-new-york'
baseURL = sys.argv[1] # take the yelp url argument 
url_good = baseURL +'?sort_by=rating_desc'
url_bad = baseURL +'?sort_by=rating_asc'

##########
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
	    if idx < 20: 
	    	blob = TextBlob(val.getText())

	    	###  APPEND NOUN PHRASES
	    	# print blob.noun_phrases[0]
	    	for i in xrange(1,len(blob.noun_phrases)): 
	    		nounPhrases.append(blob.noun_phrases[i])

			# get adjectives from review
			for word, tag in blob.tags:
				if tag == 'JJ':
					adjectives.append(word.lower())

	for i in range (1, 6):
		amount = random.choice(amountList)
		if (amount == '1/2') or (amount == '1'):
			ingredient = amount + " " + random.choice(measurementWord) + " of " + random.choice(adjectives)+ " " + random.choice(nounPhrases)
		else:
			ingredient = amount + " " + random.choice(measurementWord) + "s of " + random.choice(adjectives) + " " + random.choice(nounPhrases)

		ingredientList.append(ingredient)


	#### at the end, print everything
	print "==========================="
	print "Ingredient: "
	for ingredient in ingredientList:
		if ingredient == ingredientList[-1]:
			print ingredient + "." # last element

		else: print ingredient + ","
	print "==========================="

	print "1. " + random.choice(recipeVerbs).title() + " " + random.choice(ingredientList) + " and " + random.choice(recipeVerbs).lower() + " " + random.choice(ingredientList) + "."
	print "2. " + random.choice(recipeVerbs).title() + " " + random.choice(ingredientList) + " until it gets " + random.choice(adjectives) + "."
	print "3. " + random.choice(recipeVerbs).title() + " with " + random.choice(adjectives) + " " + random.choice(ingredientList) + "."
	print "4. " + random.choice(recipeVerbs).title() + " " + random.choice(ingredientList) + "."
	print "5. " + "Finally, " + random.choice(recipeVerbs).lower() + " "+ random.choice(ingredientList) + "."

	
###################################################
# CALL FUNCTION
getTexts(url_bad)

