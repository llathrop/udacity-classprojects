#!/usr/bin/python
from math import *

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
     
    cleaned_data = []

    ### your code goes here

    for i in range(len(ages)):
        cleaned_data.append( (ages[i][0],net_worths[i][0],abs(net_worths[i][0]-predictions[i][0])))
        
    cleaned_data.sort(key=lambda tup: tup[2])  
    
    for i in range(int(len(cleaned_data)*.1)):
        cleaned_data.pop()
    
    #for i in cleaned_data:
     #   print i
    #print len(cleaned_data)
    return cleaned_data

