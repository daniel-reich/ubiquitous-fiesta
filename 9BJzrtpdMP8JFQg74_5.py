
def twins(lst):
    for i in range(1, len(lst)):
        temp = []
        temp.append(lst[:i])
        temp.append(lst[i:])
        if sum(temp[0]) == sum(temp[1]):
            return i

