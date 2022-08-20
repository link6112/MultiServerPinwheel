import networkx as nx
import time
import itertools
import scheduleGenerator


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


    def solve(self):
        startTime = time.time()

        self.exploreAllChildren()

        if len(max(nx.algorithms.components.strongly_connected_components(self.directedGraph), key=len)) > 1:
            print(self.tasks, " is strongly connected! - solvable")
            self.solveTimeCost = time.time() - startTime	
            return True
        else:
            print(self.tasks, " is not strongly connected - unsolvable")
            self.solveTimeCost = time.time() - startTime
            return False 
            


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

        solver = loose_solver_graph(schedule)
        print(schedule)
        l = solver.solve()
        if l == True:
            print("SUCCESS")
            print(solver.solveTimeCost)
        else:
            print("BOOOO")
            print(solver.solveTimeCost)
        #print(schedule)

    k += 1
ourPGS = loose_solver_graph([3, 4, 6, 7, 7])
ourPGS.solve()
print(ourPGS.solveTimeCost)

"""Every edge represent the passing of one day. 
The configuration/state represents the number of days for each task until it has to be done again. 
Now for 2 pinwheel, each edge resets 2 task countdowns back to the frequency and counts down all others by one.
If you have tasks (4,5,8) and a current state (4,2,2) (days until due), there are there edges (for the 3 choices of 2 out of 3 tasks), one to (4,5,1), one to (4,1,8) and one to (3,5,8)."""
    