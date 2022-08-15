from fractions import Fraction

def densityCalcWFraction(tasks):
    density = Fraction(0,1)

    for i in tasks:
        #print(tasks)
        density += Fraction(1,i)
    if density <= 5/6:
        return "Schedulable", density
    elif density >5/6 and density <= 10/6:
        return "Splittable", density
    else:
        return False, density

if __name__ == "__main__":
    #t1 = [2,3, 10]
    t2 = [2, 8, 12, 16, 18]
    t3 = [2, 6, 2, 4, 3, 3, 131, 14]
    t3 = [2, 3, 5, 5, 5, 7, 9, 11, 13, 30, 52, 52]
    t3 = [3, 3, 5, 6, 8, 9, 14, 14, 15, 19]
    #print(densityCalcWFraction(t1))
    print(densityCalcWFraction(t3))


