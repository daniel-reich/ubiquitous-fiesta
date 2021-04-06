
def min_miss_pos(lst):
    return [i for i in range(1,len(lst)+2) if i not in lst][0]

