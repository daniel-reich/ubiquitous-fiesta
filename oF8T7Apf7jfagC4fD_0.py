
def antipodes_average(lst):
    return [(lst[i] + lst[-i-1])/2 for i in range(len(lst)//2)]

