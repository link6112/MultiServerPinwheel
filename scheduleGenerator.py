import numpy as np
from fractions import Fraction
import random
import math
import density


#a = np.random.dirichlet(np.ones(12),size=1)
#print(np.sum(a))
def scheduleGen(selectedDensity):

    k = Fraction(10/6)
    if selectedDensity == "10/6":
        k = Fraction(10/6)
        a = np.random.dirichlet(np.ones(10), size=1)[0]*(k)
    elif selectedDensity == "11/6":
        k = Fraction(11/6)
        a = np.random.dirichlet(np.ones(8), size=1)[0]*(k)
    elif selectedDensity == "graph":
        #print("here")
        k = Fraction(10/6)
        #print(k)
        a = np.random.dirichlet(np.ones(5), size=1)[0]*(k)
    if selectedDensity == "10/6" or selectedDensity == "graph":
        for i in range(0, len(a)):
            b = 1/a[i]
            a[i] = round(b)
        #print(a)
        a.sort()
        a = a.tolist()
        denCheck, densityValue = density.densityCalcWFraction(a)
        #print(a)
        if selectedDensity == "graph":
            return a
        elif denCheck == False:
            print(densityValue)
            return False

        else:
            return a
    else:
        #print(a)
        for i in range(0, len(a)):
            b = 1/a[i]
            a[i] = round(b)
        #print(a)
        a.sort()
        a = a.tolist()
        denCheck, densityValue = density.densityCalcWFraction(a)
        if densityValue <= Fraction(11/6):
            return False
        else:
            return a
    #print(a)
    #print(type(a))
if __name__ == "__main__":
    test = scheduleGen("11/6")
    if test == False:
        print("didn't work")
    else:
        print(density.densityCalcWFraction(test))