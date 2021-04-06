
def waterjug(start, goal):
    capA, capB, capC = start
    A, B, C = 0, 0, capC
    goal = tuple(goal)
    if sum(goal) != capC:
        return "No solution."
    moves = {(A, B, C): 0}
    queue = [(A, B, C)]
    while len(queue) > 0:
        curA, curB, curC = queue.pop(0)
        cur_moves = moves[(curA, curB, curC)]
        if curA > 0:
            if curB < capB:
                # water can be filled from jug A to jug B:
                t = min(capB - curB, curA)
                nextA, nextB = curA - t, curB + t
                state = (nextA, nextB, curC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curC < capC:
                # water can be filled from jug A to jug C:
                t = min(capC - curC, curA)
                nextA, nextC = curA - t, curC + t
                state = (nextA, curB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if curB > 0:
            if curA < capA:
                # water can be filled from jug B to jug A:
                t = min(capA - curA, curB)
                nextB, nextA = curB - t, curA + t
                state = (nextA, nextB, curC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curC < capC:
                # water can be filled from jug B to jug C:
                t = min(capC - curC, curB)
                nextB, nextC = curB - t, curC + t
                state = (curA, nextB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if curC > 0:
            if curA < capA:
                # water can be filled from jug C to jug A:
                t = min(capA - curA, curC)
                nextC, nextA = curC - t, curA + t
                state = (nextA, curB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curB < capB:
                # water can be filled from jug C to jug B:
                t = min(capB - curB, curC)
                nextC, nextB = curC - t, curB + t
                state = (curA, nextB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if goal in moves:
            return moves[goal]
    return "No solution."

