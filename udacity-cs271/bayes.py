#!/bin/python
from mystatslib import *

#ML - Maximum Likelyhood
# p(X) = count(x)/N


# LaPlace Smoothing
# LS(k) p(X) = count(x)+k /(N+k/x/)
def laPlace(K,count,total,numClasses):
    K=K+.0
#messages - count=number of matches, total=all in dictionary
    count=count+.0
    total=total+.0
# numClasses - message types:(spam,notspam) /x/=2, etc
    numClasses=numClasses+.0
    p= (count+K)/(total+K*numClasses)
    return p



# Bayes - simple form
#  P(A|B)=P(B|A)*P(A) / P(B)
#
def bayesSimple(pBgivA,pA,pB):
    pAgivB=(pBgivA*pA)/pB
    return pAgivB
#
#Bayes - Alternate
# P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
#
def bayesAlt(pBgivA,pA,pB,pBgivnotA):
    pAgivB=(pBgivA*pA)/(pBgivA*pA+pBgivnotA*pB)
    return pAgivB


K=1
totMessage=6
target=3
messageType=2

#Bayes - Variables
pA=laPlace(K,target,totMessage,messageType)
pB=1-pA
pBgivA=laPlace(K,2,8,11.)*laPlace(K,0,8,11.)
pBgivnotA=laPlace(K,1,8,11.)*laPlace(K,1,8,11.)


print "pA - ",pA
print "pB - ",pB
print "pBgivA - ",pBgivA
print "pBgivnotA - ",pBgivnotA

#print "bayes - Simple - ", bayesSimple(pBgivA,pA,pB)
print "Bayes - Alt    - ",bayesAlt(pBgivA,pA,pB,pBgivnotA)


print "3/19. ", 3/19.
print "2/19. ", 2/19.
print "1/19. ", 1/19.