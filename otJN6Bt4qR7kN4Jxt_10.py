
def incremental_depth(lst):
    lst1 = [lst[-1]]
    for i in range(2, len(lst)+1):
        lst1 = [lst[-1*i]]+[lst1]
    return lst1

