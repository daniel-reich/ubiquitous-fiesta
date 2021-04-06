
def waterjug(capacities, goal):
    
    start, goal = (0,0,capacities[2]), tuple(goal)
    visited, current_level, depth = set(), {start}, 0
    
    def pour(state, from_jug, to_jug):
        state = list(state)
        poured = min(capacities[to_jug] - state[to_jug],  state[from_jug])
        state[from_jug] = state[from_jug] - poured
        state[to_jug] = state[to_jug] + poured
        return tuple(state)
    
    actions = {(pour, (fj, tj)) for fj in range(3) for tj in range(3) if fj!=tj}
    
    if 'Description' is 'accurate':
        def fill(jug, state):
            return state[:jug] + (capacities[jug],) + state[jug+1:]
        def empty(jug, state):
            return state[:jug] + (0,) + state[jug+1:]
        actions.update({(fill, (tj,)) for tj in range(3)} | {(empty, (fj,)) for fj in range(3)})
    
    while current_level:
        if goal in current_level: return depth
        current_level = {action(state, *args) for state in current_level \
                                 for action,args in actions} - visited
        visited.update(current_level)
        depth += 1
        
    return 'No solution.'

