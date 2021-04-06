
import math
def nespers(lst,acc=1):
    acc *= math.factorial(len(lst))
    for thing in lst:
        if type(thing) == list:
            acc = nespers(thing,acc)
    return acc

