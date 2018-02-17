#abilities:hearing, seeing, comprehending,walking,talking
#hears :medium ,frequency,speeds
import numpy.random as rand
import numpy as np
from support import death
from Logger import Logger
class species():
    def __init__(self, position, maxenergy, speed):
        self.position=position
        self.maxenergy=maxenergy
        self.speed=speed
        self.walkSpeed=0.01
        self.age=1
        self.energy=10

class species1(species):
    def __init__(self,*args):
        super(species1,self).__init__(*args)
        self.lastReproduction=0

    def walk(self):
        self.age += 1
        self.walkSpeed=5*((1/(self.age)))
        x=self.position[0]+rand.uniform(0,self.walkSpeed)
        y=self.position[1]+rand.uniform(0,self.walkSpeed)
        if x>5:x-=5
        if y > 5: y -= 5
        self.position=(x,y)
        self.energy-=self.speed*np.log(self.age)

        #print(self.energy)
        if self.energy<=0 :
            return death(self)
        else: return 1
    def eat(self,tree):
        required=self.maxenergy-self.energy
        if required<(tree.energy-1):
            self.energy=self.maxenergy
            tree.energy=tree.energy-required
        else :
            #print("stomach not ful")
            maxTreeEnergy=tree.energy-1
            self.energy+=maxTreeEnergy
            tree.energy-=maxTreeEnergy
        r=0
    def reproduce(self, other):
        if self.age-self.lastReproduction>2:
            #Logger.info("A child has taken birth")
            self.lastReproduction = self.age
            child= species1(((self.position[0] + other.position[0])/2,(self.position[1] + other.position[1])/2) , (self.maxenergy +other.maxenergy) / 2,
                        (self.speed + other.speed) / 2)
            childEnergy=(self.energy+other.energy)/2
            child.energy=childEnergy
            self.energy-=childEnergy/2
            other.energy-=childEnergy/2
            return child
        else :
            return None
class tree(species):
    def __init__(self,*args):
        super(tree,self).__init__(*args)

    def production(self):
        self.energy=min(self.energy+self.speed,self.maxenergy)



