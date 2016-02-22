from mystatslib import *
 # percent: % of tot = amount or 25% of 100 == 25 or amount/tot = %
 #per = a/tot
 #histplot(Weight)
 #scatterplot(Height,Weight)
 #barchart(Height,Weight)


from random import randint

N = 1000

def simulate(N):
    K = 0
    ###insert your code here###
    for i in range(N):
        door = randint(1,3)
        mychoice= randint(1,3)
        #monty
        doorsleft=[1,2,3]
        if mychoice == door:
            doorsleft.remove(mychoice)
            monty=doorsleft[randint(0,len(doorsleft)-1)]
        else:
            doorsleft.remove(mychoice)
            doorsleft.remove(door)
            monty=doorsleft[0]

        #flip choice
        doorsleft=[1,2,3]
        doorsleft.remove(mychoice)
        doorsleft.remove(monty)
        newchoice=doorsleft[0]
        print door, mychoice, monty, newchoice, doorsleft
        if newchoice ==door:
            K+=1
            print K, i

    return float(K) / float(N)

print simulate(N)