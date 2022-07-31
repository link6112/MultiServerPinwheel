from pickletools import read_unicodestringnl
import scheduleGenerator
import density

#The goal of this code is to create 2 sets of tasks with
#density less than 5/6

class ScheduleSplit:
    def __init__(self):
        return

    def densityCheck(self, tasks):
        densityCheck, densityValue = density.densityCalcWFraction(tasks)
        if densityCheck == True:
            print("Density 5/6 or below\nDensity = " + str(densityValue))
        elif densityCheck == False:
            print("Density above 5/6, time to split it.\nDensity = " + str(densityValue))
        
    #def split(self, tasks):
        
        
        #return task1, task2


tasks = [2,3]

Task1 = ScheduleSplit()
Task1.densityCheck([2,3])
Task1.densityCheck([2, 5, 6])
# 1 - Finish density, check schedule split
# 2 - Generate schedule with density above 5/6
# 3 - check scheudle split on those
# 4 - check back here
#######