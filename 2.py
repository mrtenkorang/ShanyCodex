"""A young boy was sent by his mother to get some eggs from a nearby supermarket for his birthday party.
On his way home, he was knocked down by a motorist and had all the eggs broken. The boy was unhurt and the motorist agreed to pay for the eggs.
The boy could not remember the exact number of eggs, only that when he took them out in pairs there was one left; similarly there was one left 
when he took them out threes, fours, fives, or sixes at a time. When he took them out in sevens at a time they came out even, that is there was nothing left.
You are required to write a computer solution to determine the smallest number of eggs the boy 
could have had and the total cost if the boy claims that he paid 4 pesewas per egg.  """


if __name__ == '__main__':
    eggCount = 0 # create a count variable and start with zero
    while True: # Search for the number with this infinite loop
        eggCount +=1 # Increase the count by each iteration
        """ The conditions below must be met, at each iteration or else that number or count is not the 
            right number. Nested Loops are the best alternative for this question
        """
        if eggCount%2==1: # if the count or number qualifies this condition,then it moves to the next
            if eggCount%3==1: # which is this , if it is sucessful, then it moves to the next
                if eggCount%4 ==1: # which is this , if it is sucessful, then it moves to the next
                    if eggCount%5==1: # which is this , if it is sucessful, then it moves to the next
                        if eggCount%6==1: # which is this , if it is sucessful, then it moves to the next
                            if eggCount%7==0: #until the last and if it qualifies, you break the loop and print the number.
                                print("egg count = ",eggCount, " <===> total cost of egg = ",eggCount*0.4,"Cedis")
                                break
