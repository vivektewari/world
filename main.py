from species import species1,tree
import numpy.random as rand
import numpy as np
from Logger import Logger

class world():

    def distance(pos1,pos2):
        #print((pos1[0]-pos2[0])**2)
        return (np.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2))

    def __init__(self,numwalkable=10,numTree=70,years=20000):
        self.walker=[]
        self.trees=[]
        self.years=years
        self.currentYear=0

        while len(self.walker)<numwalkable:
            positionR=tuple(rand.uniform(0,5,2))
            maxenergyR = float(rand.uniform(5, 20, 1))
            speedR = float(rand.uniform(0, 0.1, 1))
            self.walker.append(species1( positionR, maxenergyR, speedR))
        while len(self.trees) < numTree:
            positionR=tuple(rand.uniform(0,5,2))
            maxenergyR = float(rand.uniform(5, 10, 1))
            speedR = float(rand.uniform(0, 0.1, 1))
            self.trees.append(tree(positionR, maxenergyR, speedR))
    def live(self):
        Logger.info("world is starting")
        for j in range(0,self.years):
            #if j%(self.years/10) !=0 :print(len(self.walker))
            i=len(self.walker)
            while i>0:
                i-=1
                live=self.walker[i].walk()
                if not live:
                    self.walker.pop(i)
                    break
                if self.walker[i].energy<2:
                    for l in range(0,len(self.trees)):
                        if world.distance(self.walker[i].position,self.trees[l].position)<0.5:
                            self.walker[i].eat(self.trees[l])
                            break

                else :
                    for k in range(0,len(self.walker)):
                        if k != i :
                            if world.distance(self.walker[i].position,self.walker[k].position)<0.2 and self.walker[k].energy>1:
                                child=self.walker[i].reproduce(self.walker[k])
                                if child is not None:
                                    self.walker.append(child)
                                #print(j)
                                break
            for i in range(0,len(self.trees)):self.trees[i].production()
            #print(len(self.walker))
            self.currentYear+=1
            if self.currentYear%1000==0:
                Logger.info("years passes,population=" +str((j,len(self.walker))))




firstWorld=world()
firstWorld.live()










