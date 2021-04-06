
def sum_two_smallest_nums(lst):
    newList = []
    z = [str(i) for i in lst]
    for num in range(len(z)):
        if int(z[num]) >= 0:
            newList.append(z[num])
    newList = [int(i) for i in newList]
    newList = sorted(newList)
​
    return int(newList[0]) + int(newList[1])

