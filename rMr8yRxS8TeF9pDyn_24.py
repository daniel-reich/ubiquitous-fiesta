
def war_of_numbers(lst):
    numLst = sorted([sum(i for i in lst if i % 2 == 0),sum(i for i in lst if i % 2 != 0)])
    return numLst[1] - numLst[0]

