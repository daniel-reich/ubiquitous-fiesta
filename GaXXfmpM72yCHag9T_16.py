
def unique(lst):
    result = []
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            result.append(lst[i])
​
    return result[0]

