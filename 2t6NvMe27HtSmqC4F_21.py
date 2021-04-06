
import copy
​
def boolean_and(lst):
    temp = copy.deepcopy(lst)
    while len(temp) > 1:
        temp = copy.deepcopy(lst)
        lst = []
        for i in range(len(temp)-1):
            if temp[i]==True and temp[i+1] == True:
                lst.append(True)
            else:
                lst.append(False)
    return temp[0]
​
def boolean_or(lst):
    temp = copy.deepcopy(lst)
    while len(temp) > 1:
        temp = copy.deepcopy(lst)
        lst = []
        for i in range(len(temp)-1):
            if temp[i]==True or temp[i+1] == True:
                lst.append(True)
            else:
                lst.append(False)
    return temp[0]
​
def boolean_xor(lst):
    temp = copy.deepcopy(lst)
    while len(temp) > 1:
        temp = copy.deepcopy(lst)
        lst = []
        for i in range(len(temp)-1):
            if temp[i] + temp[i+1] == 1:
                lst.append(True)
            else:
                lst.append(False)
    return temp[0]

