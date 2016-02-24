#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#print features_train,'\n',labels_train

#########################################################
### your code goes here ###
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

t0 = time()
accuracy = clf.score(features_test, labels_test)
print "score time:", round(time()-t0, 3), "s"

 
print pred, accuracy


import matplotlib
from matplotlib import pyplot as plt

for i in range(len(features_train)):
    label= 'co'
    if labels_train[i] ==0:
        label= 'mo'
    plt.plot(features_train[i], label)

for i in range(len(features_test)):
    label= 'bo'
    if labels_test[i] ==0:
        label= 'ro'
    plt.plot(features_test[i], label)
plt.show()

#########################################################


