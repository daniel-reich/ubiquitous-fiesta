
def boolean_and(lst):
    temp = lst[:]
    while len(temp) > 1:
        temp[0] = temp[0] and temp[1]
        temp.pop(1)
    return temp[0]
​
def boolean_or(lst):
    temp = lst[:]
    while len(temp) > 1:
        temp[0] = temp[0] or temp[1] 
        temp.pop(1)
    return temp[0]
​
def boolean_xor(lst):
    temp = lst[:]
    while len(temp) > 1:
        if temp[:2] == [True, True]:
            temp[0] = False
        else:
            temp[0] = temp[0] or temp[1] 
        temp.pop(1)
    return temp[0]

