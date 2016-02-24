#!/bin/python
#from matplotlib import pyplot as plt
#import numpy as np

def twiddle(p= [0,0,0], dp=[1,1,1], tol = 0.2): #Make this tolerance bigger if you are timing out!
############## ADD CODE BELOW ####################
    p= [0,0,0]
    dp=[1,1,1]
    best_err= run(p)
    n=0
    while sum(dp) >tol:
        for i in range(len(p)):
            p[i]+=dp[i]
            err = run(p)
            
            if err < best_err:
                best_err = err
                dp[i]*=1.1
            else:
                p[i]-=2.*dp[i]
                err=run(p)
                
                if err< best_err:
                    best_err=err
                    dp[i] *= 1.1
                else:
                    p[i] +=dp[i]
                    dp[i]*=0.9
        n+=1
        print 'Twiddle #',n, p,'-->',best_err 
                
    return p

