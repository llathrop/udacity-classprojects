#!/bin/python
from mystatslib import *
from math import *
import random
import itertools


# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 


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
#1 Dimension Kalman Filter
def Kalman(measurements,motion,measurement_sig,motion_sig,mu,sig):
    for i in range(len(motion)):
        mu,sig=kalmanUpdate(mu,sig,measurements[i],measurement_sig)
        print 'update: ', mu,sig
        mu,sig=kalmanPredict(mu,sig,motion[i],motion_sig)
        print 'predict: ', mu,sig
    return[mu,sig]
     
   


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 10.
sig = 1000.
   
    
print Kalman(measurements,motion,measurement_sig,motion_sig,mu,sig)
