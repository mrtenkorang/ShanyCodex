

# Finding the factors and Prime Numbers over a period of numbers 



for x in range(2,10+1):
    factorsList = [1]
    for y in range(2,x+1):
        if x%y == 0:
            factorsList.append(y)
    sumList = 0
    for v in factorsList:
        sumList+=v
    print("Sum of the factors of {}".format(x),"= ",sumList)
    if sumList - x == x:
        print("{}".format(x),"is a perfect number")
    else: pass
    print("{} has factors ".format(x), "= ",factorsList)
    print("-----------------------------------------")
    
    
