
moves = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]
def wj_recur(caps, goal, current, tried, depth=0):
    if current == goal: return depth
    ct = tuple(current)
    if ct in tried and tried[ct] <= depth: return False
    tried[ct] = depth
    best = float('inf')
    for move in moves:
        if current[move[0]] > 0 and current[move[1]] < caps[move[1]]:
            trial = current[::]
            tfr = min(trial[move[0]], caps[move[1]] - trial[move[1]])
            trial[move[0]] -= tfr
            trial[move[1]] += tfr
            res = wj_recur(caps, goal, trial, tried, depth+1)
            if res:
                best = min(res, best)
    return best
    
def waterjug(start, goal):
    res = wj_recur(start, goal, [0, 0, start[2]], {})
    return res if res != float('inf') else 'No solution.'

