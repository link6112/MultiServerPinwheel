import numpy as np
from fractions import Fraction
import random
import math
import density


#a = np.random.dirichlet(np.ones(12),size=1)
#print(np.sum(a))
def scheduleGen():

    k = Fraction(10/6)
    a = np.random.dirichlet(np.ones(14), size=1)[0]*(k)


    for i in range(0, len(a)):
        b = 1/a[i]
        a[i] = round(b)

    a.sort()
    a = a.tolist()
    denCheck, densityValue = density.densityCalcWFraction(a)
    if denCheck == False:
        #print(densityValue)
        return False
    else:
        #print(a)
        return a
    #print(a)
    #print(type(a))
if __name__ == "__main__":
    test = scheduleGen()
    if test == False:
        print("didn't work")
    else:
        print(density.densityCalcWFraction(test))