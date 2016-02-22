#!/bin/python
from mystatslib import *
 # percent: % of tot = amount or 25% of 100 == 25 or amount/tot = %
 #per = a/tot
 #histplot(Weight)
 #scatterplot(Height,Weight)
 #barchart(Height,Weight)

#print numoutcomes(4,3)

#print probxheads(4, 3, .5)

#Bayes - Variables
pA=3/8.0
pBgivA=2.0/9
pBgivnotA=2/15.0
pB=1-pA
# Bayes - simple form
#  P(A|B)=P(B|A)*P(A) / P(B)
#
pAgivB=(pBgivA*pA)/pB
print "simple -",pAgivB
#
#Bayes - Alternate
# P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
#
pAgivB=(pBgivA*pA)/(pBgivA*pA+pBgivnotA*pB)
print "Alt -",pAgivB
########





