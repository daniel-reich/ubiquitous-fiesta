
import functools
​
def divisible(arg, state='S0'):
    d = {
        'S0': ['S0', 'S1'],
        'S1': ['S2', 'S0'],
        'S2': ['S1', 'S2']
    }
    if arg == 'state':
        return state
    elif arg == 'stop':
        return 'accept' if state == 'S0' else 'reject'
    else:
        return functools.partial(divisible, state=d[state][arg])

