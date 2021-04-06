
import operator
def digit_sort(lst):
    temp = []
    for i in range(len(lst)):
        temp.append([lst[i],len(str(lst[i]))])
​
    temp = sorted(temp, key = operator.itemgetter(0))
    temp = sorted(temp, key = operator.itemgetter(1),reverse=True)
    myans = []
    for i in range(len(temp)):
        myans.append(temp[i][0])
​
    return myans

