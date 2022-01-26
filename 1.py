"""Write a function to that returns the maximum integer and minimum integer, when an indefinite number of integers are inputted as integer arguments or parameters.
Eg. maximum (1, 2,3, 4,5,6,7)
Returns 7 as maximum and 1 as minimum
minimum (1100,45,456)
Returns 1100 as maximum and 45 as minimum
"""


def maximumAndMininum(*numbers):
    if len(numbers)==0:
        return None
    else:
        maxi = numbers[0]
        mini = numbers[0]
        for i in numbers[1:]:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
        return "maxi =",maxi,"mini =",mini

if __name__ == '__main__':
    print(maximumAndMininum(1,2,4,5,6,7,8,6543,2,3,5,6,4,3))



# MaxMin . 100