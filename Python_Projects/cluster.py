# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:28:40 2016

@author: Vamsi
"""

# -*- coding: utf-8 -*-

from __future__ import print_function
import string
import nltk, sklearn, string, os
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans

# Preprocessing text with NLTK package
token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems
###########################################################################
# Loading and preprocessing text data
print("\n Loading text dataset:")
shakes = open('pro.txt', 'r')
text = shakes.read()
lowers = text.lower()
no_punctuation = lowers.translate(string.maketrans(string.punctuation,string.punctuation))
token_dict = no_punctuation
###########################################################################
true_k = 3 # *
print("\n Performing stemming and tokenization...")
vectorizer = TfidfVectorizer(tokenizer=tokenize)
X = vectorizer.fit_transform(token_dict)
print(tokenize(token_dict))
print("n_samples: %d, n_features: %d" % X.shape)
print()
###############################################################################
# Do the actual clustering
km = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=1)
y=km.fit(X)
print(km)

print("Top terms per cluster:")
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print(order_centroids[0,:10])