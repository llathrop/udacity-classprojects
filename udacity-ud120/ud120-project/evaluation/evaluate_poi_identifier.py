#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


### it's all yours from here forward!  
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels,test_size=0.3, random_state=42)

poi = 0
for t in labels_test:
    if t == 1:
        poi+=1
        
print "poi:",poi

   
print "total:", len(labels_test)

from sklearn import tree
clf = tree.DecisionTreeClassifier()

from time import time
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
### measure the accuracy 
accuracy = clf.score(features_test, labels_test)
print "accuracy:",accuracy*100,"%"