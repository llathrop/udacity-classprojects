#!/cygdrive/c/Anaconda2/python
# Scratchpad for class...

import sys
from math import *
import random
import itertools
from time import time
import copy
import numpy as np
import pylab as pl
#from matplotlib import pyplot as plt
#import matplotlib
#import nltk
#from nltk.corpus import stopwords
#from nltk.stem.snowball import SnowballStemmer
from mystatslib import *

#import class_vis
#from class_vis import prettyPicture
#from prep_terrain_data import makeTerrainData


#ten% training (for speed)
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

# Time an operation:
#t0 = time()
#clf.fit(features_train, labels_train)
#print "training time:", round(time()-t0, 3), "s"

################################################################

#for i in range(len(features_test)):
#    label= 'bo'
#    if pred[i] ==0:
#        label= 'ro'
#plt.plot(features_test[i][0],features_test[i][1], label)

#plt.show()

#prettyPicture(clf, features_test, pred)

#################################################################


sw = stopwords.words("english")
#print sw
print "Stopwords:",len(sw)

stemmer= SnowballStemmer("english")
print "stem of unresponsive:", stemmer.stem ('unresponsive')


  
#EOF