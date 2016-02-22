#!/bin/python
from mystatslib import *
from math import *
import random
import itertools

     # ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                
    for i in value:
            print " ",i
    policy = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    for col in range(len(grid[0])):
        for row in range(len(grid)):
           # print row,col
            candidate = 99
            if value[row][col] !=99:
                candidate=value[row][col]
                for i in range(len(delta_name)):
                    xCur=row+delta[i][0]
                    yCur=col+delta[i][1]
                    #print "i:",i,"row:",xCur,"col:",yCur, "candidate:",candidate
                    if   0 <= xCur < len(grid) and 0 <= yCur < len(grid[0]):
                        if value[xCur][yCur] <candidate:                          
                            candidate=i
                           # print "candidate update:",candidate
                            
                policy[row][col]= delta_name[candidate]
            else:
                policy[row][col]= " "
            #for i in policy:
             #   print " ",i  
    policy[goal[0]][goal[1]] = "*"
    return policy 


     
     
print "FIRST GO:"
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]

for i in grid:
            print " ",i 
            
print "Values:"#,compute_value(grid,goal,cost)
for i in optimum_policy(grid,goal,cost):
            print " ",i
            
print "\n\nNEXT TRY"       
grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]            
goal = [len(grid)-1, len(grid[0])-1]

for i in grid:
            print " ",i 
            
print "Values:"#,compute_value(grid,goal,cost)
for i in optimum_policy(grid,goal,cost):
            print " ",i     
      
        
print "\n\nNEXT TRY"       
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
      
           
goal = [len(grid)-1, len(grid[0])-1]

for i in grid:
            print " ",i 
            
print "Values:"#,compute_value(grid,goal,cost)
for i in optimum_policy(grid,goal,cost):
            print " ",i   
            
print "\n\nNEXT TRY"  
 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

for i in grid:
            print " ",i 
            
print "Values:"#,compute_value(grid,goal,cost)
for i in optimum_policy(grid,goal,cost):
            print " ",i     

print "\n\nNEXT TRY"  
 
grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner

init = [4, 3] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                


for i in grid:
            print " ",i 
            
print "Values:"#,compute_value(grid,goal,cost)
for i in optimum_policy(grid,goal,cost):
            print " ",i     
 
 
 
#EOF