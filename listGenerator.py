from fractions import Fraction
import csv
def listGenerator():
    testingList = [1] * 4


    allLists = []

    #print(sum(testingList))

    #print(allLists)
    for i in range(1,17):
        testingList[0] = i
        density = Fraction(0,1)
        for k in testingList:
            density += Fraction(1, k)
        if density >= 0.75 and density <=2:
            testListCopy = testingList.copy()
            allLists.append(testListCopy)
        for k in range(1,17):
            testingList[1] = k
            density = Fraction(0,1)
            for k in testingList:
                density += Fraction(1, k)
            if density >= 0.75 and density <=2:
                testListCopy = testingList.copy()
                allLists.append(testListCopy)
            for l in range(1,17):
                testingList[2] = l

                density = Fraction(0,1)
                for k in testingList:
                    density += Fraction(1, k)
                if density >= 0.75 and density <=2:
                    testListCopy = testingList.copy()
                    allLists.append(testListCopy)
                for p in range(1,17):
                    testingList[3] = p
                    for k in testingList:
                        #print(testingList)
                        density += Fraction(1, k)
                    if density >= 0.75 and density <=2:
                        testListCopy = testingList.copy()
                        allLists.append(testListCopy)
                    # for n in range(1,17):
                    #     testingList[4] = n
                    #     density = Fraction(0,1)
                    #     for k in testingList:
                    #         density += Fraction(1, k)
                    #     if density >= 0.75 and density <=2:
                    #         testListCopy = testingList.copy()
                    #         allLists.append(testListCopy)
    print(len(allLists))

    for i in allLists:
        i = i.sort()

    #print(len(allLists))
    #b_set = set(map(tuple(allLists)))
    #allLists = map(list(b_set))
    #print(len(allLists))




    # density = Fraction(0,1)
    # #print(density)
    # deleteList = []
    # for i in range(0, len(allLists)):
    #     density = Fraction(0,1)

    #     for k in allLists[i]:
    #         density += Fraction(1, k)

    #     if density >= Fraction(3/4) and density <= Fraction(8/4):
    #         deleteList.append(i)

    # print(len(allLists))
    # for i in reversed(deleteList):
    #     allLists.pop(i)

    # print(len(allLists))
    return allLists



def listGeneratorVariableK():
    k = 5
    testingList = [1] * k

    
    allLists = []
    n = 2**(k-1)
    n = n+1

    print(n)
    density = Fraction(0,1)
    #while (sum(testingList) < 192):

    allLists.append(testingList)
    #print(allLists)
    for i in range(1,n):
        #print(testingList)
        testingList[0] = i
        density = Fraction(0,1)
        for b in testingList:
            density += Fraction(1, b)
            #print(density)
        if density >= Fraction(10,6) and density <= Fraction(11,6):

            testListCopy = testingList.copy()
            allLists.append(testListCopy)
        for k in range(1,n):
            #print(testingList)
            density = Fraction(0,1)
            testingList[1] = k
            for b in testingList:
                density += Fraction(1, b)
            if density >= Fraction(10,6) and density <= Fraction(11,6):
                testListCopy = testingList.copy()
                allLists.append(testListCopy)

            for l in range(1,n):
                #print(testingList)

                testingList[2] = l
                density = Fraction(0,1)
                for b in testingList:

                    density += Fraction(1, b)
                if density >= Fraction(10,6) and density <= Fraction(11,6):
                    testListCopy = testingList.copy()
                    allLists.append(testListCopy)
                for v in range(1,n):
                    testingList[3] = v
                    density = Fraction(0,1)
                    for b in testingList:
                        density += Fraction(1, b)
                    if density >= Fraction(10,6) and density <= Fraction(11,6):
                            testListCopy = testingList.copy()
                            allLists.append(testListCopy)
                    for x in range(1,n):
                        testingList[4] = x
                        density = Fraction(0,1)
                        for b in testingList:
                            density += Fraction(1, b)
                        if density >= Fraction(10,6) and density <= Fraction(11,6):
                            testListCopy = testingList.copy()
                            allLists.append(testListCopy)
                #        for a in range(1,n):

                #             testingList[5] = a
                #             density = Fraction(0,1)
                #             for b in testingList:
                #                 density += Fraction(1, b)
                #             if density < Fraction(10,6) or density > Fraction(11,6):
                #                 testListCopy = testingList.copy()
                #                 allLists.append(testListCopy)







    print(len(allLists))

    for i in allLists:
        i = i.sort()
    #between 0.75 and 2.
    """     density = Fraction(0,1)
    #print(density)
    deleteList = []
    for i in range(0, len(allLists)):
        density = Fraction(0,1)

        for k in allLists[i]:
            density += Fraction(1, k)
        if density >= Fraction(10,6) and density <= Fraction(11,6):
            deleteList.append(i)

    print(len(allLists))
    for i in reversed(deleteList):
        allLists.pop(i)

    print(len(allLists))
    print(allLists) """

    return allLists

#list = listGenerator()
# for i in list:
#     print(i)
    #2^(k-1) <- max element value

    #citing our kernalisation conjecture - between 10/6 and 11/6
    #start at k=3