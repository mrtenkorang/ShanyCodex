# Write a function "perfect()" that determines if parameter number is a perfect number. Use 
# this function in a program that determines and prints all the perfects numbers between 1 and 1000



def perfectNumber(number):
    """A perfect number has the sum of it factors, excluding the number itself equal to the number """
    factorList = [1] # this list will hold the factors of a given number at a time
    intCount = 1 # create a variable count
    while intCount < number: # set a condition to check iteration
        intCount+=1  # increase iteration by one
        if number%intCount !=0:
            pass
        else:
            factorList.append(intCount)
    # checking if the factors are == to the number itself
    sumList = 0
    for i in factorList:
        sumList+=i
    if sumList-number == number:
        return True
    else:
        return False


if __name__ == '__main__':
    countNatural = 0
    while countNatural <1001:
        countNatural+=1
        if perfectNumber(countNatural):
            print(countNatural, "is a perfect number")
        else:
            pass




