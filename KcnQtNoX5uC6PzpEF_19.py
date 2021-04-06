
def check_sum(lst,n):
    newlst = [sum([x,y]) for x in lst for y in lst]
    return True if n in newlst else False

