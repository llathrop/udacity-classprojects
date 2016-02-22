#!/bin/python
from mystatslib import *
import math
 
#LinearRegression
#y=w_1*x+w_0

#Quadratic Loss
#w_0=1/M*sum (y_i )-w_1/M * sum(x_i)
#w_1=(M*sum(x_i*y_i)-sum(x_i)*sum(y_i))/M(sum(x_i^2)-(sum(x_i)^2))

#Gaussian
# f(x|mu,sigma**2) = (1/sqrt(2*pi*sigma**2))*exp((-1*(x-mu)**2)/(2*sigma**2))
# mu=mean, sigma**2 = variance
#gaussian = (1/math.sqrt(2*math.pi*variance(data)))* math.exp((-1*(x-mean(data))**2)/(2*variance(data)))

#Value Backup Policy- 
# V(s) <- maxA gamma * sumSprime(P(Sprime|s,a) V(Sprime)) + R(s)

#TD Learning
#?
#Q Learning
#Q(s,a)) <--Q(s,a)+alpha*(R(s)+gamma*Q(Sprime,Aprime)-Q(s,a))
#ML - Maximum Likelyhood
# p(X) = count(x)/N

# LaPlace Smoothing
# LS(k) p(X) = count(x)+k /(N+k/x/)
#count=number of matches, total=all in dictionary
#message types:(spam,notspam) /x/=2, etc

# Bayes - simple form
#  P(A|B)=P(B|A)*P(A) / P(B)
#Bayes - Alternate
# P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
#
#Transition Prob:
# p(A1) = p(A1|A0)*p(A0)+p(A1|B0)*p(B0)
#
#Value Iteration
# V(s)= maxA of gamma*sum(P(sPrime|s,a)*V(sPrime))+R(s)

pR0=1.
pS0=1-pR0
pRgivR = .6
pSgivR = 1-pRgivR
pSgivS =.8
PRgivS = 1-pSgivS
PHgivR = .4
PGgivR = 1- PHgivR
PHgivS = .9
PGgivS = 1- PHgivS

pR1 = TransitionProbab(pRgivR,pR0,PRgivS,pS0)
print "p(R1) = " , pR1

print "P(R|H): ", bayesAlt(PHgivR,pR1,PHgivS,1-pR1)



#EOF