#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
def twiddle(p= [0,0,0], dp=[1,1,1], tol = 0.2): #Make this tolerance bigger if you are timing out!
############## ADD CODE BELOW ####################

    best_err= run(p[0])
    print "Init best_err", (1-best_err)*100,"%", "p:", p,"dp:", sum(dp)
    n=0
    while sum(dp) >tol:
        for i in range(len(p)):
            p[i]+=dp[i]
            print "p is:", p
            err = run(p[0])
            
            if err < best_err:
                best_err = err
                dp[i]=int(1.1* dp[i]) 
                print "dp", sum(dp)
            else:
                p[i]-=2*dp[i]
                print "else dp", sum(dp)
                err=run(p[0])
                if err< best_err:
                    best_err=err
                    dp[i]=int(1.05* dp[i])
                else:
                    p[i] +=dp[i]
                    dp[i]=int(0.9* dp[i]) 
            
        n+=1
        print 'Twiddle #',n, p,'-->', (1-best_err)*100,"%", "dp:", sum(dp)
                
    return p[0]




def runClassifier(clf, clfName):
    from time import time
    t0 = time()
    clf.fit(features_train, labels_train)
    print clfName, "training time:", round(time()-t0, 3), "s"
    ### measure the accuracy 
    accuracy = clf.score(features_test, labels_test)
    print "accuracy:",accuracy*100,"%"
    ### visualization code (prettyPicture) to show you the decision boundary

    try:
        prettyPicture(clf, features_test, labels_test,clfName)
    except NameError:
        print "no pic"

def run(p):
    #print "---frm run, p is",p
    #clf = SVC(kernel='rbf', C=p)
    clf= ensemble.RandomForestClassifier(n_estimators = 50)
    clf.fit(features_train, labels_train)
    accuracy = clf.score(features_test, labels_test)
    #print "---err is:", 1-accuracy
    return  1-accuracy
        
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(weights ="distance")
runClassifier(clf, "KNeighborsClassifier")


from sklearn import ensemble
clf= ensemble.RandomForestClassifier(n_estimators = 50)
runClassifier(clf, "RandomForestClassifier")

from time import time
t0 = time()
param =twiddle( [400], [200], 1)
print  "Twiddle time:", round(time()-t0, 3), "s"
print "Twiddle--", param

clf= ensemble.RandomForestClassifier(n_estimators = param)
runClassifier(clf, "TWIDDLE - RandomForestClassifier")


clf= ensemble.AdaBoostClassifier(n_estimators=50, learning_rate = 1.9)
runClassifier(clf, "AdaBoostClassifier")


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
runClassifier(clf, "GaussianNB")

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split= 10.2)
runClassifier(clf, "DecisionTreeClassifier")

from sklearn.svm import LinearSVC
clf = LinearSVC()
runClassifier(clf, "SVC")


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
