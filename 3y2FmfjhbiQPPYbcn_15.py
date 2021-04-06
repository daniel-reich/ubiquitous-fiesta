
def pop(state):
    m = state[len(state)//2]
    c = m
    for i in range(len(state)):
        state[i] = i
        if i > m:
            c -= 1
            state[i] = c
    return state

