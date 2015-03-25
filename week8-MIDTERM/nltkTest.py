import sys
import random
import nltk

#nltk.download('all'): to download all modules in nltk library

sentence = "At eight o'clock on Thursday morning. Arthur didn't feel very good."
tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)
print type(tagged[0]) #turple
print tagged[0][0]
