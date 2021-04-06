
def fsa(state, *args):
    if type(args) == tuple:
        arg = args[0]
    if arg in [0, 1]:
        old_state = state
        if state == 'S0':
            state = 'S0' if arg == 0 else 'S1'
        elif state == 'S1':
            state = 'S2' if arg == 0 else 'S0'
        elif state == 'S2':
            state = 'S1' if arg == 0 else 'S2'
        return lambda x: fsa(state, x)
    if arg == 'state':
        return state
    if arg == 'stop':
        return 'accept' if state == 'S0' else 'reject'
    
def divisible(*args):
    if type(args[0]) == str:
        if args[0] == 'state':
            return 'S0'
        else:
            return 'accept'
    state = 'S0'
    arg = args[0]
    if arg in [0, 1]:
        if state == 'S0':
            state = 'S0' if arg == 0 else 'S1'
        elif state == 'S1':
            state = 'S2' if arg == 0 else 'S0'
        elif state == 'S2':
            state = 'S1' if arg == 0 else 'S2'
        return lambda x: fsa(state, x)
    return lambda x: fsa('S0', x)

