from pickletools import read_unicodestringnl
import scheduleGenerator
import density
from fractions import Fraction
import itertools
test="printstatementcheck"
#The goal of this code is to create 2 sets of tasks with
#density less than 5/6

class ScheduleSplit:
    def __init__(self):
        return

    def densityCheck(self, tasks):
        densityCheck, densityValue = density.densityCalcWFraction(tasks)
        if densityCheck == "Schedulable":
            print("Density 5/6 or below\nDensity = " + str(densityValue))
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
        individualDensityList = []
        taskCount = {i:tasks.count(i) for i in tasks}
        finalSchedules = []
        #For resolving issues where schedules such as 2, 2, 3, 3 occur.

        #USE FRACTION HERE
        for i in tasks:
            density = 1/i
            individualDensities[i] = density
            individualDensityList.append(density)
        target = 0.833333333333

        result = [seq for i in range(0, len(individualDensityList)) 
                    for seq in itertools.combinations(individualDensityList, i) 
                    if sum(seq) <= target]

        for j in range(0, len(result)):
            result[j] = list(result[j])
            
            for k in range(0, len(result[j])):
                result[j][k] = list(individualDensities.keys())[list(individualDensities.values()).index(result[j][k])]

        #Above code WORKS but I now must cut it down so that it only include sequences where all values are accounted for - Itertools uses tuples, use lists

        #Code to select all combinations which create 2 full schedules, i,e 2,5 + the rest. or 2, 18, plus the rest

        """this coe is unfinished - many iterations have been completed. The goal is to take the first schedule in the results list
        of lists and check if it has a possible partner by calculating the density of its companion. It will remove the value/s in question
        from the original schedule to check if its partner schedule is 5/6 or under. If it is then we search the results for this particular companion.
        Once this companion is found the resulting two lists will be placed into a tuple and stored to be printed as one possible solution later on
        
        So, find Length of current schedule, exclude all lengths that won't work. Exclude all results that won't have a pair.
        When pair is find, pop them from list, add them to separate list of lists which are the results. Pair them, [([a,b][c,d]).....]"""
        scheduleIterator = 0
        while scheduleIterator < len(result):
            taskCopy = tasks.copy()
            for schedule in result:
                possiblePartners = []
                currentLength = len(schedule)

                for lenSchedule in result:
                    if len(lenSchedule) == len(tasks)-currentLength:
                        possiblePartners.append(lenSchedule)
                    else:
                        continue

                for partners in possiblePartners:
                    partnerCheck = []
                    for partnerTask in partners:
                        partnerCheck.append(partnerTask)
                    for task in schedule:
                        partnerCheck.append(task)
                    partnerCheck.sort()

                    if partnerCheck == tasks:
                        scheduleTuple = (schedule,partners)
                        finalSchedules.append(scheduleTuple)

                        #UNSURE HERE - CHECK
                        result.remove(schedule)
                        result.remove(partners)

                if schedule == result[scheduleIterator]:     

                    scheduleIterator+=1
                    continue

            scheduleIterator+=1
        for i in finalSchedules:
            print(i)
        print(len(finalSchedules))





        #must find all combinations that complete the original full scheudle, i.e. [2, 5] + [6, 8, 10, 12, 14, 16, 18, 18]


Task1 = ScheduleSplit()

Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18])
#Task1.densityCheck([6, 8, 10, 12, 14, 16, 18, 18])


#Task1.densityCheck([2,12,14,16,18])
#Task1.densityCheck([5,6,8,10])
# by friday - Finish density, check schedule split
# by friday - Generate schedule with density above 5/6
# by friday - check scheudle split on those
# saturday - check back here
#######