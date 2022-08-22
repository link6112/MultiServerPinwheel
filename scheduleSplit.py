import scheduleGenerator
import density
from fractions import Fraction
import itertools
import scheduleGenerator
from collections import OrderedDict
import solver_foresight
test="printstatementcheck"





#The goal of this code is to create 2 sets of tasks with
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
                #possiblePartners = []
                #currentLength = len(schedule)


                
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
                    elif splitType == "11/6":
                        scheduleTuple = (schedule, taskCopy)
                        finalSchedules.append(scheduleTuple)
                        scheduleIterator+=1                       
                    else:
                        scheduleIterator+=1
                else:
                    scheduleIterator+=1

                


        count = 0
        if __name__ == "__main__":
            for i in finalSchedules:
                print(i)
                count +=1

                taskStatus0, densityValue1 = density.densityCalcPostSplit(i[0])
                taskStatus1, densityValue2 = density.densityCalcPostSplit(i[1])
                #print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)
                #if taskStatus0 == "Possibly Solvable" or taskStatus1 == "Possibly Solvable":
                    #print(i)
                    #print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)



                ####
                #The code below are different print statements for multiple situations which can be
                #"Possibly Solvable" indicates that the set of tasks is over 5/6 but below 1 in density
                #schedulable means it's below 5/6.

                ####

                if (taskStatus0 == "Possibly Solvable" and taskStatus1 == "Possibly Solvable") and splitType == "11/6":
                    print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)
                    #print(i)
                
                    if taskStatus0 == "Possibly Solvable":
                        print(i[0])

                        print("Using solver foresight")
                        solver = solver_foresight.solver_foresight(i[0], False, True, False)
                        solver.solve()
                    if taskStatus1 == "Possibly Solvable":
                        print(i[1])
                        solver = solver_foresight.solver_foresight(i[1], False, True, False)
                        solver.solve()

                else:
                    print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)
                    


                if (taskStatus0 == "Possibly Solvable" or taskStatus1 == "Possibly Solvable") and splitType == "<5/6+1":
                    print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)
                    print(i)
                
                    if taskStatus0 == "Possibly Solvable":
                        print(i[0])

                        print("Using solver foresight")
                        solver = solver_foresight.solver_foresight(i[0], False, True, False)
                        solver.solve()
                    if taskStatus1 == "Possibly Solvable":
                        print(i[1])
                        solver = solver_foresight.solver_foresight(i[1], False, True, False)
                        solver.solve()

                elif taskStatus0 == "Schedulable" and taskStatus1 == "Schedulable" and splitType =="<5/6+1":
                    print(taskStatus0,densityValue1," | ", taskStatus1,densityValue2)
                    #print(i)
                

            print(len(finalSchedules))
        return finalSchedules






if __name__ == "__main__":
    Task1 = ScheduleSplit()

    #Density less than 12/6, possibly solvable based on all under density 1 and above density 5/6 can be solved.
    #not possible in loose pinwheel either.
    #Task1.densityCheck([1,2,5,7,9], "11/6")


    #Task1.densityCheck([2, 2, 3, 3, 6], "11/6")



    #Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18], "5/6+5/6")
    #Task1.densityCheck([2, 5, 6, 8, 10, 12, 14, 16, 18, 18], "<5/6+1")

    k=11
    while k <= 10:
        schedule = scheduleGenerator.scheduleGen("11/6")
        #schedule = scheduleGenerator.scheduleGen("11/6")
        if isinstance(schedule, list): 
            #Task1.densityCheck(schedule, "5/6+5/6")
            #Task1.densityCheck(schedule, "<5/6+1")
            Task1.densityCheck(schedule, "11/6")
            print(schedule)
        else:
            continue
        k +=1

