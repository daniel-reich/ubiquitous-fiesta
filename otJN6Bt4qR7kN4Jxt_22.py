
def incremental_depth(lst):
    return eval(str(lst).replace(',',', [')+"]"*(len(lst)-1))

