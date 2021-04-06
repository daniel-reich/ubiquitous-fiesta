
def pop(state):
    s = sum(state)
    if s == 0:
        return state
    cur = state.index(s) - 1
    water = s - 1
    while cur >= 0 and water > 0:
        state[cur] = water
        cur -= 1
        water -= 1
    cur = state.index(s) + 1
    water = s - 1
    while cur < len(state) and water > 0:
        state[cur] = water
        cur += 1
        water -= 1
    return state

