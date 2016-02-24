#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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




#########################################################
### your code goes here ###
from sklearn import tree

#ten% training (for speed)
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


clf = tree.DecisionTreeClassifier(min_samples_split= 40)

#### fit model to data 
# Time an operation:
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

#### store your predictions in a list named pred
pred = clf.predict(features_test)
### measure the accuracy 
accuracy = clf.score(features_test, labels_test)
print "accuracy:",accuracy

print len(features_train[0])


#########################################################


