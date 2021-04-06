
def waterjug(start, goal):
    source = [[0, 0, start[2]]]
    result = inception(source, start, goal, 0)
    return result
​
def pour(source, destination, jugs, capacity):
    localJugs = [x for x in jugs]
    pourableAmt = capacity[destination] - localJugs[destination]
    if localJugs[source] > pourableAmt:
        localJugs[source] -= pourableAmt
        localJugs[destination] += pourableAmt
    else:
        localJugs[destination] += localJugs[source]
        localJugs[source] = 0
​
    return localJugs
​
def inception(jugArray, capacity, goal, level):
    tempArr = []
    if level == 10:
        return "No solution."
    if goal in jugArray:
        return level
​
    for jugs in jugArray:
        for x in range(3):
            for y in range(3):
                if jugs != pour(x, y, jugs, capacity):
                    tempArr.append(pour(x, y, jugs, capacity))
    
    level += 1
    jugArray = tempArr
    level = inception(jugArray, capacity, goal, level)
    return level

