
def percentage_changed(old,new):
    
    old = int(old[1:])
    new = int(new[1:])
​
    result = int(((new-old)/old)*100)
​
    if result < 0:
        result = -1 * result
        return "{}% decrease".format(result)
    else:
        return "{}% increase".format(result)

