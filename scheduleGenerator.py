import numpy as np
from fractions import Fraction
import random
import math
import density


#a = np.random.dirichlet(np.ones(12),size=1)
#print(np.sum(a))
def scheduleGen():
    k = Fraction(10/6)
    a = np.random.dirichlet(np.ones(12), size=1)[0]*(k)
    #print(a)
    #print(np.sum(a))

    for i in range(0, len(a)):
        b = 1/a[i]
        a[i] = round(b)

    a.sort()
    a = a.tolist()
    print("Schedule made")
    return a
    #print(a)
    #print(type(a))

test = scheduleGen()

print(density.densityCalcWFraction(test))