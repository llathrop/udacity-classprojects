#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import random
import numpy


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop("TOTAL", 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")



########
cleaned_data = []
salaryList =[]
bonusList=[]

for point in data:
    salary = point[0]
    bonus = point[1]
    cleaned_data.append((salary,bonus))
    salaryList.append(salary)
    bonusList.append(bonus)

salaryList = numpy.reshape( numpy.array(salaryList), (len(salaryList), 1)) 
bonusList =  numpy.reshape( numpy.array(bonusList), (len(bonusList), 1)) 

from sklearn.cross_validation import train_test_split
salary_train, salary_test, bonus_train, bonus_test = train_test_split(salaryList, bonusList, test_size=0.1, random_state=42)

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(salary_train,bonus_train)
print reg.score(salary_test, bonus_test ) 

predictions=reg.predict(salaryList)

matplotlib.pyplot.plot(salaryList, predictions, color="blue")
cleaned_data = []

for i in range(len(salaryList)):
    cleaned_data.append( (salaryList[i][0],bonusList[i][0],abs(bonusList[i][0]-predictions[i][0])))
    
cleaned_data.sort(key=lambda tup: tup[2])  

for c in cleaned_data:
    print c

print "end"
outliers=[]
for i in range(int(len(cleaned_data)*.1)):
    outliers.append( cleaned_data.pop())
#print outliers

for d in data_dict:
    for o in outliers:
        if data_dict[d]["salary"]==o[0]:
            print d,"Outlier bonus", data_dict[d]["bonus"], "diff in pred:",o[2]


matplotlib.pyplot.show()

#EOF