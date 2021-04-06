
def reversible_inclusive_list(start_of_range, end_of_range):
    res =[]
    if start_of_range>end_of_range:
        for i in range(start_of_range,end_of_range-1,-1):res.append(i)
    else:
        for i in range(start_of_range,end_of_range+1):res.append(i)
    return res

