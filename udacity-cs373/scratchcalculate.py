#!/bin/python
#from matplotlib import pyplot as plt
#import numpy as np

from mystatslib import *
from math import *
import random
import itertools

#P(rainTomorrow|rainToday)=60%
#P(rainTomorrow|!rainToday)=25%
#P(rainFriday)=75%

#P(rainSaturday)=?
#P(rainSunday)=?
#p(rainWeekend)=P(rainSaturday)*P(rainSunday)

pBgivA=.6
pBgivnotA=.25
pA=.75
pnotA=1-pA

print "Given:"
print "P(rainTomorrow|rainToday)= %",pBgivA*100
print "P(rainTomorrow|!rainToday)= %",pBgivnotA*100
print "P(rainFriday)= %",pA*100

#Bayes - Alternate
# P(A|B)=P(B|A)*P(A) / P(B|A)*P(A)+P(B|!A)*P(!A)
pRainSaturday=pBgivnotA*pA

pA=pRainSaturday

pRainSunday=pBgivnotA*pA

pNoRainWeekend=(pRainSaturday)+(pRainSunday)

print"\n"
print "Results:"
print "P(no RainSaturday)= %",(1-pRainSaturday)*100
print "P(no RainSunday)= %",(1-pRainSunday)*100
print "P(NoRainWeekend)= %",pNoRainWeekend*100

