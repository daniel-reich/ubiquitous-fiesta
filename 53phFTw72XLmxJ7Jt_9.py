
def marathon_distance(d):
    x=0
    if len(d) is 0:
        return False
    else:
        for i in d:
            x=x+abs(i) 
        if x is 25:
            return True
        else:
            return False

