#!/usr/bin/python
# by:Luke Lathrop started:9-24-2012
# when two files are given as input, output a list of key fields in file a that have a matching file a value as a key in file b, and output key a with value b
import string
import sys
import math

# matrix math

C = [0,4,-6,1]

N= [[1,0,0,0],
    [0,1,0,0],
    [0,0,-1.2,-2.2],
    [0,0,-1,0]]

for  i in range(0,len(N)):
    row=0
    for x in range(0,len(N[i])):
       #print "N row ", N[i][x], "C col: ", C[x]
       row = row+N[i][x]*C[x]
    print row
    
print "\nmatrix math done..... "


count = set()
for i in range(0, 255):
    step1=i/255.0
    step2=step1**(1.0/2.2)
    step3=step2*255.0
    count.add(round(step3, 0))
    
print len(count)