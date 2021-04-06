
import math
def wash_hands(n, nM):
    mins = ((n*21)*30)*nM/60
    sec = math.ceil(mins)-mins
    return "{} minutes and {} seconds".format(int(mins), int(sec*60))

