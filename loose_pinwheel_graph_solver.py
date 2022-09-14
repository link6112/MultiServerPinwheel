import networkx as nx
import time
import itertools
import scheduleGenerator
import scheduleSplit
import density
import solver_foresight
import listGenerator

class loose_solver_graph:
    def __init__(self, tasks):
        self.tasks = tuple(tasks)
        
        self.directedGraph = nx.DiGraph()

        self.statesVisited = []

    """
    def exploreAllChildren(self, state):
        if state not in self.statesVisited:

            self.statesVisited.append(state)

            stateList = list(state)

            for i in range(len(stateList)):
                stateList[i] += 1
            
            for i in range(len(stateList)):
                if stateList[i] > self.tasks[i]:
                    return
            
            for i in range(len(stateList)):
                newState = stateList.copy()
                newState[i] = 0
                newState = tuple(newState)

                self.directedGraph.add_edge(state, newState)
                self.exploreAllChildren(newState)
        return
    """

    def exploreAllChildren(self):
        unexploredStates = []
        exploredStates = []


        initialState = [0] * len(self.tasks)
        unexploredStates.append(initialState)

        while len(unexploredStates) > 0:
            inputState = unexploredStates[0].copy()
            currentState = inputState.copy()
            unexploredStates.pop(0)

            if tuple(currentState) not in exploredStates:
                exploredStates.append(tuple(currentState))

                for i in range(len(currentState)):
                    currentState[i] += 1

                skip = False
                for i in range(len(currentState)):
                    if currentState[i] > self.tasks[i]:
                        skip = True

                if not skip:
                    #for i, for j in same range, if j not less than i
                    for i in range(len(currentState)):
                        for j in range(len(currentState)):
                            #print(currentState)
                            if j <= i:
                                #print(i,j)
                                newState = currentState.copy()
                                newState[i] = 0
                                newState[j] = 0

                            self.directedGraph.add_edge(tuple(inputState), tuple(newState))

                            unexploredStates.append(newState)
                            #print(newState)


    def solve(self):
        startTime = time.time()

        self.exploreAllChildren()

        if len(max(nx.algorithms.components.strongly_connected_components(self.directedGraph), key=len)) > 1:
            print(self.tasks, " is strongly connected! - solvable")
            self.solveTimeCost = time.time() - startTime	
            return True, self.tasks
        else:
            print(self.tasks, " is not strongly connected - unsolvable")
            self.solveTimeCost = time.time() - startTime
            return False, self.tasks
            

def runTestsLooseWins():
    k=0
    while k <= 1000:
        #print("Hello?") 
        schedule = scheduleGenerator.scheduleGen("graph")
        #print(schedule)
        #schedule = scheduleGenerator.scheduleGen("11/6")
        run = True
        for task in schedule:
            if task > 35:
                run = False
        if isinstance(schedule, list) and run == True:
            splitter = scheduleSplit.ScheduleSplit
            solver = loose_solver_graph(schedule)
            #print(schedule)
            solved, task = solver.solve()
            if solved == True:
                print("SUCCESS")
                print(solver.solveTimeCost)
                schedule = splitter.split(splitter, list(task), "<5/6+1")

                print(len(schedule))

                for i in schedule:
                    solved0 = 0
                    solved1 = 0
                    taskStatus0, densityValue1 = density.densityCalcPostSplit(i[0])
                    taskStatus1, densityValue2 = density.densityCalcPostSplit(i[1])


                    solverForesight0 = solver_foresight.solver_foresight(i[0], False, False, False)
                    solverForesight1 = solver_foresight.solver_foresight(i[1], False, False, False)

                    solved0 = solverForesight0.solve()
                    solved1 = solverForesight1.solve()
                    if solved0 == -1 and solved1 == -1:
                        print(i[0], i[1])
                        k = 10000
                        break
                    elif taskStatus1 == "Not Solvable" and solved0 == -1:
                        print(i[0], i[1])
                        k = 10000
                        break
                    elif taskStatus0 == "Not Solvable" and solved1 == -1:
                        print(i[0], i[1])
                        k = 10000
                        break
            else:
                print("BOOOO")
                print(solver.solveTimeCost)
            #k+=1
    return

def runTestsLooseOnly():
    k=0
    while k <= 1000:
        #print("Hello?") 
        schedule = scheduleGenerator.scheduleGen("graph")
        #print(schedule)
        #schedule = scheduleGenerator.scheduleGen("11/6")
        run = True
        for task in schedule:
            if task > 25:
                run = False
        if isinstance(schedule, list) and run == True:
            splitter = scheduleSplit.ScheduleSplit
            solver = loose_solver_graph(schedule)
            print(schedule)
            solved, task = solver.solve()
        else:
            print("BOOOO")
            print(solver.solveTimeCost)
    k += 1
    return
        

        #print(schedule)

    k += 1


#runTestsLooseWins()
#[2, 3] [2, 3, 6]
#[2,2,3,3,6]
#ourPGS = loose_solver_graph([1,2,5,7,9])
#ourPGS = loose_solver_graph([3, 4, 6, 7, 7])
#ourPGS = loose_solver_graph([2, 2, 3, 3, 11, 32])
#ourPGS = loose_solver_graph([16])
#ourPGS = loose_solver_graph([2, 5, 6, 8, 10, 12, 14, 16, 18, 18])
allLists = listGenerator.listGenerator()
solveCount = 0
failCount = 0
print(len(allLists))


for i in allLists:
    print("Starting testing")
    print(i)

    ourPGS = loose_solver_graph(i)
    solved, _ = ourPGS.solve()
    spliter = scheduleSplit.ScheduleSplit

    # solved0 = 0
    # solved1 = 0
    # taskStatus0, densityValue1 = density.densityCalcPostSplit(i[0])
    # taskStatus1, densityValue2 = density.densityCalcPostSplit(i[1])


    # solverForesight0 = solver_foresight.solver_foresight(i[0], False, False, False)
    # solverForesight1 = solver_foresight.solver_foresight(i[1], False, False, False)

    # solved0 = solverForesight0.solve()
    # solved1 = solverForesight1.solve()
    if solved == True:
        solveCount += 1
    elif solved == False:
        failCount +=1
    
    #if solved == True and (solved0 != 1 and taskStatus0)

print("Graph solver fail:", failCount)
print("Graph solver success:", solveCount)


    #print(ourPGS.solveTimeCost)

"""Every edge represent the passing of one day. 
The configuration/state represents the number of days for each task until it has to be done again. 
Now for 2 pinwheel, each edge resets 2 task countdowns back to the frequency and counts down all others by one.
If you have tasks (4,5,8) and a current state (4,2,2) (days until due), there are there edges 
(for the 3 choices of 2 out of 3 tasks), one to (4,5,1), one to (4,1,8) and one to (3,5,8)."""
    