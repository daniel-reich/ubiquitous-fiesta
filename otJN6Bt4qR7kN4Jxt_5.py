
def incremental_depth(lst):
    i = [lst[-1]]
    for x in lst[-2::-1]:
        z = [x, i]
        i = z
    return i

