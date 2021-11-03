from sys import stdout

def finalPercentage(number):
    """final percentage check"""
    if number >= 60:
        return True
    return False


def classAverage(number):
    """class average"""
    if number >=65:
        return True
    return False

def checkStatus(final_percentage , class_average):
     if finalPercentage(final_percentage) == True and classAverage(class_average) == True:
         return 'Student passed'
     return 'student failed (-: '

if __name__ == '__main__':
    stdout.write(checkStatus(85, 76))

