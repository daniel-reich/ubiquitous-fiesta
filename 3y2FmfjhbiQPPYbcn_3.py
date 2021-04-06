
def pop(state):
    balloon_pos = len(state) // 2
    counter = balloon_pos
    for x in range((balloon_pos-1), 0, -1):
        counter -= 1
        state[x] = counter
    counter = balloon_pos
    for x in range((balloon_pos+1), len(state)):
        counter -= 1
        state[x] = counter
    return state

