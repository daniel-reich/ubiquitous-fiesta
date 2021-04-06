
def waterjug(start, goal):
    full = start
    start = [0, 0, full[2]]
    opFree = {
        "f_0": lambda x: [full[0], x[1], x[2]],
        "f_1": lambda x: [x[0], full[1], x[2]],
        "f_2": lambda x: [x[0], x[1], full[2]],
        "e_0": lambda x: [0, x[1], x[2]],
        "e_1": lambda x: [x[0], 0, x[2]],
        "e_2": lambda x: [x[0], x[1], 0]
    }
​
    def m(a, b, x): return min(x[a], full[b] - x[b])
    opCost = {
        "t01": lambda x: [x[0] - m(0, 1, x), x[1] + m(0, 1, x), x[2]],
        "t02": lambda x: [x[0] - m(0, 2, x), x[1], x[2] + m(0, 2, x)],
        "t10": lambda x: [x[0] + m(1, 0, x), x[1] - m(1, 0, x), x[2]],
        "t12": lambda x: [x[0], x[1] - m(1, 2, x), x[2] + m(1, 2, x)],
        "t20": lambda x: [x[0] + m(2, 0, x), x[1], x[2] - m(2, 0, x)],
        "t21": lambda x: [x[0], x[1] + m(2, 1, x), x[2] - m(2, 1, x)]
    }
​
    visited = [start]
    steps = 0
    flag = 0
​
    while goal not in visited:
        visitedLength = len(visited)
        for F in opFree:
            for x in visited:
                newState = opFree[F](x)
                if newState not in visited and sum(newState) <= full[2]:
                    visited.append(newState)
​
        if goal in visited:
            break
        else:
            flag = 0
            visitedPrev = visited.copy()
            for F in opCost:
                for x in visitedPrev:
                    newState = opCost[F](x)
                    if newState not in visited and sum(newState) <= full[2]:
                        visited.append(opCost[F](x))
                        flag = 1
            if flag:
                steps += 1
        if visitedLength == len(visited):
            return "No solution."
    return steps

