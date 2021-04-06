
from collections import deque
​
​
def waterjug(start, goal):
    lastJugCapacity = start[-1]
    sizes = start
    goal = tuple(goal)
    initial = tuple(([0] * (len(start) - 1)) + [start[-1]])
​
    clones = deque([(initial, 0, "initial", [initial])])
    calculated = set()
​
    while clones:
        jugs, step, move, path = tuple(clones.popleft())
​
        if jugs in calculated:
            continue
        else:
            calculated.add(jugs)
​
        if jugs == goal and sum(jugs[:-1]) != lastJugCapacity:
            # for j, s, m in path:
            #     print("{} {} {}".format(j, s, m))
            return step
​
        for i, (jug, jugSize) in enumerate(zip(jugs, sizes)):
            # empty jug
            if jug > 0:
                clone = list(jugs)
                clone[i] = 0
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "empty {}".format(i), path + [(jugs, step, move,)]))
            # fill jug
            if jug < jugSize:
                clone = list(jugs)
                clone[i] = jugSize
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "fill {}".format(i), path + [(jugs, step, move,)]))
​
            for j, (targetJug, targetJugSize) in enumerate(zip(jugs, sizes)):
                if i == j:
                    continue
                if targetJug == targetJugSize:
                    continue
                if jug == 0:
                    continue
​
                before = jug + targetJug
                toTranfer = min(jug, targetJugSize - targetJug)
​
                clone = list(jugs)
                clone[i] -= toTranfer
                clone[j] += toTranfer
                assert clone[i] + clone[j] == before
​
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "move {} to {}".format(i, j), path + [(jugs, step, move,)]))
    return "No solution."

