
def clear_ordering(lst):
    firstDict = {}
    secondDict = {}
    for item in lst:
        if item[0] in firstDict:
            firstDict[item[0]] += 1
        else:
            firstDict[item[0]] = 1         
        if item[1] in secondDict:
            secondDict[item[1]] += 1
        else:
            secondDict[item[1]] = 1
    for item in firstDict:
        if firstDict[item] > 1:
            return False
    for item in secondDict:
        if secondDict[item] > 1:
            return False
    return True

