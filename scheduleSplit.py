from pickletools import read_unicodestringnl
import scheduleGenerator
import density
from fractions import Fraction
import itertools
import scheduleGenerator
from collections import OrderedDict
test="printstatementcheck"
#The goal of this code is to create 2 sets of tasks with
#density less than 5/6

class ScheduleSplit:
    def __init__(self):
        return

    def densityCheck(self, tasks):
        """
        This function calls the density program which calculates the density of a set of tasks.
        Once checked, if the set of tasks are below 5/6 it assumes schedulability. Over 5/6 it
        realises that the schedule can be split, and subsequently calls the split function.

        Parameters: 
        list - tasks - list of tasks to be checked.

        Returns: None
        """
        densityCheck, densityValue = density.densityCalcWFraction(tasks)
        if densityCheck == "Schedulable":
            print("Density 5/6 or below\nDensity = " + str(densityValue))
            return
        elif densityCheck == "Splittable":
            print("Splitting")
            self.split(tasks)
            return
        else:
            return
        
    def split(self, tasks):
        """
        This function takes a set of tasks with density between 5/6 and 10/6 and splits them.

        Parameters:
            list - tasks - tasks to be split.
        Returns:
            All possible schedules.
        """
        serverA = []
        serverB = []
        individualDensities = {}
        individualDensityList = []
        taskCount = {i:tasks.count(i) for i in tasks}
        finalSchedules = []

        #Creates a list of the densities of each task.
        #Can return to:
        """
        for i in tasks:
            den = 1/i
            individualDensitiesd[i] = den
            individualDensityList.append(den)
        target = 0.83333333333
        """
        for i in tasks:
            den = Fraction(1,i)
            individualDensities[i] = den
            individualDensityList.append(den)
        target = Fraction(5, 6) #5/6 density goal
        target2 = Fraction(3, 6)
        #print("passed creation")

        #This use of itertools gives ALL possible combinations of densities that are equal to
        #or below 5/6
        result = [seq for i in range(0, len(individualDensityList)) 
                    for seq in itertools.combinations(individualDensityList, i) 
                    if sum(seq) <= target and sum(seq) >= target2]

        ##
        #bitvector of size n, iterate over all possible bits
        #is element in subset a, yes if a, no if b.

        #10/6
        ##

        print("original length: ", len(result))
        result = list(set(result))
        print("optimised length: ",len(result))
        #print("passed itertools")


        #This code matches each density to its corresponding number and finds all possible combinations with their actual digits
        for j in range(0, len(result)):
            result[j] = list(result[j])            
            for k in range(0, len(result[j])):
                result[j][k] = list(individualDensities.keys())[list(individualDensities.values()).index(result[j][k])]
        #print(result)

        #This code is relatively complicated.
        #It will iterate over every single combination, it will check to see if a partner exists.
        #For [2, 5, 6, 8, 10, 12, 14, 16, 18, 18] the code will create a split with just [18,18] by itself, but there will
        #be no partner as its partner would have a density of greater than 5/6. So it will match it to all
        #sets of tasks with 8 tasks in them.
        #The code then checks if the partners matched are equal to the original set of tasks passed into this function, if 
        #they are not equal then the code continues to run until it finds its partner, if it cannot then this particular
        #split is not allowed. It will move on to the next result with a density of 5/6 or below. Eventually
        #The code will have fully split all tasks into schedulable schedules.
        scheduleIterator = 0
        while scheduleIterator < len(result):
            #taskCopy = tasks.copy()
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
                        if schedule in result:
                            result.remove(schedule)
                        if partners in result:    
                            result.remove(partners)

                if schedule == result[scheduleIterator]:     

                    scheduleIterator+=1
                    continue

            scheduleIterator+=1
        #for i in finalSchedules:
        #    print(i)
        #    _2, densityValue1 = density.densityCalcWFraction(i[0])
        #    _1, densityValue2 = density.densityCalcWFraction(i[1])
        #    print(_2,densityValue1," | ", _1,densityValue2)
        #if len(finalSchedules) == 0:
        #    print(result)
        print(len(finalSchedules))
        #print("Success")




        #must find all combinations that complete the original full scheudle, i.e. [2, 5] + [6, 8, 10, 12, 14, 16, 18, 18]


Task1 = ScheduleSplit()

Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18])
#Task1.densityCheck([2,2,3,3])
#Task1.densityCheck([6, 8, 10, 12, 14, 16, 18, 18])
k=1
#while k <= 1:
#    schedule = scheduleGenerator.scheduleGen()
#    if isinstance(schedule, list): 
#        Task1.densityCheck(schedule)
#        print(schedule)
#    else:
#        continue
#    k +=1

#TODO
###################################################################
##Mon - Thoroughly test - Attempt schedule generator             ##
##Tue - Understand Ben's code to extend this program             ##
##Wed - Add 11/6 and higher densities - Split to                 ##
##    - one 5/6 and one higher to see if it is possible.         ##
##Thu - MEETING POSS                                             ##
##Fri - MEETING POS- Return here                                 ##
##Sat - Break                                                    ##
##Sun - Unknown                                                  ##
###################################################################



"""
Where to go next:
Care that both get a feasible sub problem
Allow schedules where 5/6 and 1 is possible

find pinwheel where density is between 5/6 and 1, and under 5/6

try to make pareto surface 10/6
assign each task a or b, 2 schedules for 2 instances 

schedule: task 1 to task k
          schedule just says there's those tasks.
          task 1 goes to a, task 2 to b, so on and so on

find a loose 2 pinwheel example
"""