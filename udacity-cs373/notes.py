#!/bin/python
from mystatslib import *
import math
 
#LinearRegression: y=w_1*x+w_0
 
#Quadratic Loss
#w_0=1/M*sum (y_i )-w_1/M * sum(x_i)
#w_1=(M*sum(x_i*y_i)-sum(x_i)*sum(y_i))/M(sum(x_i^2)-(sum(x_i)^2))
 
#Gaussian
# f(x|mu,sigma**2) = (1/sqrt(2*pi*sigma**2))*exp((-1*(x-mu)**2)/(2*sigma**2))
# mu=mean, sigma**2 = variance
#gaussian = (1/math.sqrt(2*math.pi*variance(data)))* math.exp((-1*(x-mean(data))**2)/(2*variance(data)))
 
#Value Backup Policy: V(s) <- maxA gamma * sumSprime(P(Sprime|s,a) V(Sprime)) + R(s)
 
#TD Learning
#?
#Q Learning: Q(s,a)) <--Q(s,a)+alpha*(R(s)+gamma*Q(Sprime,Aprime)-Q(s,a))
 
#ML - Maximum Likelyhood: p(X) = count(x)/N
 
# LaPlace Smoothing
# LS(k) p(X) = count(x)+k /(N+k/x/)
#count=number of matches, total=all in dictionary(N), message types:(spam,notspam) /x/=2, etc
 
# Bayes - simple form: P(A|B)=P(B|A)*P(A) / P(B)
# Bayes - Alternate:   P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
 
#Transition Prob: p(A1) = p(A1|A0)*p(A0)+p(A1|B0)*p(B0)
 
#Value Iteration: V(s)= maxA of gamma*sum(P(sPrime|s,a)*V(sPrime))+R(s)
 
# Stationay distribution: aP+b(1-p)=p
 
##Scheduling
#ES(s)=0
#ES(B)=maxAleadingtoB(ES(A)+Duration(A)
#LS(Finish)=ES(Finish)
#LS(A)=minBbeforeA(LS(B)-Duration(A)

#Perspective projection
# x=X*(f/z) , f=x*z/X , X=x*z/f , z= X*f/x  <--range
# focus = 1/f=1/Z+1/z
#X=height of object, x=sensor size, z=distance, f=focal plane

#Linear Filter: I(x,y)= sumfrmutov(I(x-u, y-v)*g(u,v)

#Diffraction: Z=(f*B)/(x2-x1)
#deltaX/f=B/Z

#Localization: theta = heading , omega = turning velocity, deltaT = change in time.
# "xPrime=",x+v*deltaT*cos(theta)
# "yPrime=",y+v*deltaT*sin(theta) 
# "thetaP=", theta+omega*deltaT






#EOF
