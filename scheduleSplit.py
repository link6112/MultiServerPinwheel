from pickletools import read_unicodestringnl
import scheduleGenerator
import density
from fractions import Fraction
import itertools

#The goal of this code is to create 2 sets of tasks with
#density less than 5/6

class ScheduleSplit:
    def __init__(self):
        return

    def densityCheck(self, tasks):
        densityCheck, densityValue = density.densityCalcWFraction(tasks)
        if densityCheck == "Schedulable":
            #print("Density 5/6 or below\nDensity = " + str(densityValue))
            return
        elif densityCheck == "Splittable":
            #print("Density above 5/6 but below or equal to 10/6, time to split it.\nDensity = " + str(densityValue))
            self.split(tasks)
            return
        else:
            #print("Density is too high, add a third pinwheel.")
            return
        
    def split(self, tasks):
        serverA = []
        serverB = []
        individualDensities = {}
        
        for i in tasks:
            density = 1/i
            individualDensities[i] = density
        target = 0.833333333333


        result = [seq for i in range(0, len(individualDensities.values())) for seq in itertools.combinations(individualDensities.values(), i) if sum(seq) <= target]
        print(individualDensities)
        print(result)

        #Above code WORKS but I now must cut it down so that it only include sequences where all values are accounted for

        #for i in tasks[::2]:
        #    serverA.append(i)
        #for k in tasks[1::2]:
        #    serverB.append(k)
        #dumb split, obviously doesn't work.

        
        #return task1, task2


tasks = [2,3]

Task1 = ScheduleSplit()
#Task1.densityCheck([2,3])

Task1.densityCheck([1,1,1])
Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18])


Task1.densityCheck([2,12,14,16,18])
Task1.densityCheck([5,6,8,10])
# by friday - Finish density, check schedule split
# by friday - Generate schedule with density above 5/6
# by friday - check scheudle split on those
# saturday - check back here
#######