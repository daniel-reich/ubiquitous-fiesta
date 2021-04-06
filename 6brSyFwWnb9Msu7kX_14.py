
def pos_neg_sort(lst):
​
    negNumbers = []
    negNumbersIndex = []
    i = 0
​
    while i < len(lst):
        if lst[i] < 0:
            negNumbers.append(lst[i])
            negNumbersIndex.append(i)
        i += 1
    
    posArray = [y for y in lst if y > 0]
    posArray.sort()
​
    i2 = 0
    for negNumber in negNumbers:
        posArray.insert(negNumbersIndex[i2], negNumbers[i2])
        i2 += 1
    return(posArray)

