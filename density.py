from fractions import Fraction

def densityCalcWFraction(tasks):
    density = Fraction(0,1)

    for i in tasks:
        density += Fraction(1,i)
    if density <= 5/6:
        return "Schedulable", density
    elif density <= 10/6:
        return "Splittable", density
    else:
        return False, density

if __name__ == "__main__":
    #t1 = [2,3, 10]
    t2 = [2, 8, 12, 16, 18]
    #print(densityCalcWFraction(t1))
    print(densityCalcWFraction(t2))


