
def divisible(arg, state='S0'):
    d = {'S0':('S0', 'S1'),
         'S1':('S2', 'S0'),
         'S2':('S1', 'S2'),}
    
    if arg == 'state': return state
    if arg == 'stop': return ['accept', 'reject'][state != 'S0']
    return lambda a: divisible(a, d[state][arg])

