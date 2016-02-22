
#from __future__ import division
from math import *
import random
import itertools
#from plotting import *

def prob(amount,total):
    return float(amount)/total

def mean(data):
    return float(sum(data))/len(data)

def median(data):
    sorteddata=sorted(data)
    return sorteddata[len(sorteddata)/2]

def lowquartile(data):
    sorteddata=sorted(data)
    return sorteddata[len(sorteddata)/4]

def upquartile(data):
    sorteddata=sorted(data)
    return sorteddata[3*len(sorteddata)/4]
def quartile(lengthdata): #return #elements left after quartile
    return ((lengthdata-3)/2)+3

def trimmedmean(data): #broken
    sorteddata=sorted(data)
    trimdata=sorteddata[(len(sorteddata)/4):(3*len(sorteddata)/4)+1]
    print trimdata
    return mean(trimdata)

def mode(data):
    #stuff
    count = 0
    for i in data:
        if data.count(i) >=data.count(count):
            count = i
    return count

def variance(data):
    m=mean(data)
    return sum([(i-m)**2 for i in data])/(len(data))

def stddev(data):
    return sqrt(variance(data))

def stanscore(data,pointx):
    return (pointx-mean(data))/stddev(data)

def scale(m,sd,v,pointx,ss,scaler):
    mean = m*scaler
    standev= sd*scaler
    var= (v*scaler)**2
    pointy= pointx*scaler
    stscore=(pointy-mean)/standev
    return mean,standev,var,pointy,stscore

#print incmean(currentmean,currentcount,newitem)
def incmean(oldmean,n,x):
    #Insert your code here
    return ((oldmean*n)+x)/(n+1)

def numoutcomes(n,k):
#n!/(n-k)!k!
# n= flips k= expectednumofheads return # of matching outcomes
    f=0
    h=1
    coins = range(n)
    for i in itertools.permutations(coins,k):
        f+=1
    for i in range(k):
        h=h*(i+1)
    return float(f/h)

def sizeoftruthtable(flips,answers):
     return answers**flips


def probxheads(flips, numheads, probheads):
    numtails=flips-numheads
    probtails=1-probheads
    return  numoutcomes(flips,numheads)*(probheads**numheads)*(probtails**numtails)

def flip(N):
    data= [1.0 if random.random() > .5 else 0.0 for i in range(N)]
    return data

def confidence(n,p,a): #n=sample size
    ci = a*sqrt(variancexforp(p)/n)
    return ci

def margerr(m,p,a):
    return (p*(1-p))*((a**2)/(m**2))

def variancexforp(p):
    return p*(1-p)

def factor(l): #should be the whole t-table
    return 1.96

def conf(l):
    return factor(l)*(sqrt(var(l)/len(l)))

def onesidedtest(n,p,ci):
    critregion= [probxheads(n, i, p) for i in range(11)]
    c=0
    for i in critregion:
        c=c+i
        if c>=ci:
            break
        ti=i

    return critregion.index(ti)

def linregressionb(c):
    mx=mean([x for x,y in c])
    my=mean([y for x,y in c])
    regtop=[((x-mx)*(y-my))for x,y in c]
    regbottom= [(x-mx)**2 for x,y in c]

    return (sum(regtop))/(sum(regbottom))

def linregressiona(c):
    mx=mean([x for x,y in c])
    my=mean([y for x,y in c])
    return my-(linregressionb(c)*mx)


def correlationr(c):
    mx=mean([x for x,y in c])
    my=mean([y for x,y in c])
    sumxy=sum([((x-mx)*(y-my))for x,y in c])
    sumxsq= sum([(x-mx)**2 for x,y in c])
    sumysq= sum([(y-my)**2 for x,y in c])

    return (sumxy)/sqrt(sumxsq*sumysq)

    
#ML - Maximum Likelyhood
# p(X) = count(x)/N

# LaPlace Smoothing
# LS(k) p(X) = count(x)+k /(N+k/x/)
def laPlace(K,matches,total,numClasses):
    K=K+.0
#messages - matches=number of matches of target, total=all in dictionary
    matches=matches+.0
    total=total+.0
# numClasses - message types:(spam,notspam) /x/=2, etc
    numClasses=numClasses+.0
    p= (matches+K)/(total+K*numClasses)
    return p

# Bayes - simple form
#  P(A|B)=P(B|A)*P(A) / P(B)
def bayesSimple(pBgivA,pA,pB):
    pAgivB=(pBgivA*pA)/pB
    return pAgivB

#Bayes - Alternate
# P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
def bayesAlt(pBgivA,pA,pnotA,pBgivnotA):
    pAgivB=(pBgivA*pA)/(pBgivA*pA+pBgivnotA*pnotA)
    return pAgivB

#Transition Prob:
# p(A1) = p(A1|A0)*p(A0)+p(A1|B0)*p(B0)
def TransitionProbab(pA1givA0,pA0,pA1givB0,pB0):
    pA1= pA1givA0*pA0+pA1givB0*pB0
    return pA1
    
# gaussian :  f(x|mu,sigma**2) = (1/sqrt(2*pi*sigma**2))*exp((-1*(x-mu)**2)/(2*sigma**2))
def gaussian(sigma,mu,x):
    return (1./sqrt(2.*pi*sigma))* exp(((-1./2)*((x-mu)**2.))/(sigma))
    
#Kalman Filter:- Measurement update step
def kalmanUpdate(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]
#Kalman Filter:- movement update step
def kalmanPredict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]
# 1 Dimension Kalman Filter
def Kalman(measurements,motion,measurement_sig,motion_sig,mu,sig):
    for i in range(len(motion)):
        mu,sig=kalmanUpdate(mu,sig,measurements[i],measurement_sig)
        print 'update: ', mu,sig
        mu,sig=kalmanPredict(mu,sig,motion[i],motion_sig)
        print 'predict: ', mu,sig
    return[mu,sig]
    
    


#data is a list like [1,2,3,4]
##print mean(data)
#print median(data)
#print lowquartile(data)
#print upquartile(data)
#print trimmedmean(data)
#print mode(data)
#print variance(data)
#print standev(data)
#print stanscore(data,5)
#print "scale: mean,standev,var,pointy,stscore"
#print scale(mean(data),standev(data),variance(data),5,stanscore,1.5)
#print numoutcomes(flips,numheads)
#print sizeoftruthtable(flips,answers)
#print numoutcomes(flips,numheads)/sizeoftruthtable(flips,answers)
#print probxheads(flips, numheads, probheads)

