# Define a function that takes in 2 strings and return every character the strings have in common
# Eg. common("hello","world") 
# returns "lo"


def searchSimilar(stringOne, stringTwo):
    simi = []  # created an empty list
    for i in stringOne:  # iterate over stringOne
        for x in stringTwo:  # create a nested iteration over stringTwo
            if i==x:  # set condition to check similar letters
                simi.append(i)  # add similar letters to the set
    simiString =str(set(simi))  # explicitly convert the list to a set and to a string
    return simiString, "  ",type(simiString)


if __name__ == '__main__':
    print(searchSimilar('hello','world'))
