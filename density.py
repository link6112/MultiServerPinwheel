def densityCalc(tasks):
    inverseList = []
    for i in tasks:
        inverse = 1/i
        inverseList.append(inverse)
    density = sum(inverseList)

    if density <= 0.833333333333333333333:
        print("Density 5/6 or below!")
        print(density)
    else:
        print("Density is above 5/6")
        print(density)
    
t1 = [2,3, 10]
t2 = [2,3]
densityCalc(t1)

densityCalc(t2)