from pickletools import read_unicodestringnl
import scheduleGenerator
import density
from fractions import Fraction
import itertools
import scheduleGenerator
from collections import OrderedDict
import solver_naive
import solver_opt
import solver_foresight
test="printstatementcheck"#The goal of this code is to create 2 sets of tasks with
#density less than 5/6

class ScheduleSplit:
    def __init__(self):
        return

    def densityCheck(self, tasks, splitType):
        """
        This function calls the density program which calculates the density of a set of tasks.
        Once checked, if the set of tasks are below 5/6 it assumes schedulability. Over 5/6 it
        realises that the schedule can be split, and subsequently calls the split function.

        Parameters: 
        list - tasks - list of tasks to be checked.

        Returns: None
        """
        densityCheck, densityValue = density.densityCalcWFraction(tasks)
        if splitType == "5/6+5/6" or splitType == "<5/6+1":
            if densityCheck == "Schedulable":
                print("Density 5/6 or below\nDensity = " + str(densityValue))
                return
            elif densityCheck == "Splittable":
                print("Splitting")

                self.split(tasks, splitType)

                return
            else:
                print("Didn't work")
                return
        elif splitType == "11/6":
            self.split(tasks, splitType)
        
    def split(self, tasks, splitType):
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

        if splitType == "5/6+5/6":
            for i in tasks:
                den = Fraction(1,i)
                individualDensities[i] = den
                individualDensityList.append(den)
            target = Fraction(5, 6) #5/6density goal
            target2 = Fraction(3, 6)


            #This use of itertools gives ALL possible combinations of densities that are equal to
            #or below 5/6
            result = [seq for i in range(0, len(individualDensityList)) 
                        for seq in itertools.combinations(individualDensityList, i) 
                        if sum(seq) <= target and sum(seq) >= target2]
        elif splitType == "<5/6+1":
            for i in tasks:
                den = Fraction(1,i)
                individualDensities[i] = den
                individualDensityList.append(den)
            target = Fraction(1, 1) #1/1 density goal
            target2 = Fraction(3, 6)


            #This use of itertools gives ALL possible combinations of densities that are equal to
            #or below 5/6
            result = [seq for i in range(0, len(individualDensityList)) 
                        for seq in itertools.combinations(individualDensityList, i) 
                        if sum(seq) <= target and sum(seq) >= target2]
        elif splitType == "11/6":
            print("11/6 splitting")
            for i in tasks:
                den = Fraction(1,i)
                individualDensities[i] = den
                individualDensityList.append(den)
            target = Fraction(1, 1) #5/6 density goal
            target2 = Fraction(3, 6)


            #This use of itertools gives ALL possible combinations of densities that are equal to
            #or below 5/6
            result = [seq for i in range(0, len(individualDensityList)) 
                        for seq in itertools.combinations(individualDensityList, i) 
                        if sum(seq) <= target and sum(seq) >= target2]


        print("original length: ", len(result))
        result = list(set(result))
        print("optimised length: ",len(result))


        #This code matches each density to its corresponding number and finds all possible combinations with their actual digits
        for j in range(0, len(result)):
            result[j] = list(result[j])            
            for k in range(0, len(result[j])):
                result[j][k] = list(individualDensities.keys())[list(individualDensities.values()).index(result[j][k])]


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

            for schedule in result:
                taskCopy = tasks.copy()
                possiblePartners = []
                currentLength = len(schedule)


                
                for i in schedule:
                    taskCopy.remove(i)
                taskCopyCheck, densityValue = density.densityCalcWFraction(taskCopy)
                scheduleDensityCheck, _ = density.densityCalcWFraction(schedule)
                scheduleCheck = []
                for freq in taskCopy:
                    scheduleCheck.append(freq)
                for freq in schedule:
                    scheduleCheck.append(freq)
                scheduleCheck.sort()
                #print(scheduleCheck)
                if scheduleCheck == tasks:
                    if taskCopyCheck == "Schedulable" and splitType != "11/6":
                        scheduleTuple = (schedule, taskCopy)
                        finalSchedules.append(scheduleTuple)
                        scheduleIterator+=1
                        #if schedule in result:
                        #    result.remove(schedule)
                        #if taskCopy in result:    
                        #    result.remove(taskCopy)
                    elif (taskCopyCheck == "Splittable" and splitType == "<5/6+1"):
                        scheduleTuple = (schedule, taskCopy)
                        finalSchedules.append(scheduleTuple)
                        scheduleIterator+=1
                    elif taskCopyCheck == "Splittable" and splitType == "11/6" and scheduleDensityCheck == "Splittable":
                        scheduleTuple = (schedule, taskCopy)
                        finalSchedules.append(scheduleTuple)
                        scheduleIterator+=1                       
                    else:
                        scheduleIterator+=1
                else:
                    scheduleIterator+=1

                
                
                """
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

                #everything above is dumb, rewrite
                #use set - set to find corresponding schedule
                if schedule == result[scheduleIterator]:     

                    scheduleIterator+=1
                    continue"""

                #scheduleIterator+=1
        count = 0
        for i in finalSchedules:
            #print(i)
            count +=1
            _1, densityValue1 = density.densityCalcPostSplit(i[0])
            _2, densityValue2 = density.densityCalcPostSplit(i[1])
            if _1 == "Possibly Solvable" and _2 == "Possibly Solvable":
                print(_1,densityValue1," | ", _2,densityValue2)
                print(i)
            
                if _1 == "Possibly Solvable":
                    print(i[0])
                    #print("Using solver naive")
                    #solver = solver_naive.solver_naive(i[0], False, True)
                    #solver.solve()
                    print("Using solver foresight")
                    solver = solver_foresight.solver_foresight(i[0], False, True, False)
                    solver.solve()
                if _2 == "Possibly Solvable":
                    print(i[1])
                    solver = solver_foresight.solver_foresight(i[1], False, True, False)
                    solver.solve()

            elif _1 == "Schedulable" and _2 == "Schedulable":
                print(_1,densityValue1," | ", _2,densityValue2)
                #print(i)


        print(len(finalSchedules))







Task1 = ScheduleSplit()

#Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18], "5/6+5/6")
#Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18], "<5/6+1")

k=1
while k <= 1:
    schedule = scheduleGenerator.scheduleGen("10/6")
    #schedule = scheduleGenerator.scheduleGen("11/6")
    if isinstance(schedule, list): 
        Task1.densityCheck(schedule, "5/6+5/6")
        #Task1.densityCheck(schedule, "<5/6+1")
        #Task1.densityCheck(schedule, "11/6")
        print(schedule)
    else:
        continue
    k +=1

#TODO
###################################################################
##Mon - Rewrite main code                                        ##
##Tue - Work with ben 5/6 + 1                                   ##
##Wed - find 5/6 + 5/6 or 5/6 + 1 that isn't poss                ##
##Thu - Loose pinwheel                                           ##
##Fri - Graph loose                                              ##
##Sat - Break                                                    ##
##Sun - Unknown                                                  ##
###################################################################



"""
Where to go next:
Care that both get a feasible sub problem
monday - trueday : Allow schedules where 5/6 and 1 is possible

all week: find pinwheel where density is between 5/6 and 1, and under 5/6

try to make pareto surface 10/6
assign each task a or b, 2 schedules for 2 instances 

schedule: task 1 to task k
          schedule just says there's those tasks.
          task 1 goes to a, task 2 to b, so on and so on

do by hand by sunday: find a loose 2 pinwheel example


below: thursday and friday
--
pareto surfaces not too interesting

could try finding graph way

pyton graph library - test for directed cycle

https://github.com/roarin-roran/Towards-the-5-over-6-Density-Conjecture-of-Pinwheel-Scheduling/blob/a56bfd71bae773606de11614844fb6ae1c8f4a0c/solver_graph.py#L50
https://www.wild-inter.net/publications/html/gasieniec-smith-wild-2022.pdf.html#pf3

state graph - try to edge has passed, 2 tasks schedules - edge set different.
--
"""