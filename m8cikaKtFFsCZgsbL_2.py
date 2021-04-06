
def process(state,i,others,capacities):
    '''
    Returns the jug states possible from permissible changes to state[i]
    '''
    possibles = []
    temp = list(state)
    temp[i] = 0  # can always empty it!
    possibles.append(tuple(temp))
    for pos in others:
        temp = list(state)
        pourable = min(temp[i],capacities[pos] - temp[pos])
        temp[i] -= pourable
        temp[pos] += pourable
        possibles.append(tuple(temp))  # water poured from i.
​
    return possibles
    
def get_states(state, capacities):
    '''
    Returns a list of all the states possible from this one, based on
    permissible actions
    '''
    states = []
    size = len(state)
    for i in range(size):
        if state[i]:  # it's got some water
            others = sorted(set(range(size)) - {i})
            states += process(state,i,others,capacities)
​
    return states
​
def waterjug(capacities, target):
    '''
    Returns the minimum number of moves to reach target from the start state,
    or 'No solution' if not possible, given constraints and operations as per
    the instructions.
    '''
    CAPS = {i:jug for i, jug in enumerate(capacities)}
    start = (0,0,CAPS[2])
    target = tuple(target)
    if sum(target) > start[2]:
        return 'No solution.'
​
    q = [start]
    visited = set()
    path = {start:0}
​
    while q:
        state = q.pop(0)
        visited.add(state)
        if state == target:
            count = 0
            current = target
            while current != start:
                count += 1
                current = path[current]
​
            return count
​
        for next_state in get_states(state,CAPS):  # all states possible from here
            if next_state not in visited and next_state not in q:
                path[next_state] = state  # show it came from here
                q.append(next_state)
​
    return 'No solution.'  # did not find target

