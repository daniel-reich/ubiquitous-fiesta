
def order_people(lst, people):
    if people > lst[0] * lst[1]: return 'overcrowded'
    finalArray = []
    for row in range(0, lst[0]):
        tempArray = [x + (row * lst[1]) if x + (row * lst[1]) <= people else 0 for x in range(1, (lst[1]) + 1)]
        if row % 2 != 0: tempArray.reverse()
        finalArray.append(tempArray)
    return finalArray

