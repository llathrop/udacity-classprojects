#!/cygdrive/c/Anaconda2/python
#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")
import math

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, test_classifier


from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn import linear_model, decomposition, datasets, ensemble
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer,precision_score, recall_score, f1_score, average_precision_score, accuracy_score
from sklearn.cross_validation import train_test_split, StratifiedShuffleSplit
from sklearn.preprocessing import MinMaxScaler



def plotData(data_dict, Xplot,Yplot,Zplot='poi'): 
    print "size of dataset, post-Feature creation:",len(my_dataset)
    # plot some data, for inspection for outliers
    import matplotlib.pyplot
    for point in data_dict:
        X= data_dict[point][Xplot]
        Y = data_dict[point][Yplot] 
        ZTrue='b'
        if data_dict[point][Zplot]==True:
            ZTrue= 'r'
        matplotlib.pyplot.scatter( X, Y, color = ZTrue )
    matplotlib.pyplot.xlabel(Xplot)
    matplotlib.pyplot.ylabel(Yplot)
    matplotlib.pyplot.show()

######################## Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

def createNewFeature( data_dict, featuresList):
    for key in data_dict:
        # create a feature relating the salary to to total payments
        #if salary or total payments is 'NaN', then the ratio is zero
        if data_dict[key]['salary'] ==0 or data_dict[key]['total_payments'] ==0:
            data_dict[key]['salary-totalpayratio'] =0
        else:
            data_dict[key]['salary-totalpayratio']=float(data_dict[key]['salary'])/float(data_dict[key]['total_payments'])
            #print key,data_dict[key]['salary-totalpayratio'], data_dict[key]['poi']
        
        # create a feature relating the bonus to to total payments
        #if bonus or total payments is 'NaN', then the ratio is zero
        if data_dict[key]['bonus'] ==0 or data_dict[key]['total_payments'] ==0:
            data_dict[key]['bonus-totalpayratio'] =0
        else:
            data_dict[key]['bonus-totalpayratio']=float(data_dict[key]['salary'])/float(data_dict[key]['total_payments'])
        # create a feature relating total POI emails to total emails
        totalPOIEmails = float(data_dict[key]['from_poi_to_this_person']+data_dict[key]['from_this_person_to_poi']+data_dict[key]['shared_receipt_with_poi'])
        totalEmails = float(data_dict[key]['from_messages']+data_dict[key]['to_messages'])
        #if totalPOI or totalEmails is 'NaN', then the ratio is zero 
        if totalPOIEmails==0 or totalEmails==0:
            data_dict[key]['email-totalPOIratio'] =0
        else:
            data_dict[key]['email-totalPOIratio']=totalPOIEmails/float(totalEmails) 
    featuresList.append('salary-totalpayratio')
    featuresList.append('bonus-totalpayratio')
    featuresList.append('email-totalPOIratio')
    return data_dict, featuresList

######################## Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

# set up a PCA and a list of classifiers to try

def setUpCLF(quick = False):


    # the classifiers list is a list of list classifiers with a dict containging the params to use in the grid search
    classifiers = []

    
    classifiers.append([ # 28 sec
        linear_model.LogisticRegression(n_jobs =-1),
        dict(classifier__C= [ 1, 10, 100,1000,10**10, 10**20, 4000],classifier__class_weight =["balanced",None],classifier__tol=[.01, .00001, .000001,10**-10], classifier__random_state=[42,None])])

#classifiers.append([ #7 sec
#    GaussianNB(),
#    dict()])
       
    # for testing, it's nice to have a way to not run all the classifiers...
    if quick == True: return classifiers
    

    classifiers.append([ #12 sec
        DecisionTreeClassifier(class_weight ="balanced"),
        dict(classifier__max_depth=[None,1,2,4],classifier__criterion=['gini', 'entropy'], classifier__splitter =['best','random'],classifier__max_features =[ "auto","log2", 2,None,3])])

    classifiers.append([ #17 sec
         KMeans( n_jobs=-1, n_clusters=2, tol = 0.001),
         dict()])
         
    classifiers.append([ # 24sec
        ensemble.AdaBoostClassifier(),
        dict(classifier__n_estimators=[2,5,10,50,60,80,90], classifier__learning_rate = [.8,1.0,1.2,2.0])])
    classifiers.append([ #18 sec
        ensemble.AdaBoostClassifier(GaussianNB()),
        dict(classifier__n_estimators=[2,5,10,50,60,80,90], classifier__learning_rate = [.8,1.0,1.2,2.0])])
    classifiers.append([  # 40 sec
        LinearSVC(class_weight="balanced"),
        dict(classifier__C= [.5,1,2,4,40,400], classifier__max_iter=[800,1000,1200,1400,1600,10000], classifier__tol=[.0001,.01,.4,.8,1.,1.2,1.4,2.0])])    
    classifiers.append([ #2.3 min
        KNeighborsClassifier(n_jobs =-1),
        dict(classifier__weights =["uniform", "distance"], classifier__leaf_size =[3,15,30,50], classifier__n_neighbors=[2,5,7,10])])
    classifiers.append([ # 6 min w/classifier__n_estimators=[2,5,10,50,60,80,90]. running with smaller set due to not winning as best algo
        ensemble.RandomForestClassifier(n_jobs =-1,class_weight="balanced"),
        dict(classifier__n_estimators=[2,5,10,50,60],classifier__oob_score = [True,False],classifier__max_features= ["auto","sqrt","log2"], classifier__criterion=['gini', 'entropy'])])
    classifiers.append( # 120sec
        [ensemble.AdaBoostClassifier(DecisionTreeClassifier(max_depth=2)),
        dict(classifier__n_estimators=[2,5,10,50,60,80,90], classifier__learning_rate = [.8,1.0,1.2,2.0])])
    return classifiers

    
######################## Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

#why not run it all together!( uses a slightly modified test_classifier to get the stats back, rather than writing up our own.
# then we can store the stats to a list to look at later!
def runClassifiers(name,classifiers,features, labels, cur_dataset, featuresList, folds = 10):
    stats =[] # store the stats about each clf
    pcaType=['noPCA','PCA','randomPCA'] # labels for the different PCA types we will use
    scaled=["unscaled","scaled"]
    
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    
    ## run things scaled and non-scaled
    for s in scaled:
        if s =="scaled":
                # minmax is appropriate for this type of dataset--we have many features that don't have data for some cases, and need to preserve this association
                scaler= MinMaxScaler() 
                features = scaler.fit_transform(features)
 
        ## set up the test/train split--per suggestion, using Stratified Shuffle, due to smaller data set
        cv = StratifiedShuffleSplit(labels, folds, random_state = 42)
        for train_idx, test_idx in cv: 
            features_train = []
            features_test  = []
            labels_train   = []
            labels_test    = []
            for ii in train_idx:
                features_train.append( features[ii] )
                labels_train.append( labels[ii] )
            for jj in test_idx:
                features_test.append( features[jj] )
                labels_test.append( labels[jj] )
                    
            ## test and store the info for each classifier in a list: stats
            for c in classifiers:
                ## try the data as no PCA, PCA and randomized PCA
                for pType in pcaType:
                    t0 = time()
                    clf = Pipeline(steps=[('classifier', c[0] )])  # pipeline in use to save the bother of re-doing the gridsearch dict for both cases
                    if c[1].has_key('pca__n_components'): # depending on where we are, we may have inserted this in the list, and it will cause issues.
                        del c[1]['pca__n_components']
                    if pType=='PCA':  
                        pca = decomposition.PCA()
                        #add to the param grid for this classifier an element for PCA
                        c[1]['pca__n_components']=[None,'mle',int(math.sqrt(len(featuresList))),int(len(featuresList)/2.),int((2*len(featuresList))/3.),int((3*len(featuresList))/4.),len(featuresList)-1 ]
                        clf = Pipeline(steps=[('pca', pca), ('classifier', c[0] )]) # set up the clf as a pipeline so we can do PCA
                    if pType=='randomPCA':
                        pca = decomposition.RandomizedPCA()
                        #add to the param grid for this classifier an element for PCA--same as above, but without mle
                        c[1]['pca__n_components']=[None,int(math.sqrt(len(featuresList))),int(len(featuresList)/2.),int((2*len(featuresList))/3.),int((3*len(featuresList))/4.),len(featuresList)-1 ]
                        clf = Pipeline(steps=[('pca', pca), ('classifier', c[0] )]) # set up the clf as a pipeline so we can do randomized PCA
                    
                    #search the param_grid for best params based on the f1 score
                    grid_search = GridSearchCV(clf, param_grid= c[1], n_jobs= 1, scoring=make_scorer(f1_score)) 
                    grid_search.fit(features_train,labels_train)
                    #reach into the grid search and pull out the best parameters, and set those on the clf
                    params={}
                    for p in grid_search.best_params_:
                        params[p]=grid_search.best_params_[p]
                    clf.set_params(**params)
                    
                    # here we test each classifier and attach the results to a list to use later
                    # We fit the classifier using training set, and test on test set - this is cribbed from the test.py...mostly for speed
                    clf.fit(features_train, labels_train)
                    predictions = clf.predict(features_test)
                    for prediction, truth in zip(predictions, labels_test):
                        if prediction == 0 and truth == 0:
                            true_negatives += 1
                        elif prediction == 0 and truth == 1:
                            false_negatives += 1
                        elif prediction == 1 and truth == 0:
                            false_positives += 1
                        elif prediction == 1 and truth == 1:
                            true_positives += 1
                        else:
                            print "Warning: Found a predicted label not == 0 or 1."
                            print "All predictions should take value 0 or 1."
                            print "Evaluating performance for processed predictions:"
                            break
                try:
                    total_predictions = true_negatives + false_negatives + false_positives + true_positives
                    accuracy  = 1.0*(true_positives + true_negatives)/total_predictions
                    precision = 1.0*true_positives/(true_positives+false_positives)
                    recall    = 1.0*true_positives/(true_positives+false_negatives)
                    f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
                    f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)

                except:
                    print "Got a divide by zero when trying out:", clf
                    print "Precision or recall may be undefined due to a lack of true positive predicitons."    
                    precision = 0
                    recall = 0      
                    f1=0
                    f2=0
                # Originally, used a slightly modified test_classifier from the tester.py.moved here for speed
                #stats.append((name+","+s+","+p,)+test_classifier(clf, cur_dataset, featuresList, folds, outPrint=False)+(round(time()-t0, 3),))
                stats.append(([name,s,pType],)+(clf,accuracy, precision, recall, f1)+(round(time()-t0, 3),))

    return stats
   


def main():
    startTime0 = time()
    
######################## Task 1: Select what features you'll use.
    ### features_list is a list of strings, each of which is a feature name.
    ### The first feature must be "poi".
    features_list =['poi'] #build a full list from the data, but we need the first feature to be 'poi'
    # we build the full feature list later, after we take a look at the data and gather some info.

    ### Load the dictionary containing the dataset
    with open("final_project_dataset.pkl", "r") as data_file:
        data_dict = pickle.load(data_file)

    ######################## Rubric questions, re: Data Exploration:
    print "data set,# entries:",len(data_dict.keys())
    poi=0
    person=0
    featuresInData={} # all the features in the original set
    outlierLowData = []  #holds some possible entries without enough data to be useful
    featuresLowData = [] # these features may not be usefull due to being low in data
    for d in data_dict:
        #count the POI and non-POI
        if data_dict[d]['poi'] == True:
            poi+=1
        else:
            person+=1
        # count up the features, and count how many have have a missing value. Also count how many of each data points featues are NaN
        NaNInData=0
        for f in data_dict[d].keys():
            if featuresInData.has_key(f) !=True:
                    featuresInData[f] =0
            if data_dict[d][f] == 'NaN':            
                featuresInData[f] +=1
                NaNInData+=1
                data_dict[d][f] =0 #convert the NaN to a zero, for convenience
        if NaNInData > ((5./6)*len(featuresInData)): # most of the data is empty
            outlierLowData.append(d)
        #print "------test:",d, NaNInData
        
    print "data set, POI:",poi,"non-POI:",person
    print "data set, num original featues:", len(featuresInData)
    print "data set, features w/ greater than 2/3 values missing?"

    ### Use the previously generated feature dict to find some low data features
    for f in featuresInData.keys():
        if featuresInData[f] >(len(data_dict.keys())*(2./3)):
            featuresLowData.append(f)
            print "      ",f,featuresInData[f],"NaN"
            
    print "data set, low data outliers:"
    for o in outlierLowData:
        print "      ",o

    # setup a feature list with all known features included
    featuresListALL =[]
    featuresListALL.extend(features_list)
    removeFeatureList = ['poi','email_address']
    for f in featuresInData.keys():
        if f not in removeFeatureList:
            featuresListALL.append(f)
    print "constructed featuresListALL: \n   ","    num feature:", len(featuresListALL),"\n"
     

    # setup a featur list with 
    featuresListTrimmed = [] 
    featuresListTrimmed.extend(features_list)
    removeFeatureList = ['poi','email_address']
    removeFeatureList.extend(featuresLowData) # remove the low data features
    for f in featuresInData.keys():
        if f not in removeFeatureList:
            featuresListTrimmed.append(f)
    print "constructed featuresListTrimmed: \n   ","    num feature:", len(featuresListTrimmed),"\n"


######################## Task 2: Remove outliers
    # get rid of the non-data entry
    del data_dict['TOTAL']
    # other outliers may be the low-data entries above: - accuracy decreased with this in a few tests, so commented out...

    dataDictOutlierRemoved=data_dict.copy()
    for o in outlierLowData:
        del dataDictOutlierRemoved[o]

    print "\npost-Total removal,size of dataset:",len(data_dict)
    print "\npost-Outlier removal,size of dataset:",len(dataDictOutlierRemoved)

    
######################## Task 3: Create new feature(s)


    my_datasetPrenewfeatrs=data_dict # dataset without new features, outliers untrimmed
    my_datasetPrenewfeatrsTrmmd=dataDictOutlierRemoved ## dataset without new features, outliers trimmed

    featureListPrenewfeatrs=featuresListALL #featurelist without new feature, feature list untrimmed
    featureListPrenewfeatrsTrmmd=featuresListTrimmed #featurelist without new feature, feature list trimmed

    my_dataset, featuresListALL=createNewFeature( my_datasetPrenewfeatrs, featureListPrenewfeatrs)
    my_datasetTrmmd, featuresListTrmmd=createNewFeature( my_datasetPrenewfeatrsTrmmd, featureListPrenewfeatrsTrmmd)

    print "\npost featuresListTrimmed feature creation change:\n   ","    num feature:", len(featuresListTrimmed),"\n"

     

    ### Extract features and labels from dataset for local testing

    ##pre-new features, all data
    dataPrenewfeatrs = featureFormat(my_datasetPrenewfeatrs, featureListPrenewfeatrs, sort_keys = True)
    print "size of dataPrenewfeatrs, after featureFormat-dataPrenewfeatrs",len(dataPrenewfeatrs)
    labelsPrenewfeatrs, featuresPrenewfeatrs = targetFeatureSplit(dataPrenewfeatrs)
    print " size after targetFeatureSplit-featuresPrenewfeatrs",(len(featuresPrenewfeatrs)),"\n\n"

    # pre-new features, trimmed data
    dataPrenewfeatrsTrmmd = featureFormat(my_datasetPrenewfeatrsTrmmd, featureListPrenewfeatrsTrmmd, sort_keys = True)
    print "size of dataPrenewfeatrsTrmmd, after featureFormat-dataPrenewfeatrsTrmmd",len(dataPrenewfeatrsTrmmd)
    labelsPrenewfeatrsTrmmd, featurePrenewfeatrsTrmmd = targetFeatureSplit(dataPrenewfeatrsTrmmd)
    print " size after targetFeatureSplit-featureListPrenewfeatrsTrmmd",(len(featureListPrenewfeatrsTrmmd)),"\n\n"

    #after new features, untrimmed data
    data = featureFormat(my_dataset, featuresListALL, sort_keys = True)
    print "size of data, after featureFormat",len(data)
    labels, features = targetFeatureSplit(data)
    print " size after targetFeatureSplit",(len(features)),"\n\n"

    #after new features, trimmed data
    dataTrmmd = featureFormat(my_datasetTrmmd, featuresListTrmmd, sort_keys = True)
    print "size of dataTrmmd, after featureFormat",len(dataTrmmd)
    labelsTrmmd, featuresTrmmd = targetFeatureSplit(dataTrmmd)
    print " size after targetFeatureSplit",(len(featuresTrmmd)),"\n\n"


    scaler= MinMaxScaler()
    rescaled = scaler.fit_transform(features)

######################## Task 4: Try a varity of classifiers
    # set quick to True to test, false or clear for all classifiers
    classifiers =  setUpCLF(quick=False) 
      

######################## Task 5: Tune your classifier to achieve better than .3 precision and recall 

    ## For each data set that we have set up in dataPicker, run it against the classifiers, and add it to our stats
        ###run the classifiers with pipeline/gridcv, and pick the best score for each. run against several data/feature variations, for excitement

    stats=[]
    dataPicker={"newfeatures, Trmmd":(my_datasetTrmmd,featuresListTrmmd,featuresTrmmd,labelsTrmmd),
                "newfeatures, Untrmmd":(my_dataset,featureListPrenewfeatrs,features,labels),
                "Prenewfeatures, Trmmd":(my_datasetPrenewfeatrsTrmmd,featureListPrenewfeatrsTrmmd,featurePrenewfeatrsTrmmd,labelsPrenewfeatrsTrmmd),
                "Prenewfeatures, Untrmmd":(my_datasetPrenewfeatrs,featuresListALL,featuresPrenewfeatrs, labelsPrenewfeatrs)}
                
    for key in dataPicker:
            stats.extend( runClassifiers(key,classifiers, dataPicker[key][2],dataPicker[key][3],dataPicker[key][0],dataPicker[key][1],folds = 7))
  
######################## Task 6: Dump your classifier, dataset, and features_list so anyone can
    ### check your results. You do not need to change anything below, but make sure
    ### that the version of poi_id.py that you submit can be run on its own and
    ### generates the necessary .pkl files for validating your results.
    
    ### Take the returned optimized CLF's, and sort out who had the highest score and display it.
    print "\n--------Final Scores:\n"
    highF1=(0,0,0,0,0,0)
    avgAcc=0
    avgPre=0
    avgRec=0
    avgF1=0
    totTime=0
    for s in stats:
        avgAcc+=s[2]
        avgPre+=s[3]
        avgRec+=s[4]
        avgF1+=s[5]
        totTime+=s[6]
        print "    ",s[0],":",s[1].named_steps,  "\n Accuracy:",s[2], " Precision:",s[3], " Recall:", s[4], " F1:",s[5],"testing time:",s[6],"s","\n\n"
        #if s[3]>=.3 and s[4] >=.3 and
        if highF1[5]<s[5]:
            highF1=s
       
    #print "results--", "accuracy:",accuracy, " precision:",precision, " recall:", recall, " f1:",f1
    print "\n--------Highest Scores:"
    print "    ",highF1[0],":",highF1[1].named_steps,  "\n Accuracy:",highF1[2], " Precision:",highF1[3], " Recall:", highF1[4], " F1:",highF1[5],"testing time:",s[6],"s","\n\n"

    totalTests= len(stats)
    print "--------Summary:\n    avgAcc:",avgAcc/totalTests,"avgPre",avgPre/totalTests,"avgRec",avgRec/totalTests,"avgF1",avgF1/totalTests,"\n    avgTime:",totTime/totalTests,"totTime:",totTime,"totalTests:",totalTests

    timeMin=round((time()-startTime0)/60, 3)
    print "\nRun Time:", timeMin,"m\\nn"
   
    my_dataset=dataPicker[highF1[0][0]][0]
    features_list=dataPicker[highF1[0][0]][1] #for now
    clf= highF1[1]
    #run data against a possible best, for sanity check.
    sanityCLF= Pipeline(steps=[(
        'pca', decomposition.PCA(copy=True, n_components=18, whiten=False)),
        ('logistic', linear_model.LogisticRegression(C=100000000000000000000L, class_weight='balanced', dual=False, fit_intercept=True, intercept_scaling=1, penalty='l2', random_state=42, tol=1e-10))])
    print  "----Reality check:"
    test_classifier(sanityCLF, my_dataset, features_list, folds=1000, outPrint=True)
    print "----Our winner:"
    test_classifier(clf, my_dataset, features_list, folds=1000, outPrint=True)

    dump_classifier_and_data(clf, my_dataset, features_list)


if __name__ == '__main__':
    main()