
def divisible(arg,state = 'S0'):
    s = {'S0': ['S0','S1'],
        'S1':  ['S2','S0'],
        'S2':  ['S1','S2']}
    if arg == 'stop':
        return 'accept' if state == 'S0' else 'reject'
    if arg == 'state':
        return state
    return lambda x: divisible(x,s[state][arg])

