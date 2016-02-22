#!/bin/python
#from mystatslib import *

#LinearRegression
#y=w_1*x+w_0

#Quadratic Loss
#w_0=1/M*sum (y_i )-w_1/M * sum(x_i)
#
#w_1=(M*sum(x_i*y_i)-sum(x_i)*sum(y_i))/M(sum(x_i^2)-(sum(x_i)^2))



M=5.
X_Y=((0.,3.),(1.,6.),(2.,7.),(3.,8.),(4.,11.))

sumx_iy_i=0
for pair in X_Y:
 sumx_iy_i = pair[0]*pair[1] +sumx_iy_i
print "sum(x_i*y_i)", sumx_iy_i
 
sumx_i=0
for pair in X_Y:
 sumx_i = pair[0] +sumx_i
print "sum(x_i", sumx_i
 
sumy_i=0
for pair in X_Y:
 sumy_i = pair[1] +sumy_i
print "sum(y_i)", sumy_i
 
sumx_isquared=0
for pair in X_Y:
 sumx_isquared = pair[0]**2 + sumx_isquared
print "sum(x_i^2)", sumx_isquared

sumsquaredX=0
for pair in X_Y:
 sumsquaredX = pair[0] +sumsquaredX
sumsquaredX=sumsquaredX**2
print "sum(x_i)^2", sumsquaredX

w_1= (M*sumx_iy_i-sumx_i*sumy_i)/(M*sumx_isquared-sumsquaredX)
w_0=((1./M)*sumy_i)-((w_1/M)*sumx_i)

print "w1 - ",w_1
print "  w0 - ",w_0

