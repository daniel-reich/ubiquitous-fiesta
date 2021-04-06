
def foil(length):
    turns=0
    while length >0:
        length= length- 3.1416*(4+turns*.005)
        turns+=1
        if -length > .5*3.1416*(4+turns*.005): turns-=.5
    return round(turns*.005+4,4)

