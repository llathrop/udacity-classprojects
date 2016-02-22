#!/bin/python
from mystatslib import *
from math import *
import random
import itertools

# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    moves = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 99
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            moves[x2][y2] = i
   
    path = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    path[goal[0]][goal[1]]='*' 
    node= goal
    found = False  # flag that is set when search is complete
    pathcost = 0
    while not found:
        x=node[0]
        y=node[1]
        if x == init[0] and y == init[1]:
            found =True
            path[x][y] = "S"
            return pathcost
        lastx=x-delta[moves[x][y]][0]
        lasty=y-delta[moves[x][y]][1]
        node=[lastx,lasty]
        path[lastx][lasty]=delta_name[moves[x][y]]
        pathcost+=1

    return pathcost
    

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    value = [["99" for row in range(len(grid[0]))] for col in range(len(grid))]
    #print "goal:",goal
     
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            node=[row,col]
            if grid[row][col] !=1:
                value[row][col] = search(grid,[row,col],goal,cost)
    
    return value 

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
for i in compute_value(grid,goal,cost):
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
for i in compute_value(grid,goal,cost):
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
for i in  compute_value(grid,goal,cost):
            print " ",i     
      
     
#EOF