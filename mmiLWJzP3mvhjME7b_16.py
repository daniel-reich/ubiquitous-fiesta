
def divisible(arg):
    def inner(arg):
        nonlocal state
        if arg == 'state':
            return 'S%s' % state
        elif arg == 'stop':
            return 'reject' if state else 'accept'
        else:
            state = (0,1,2,0,1,2)[2 * state + arg]
            return inner
    state = 0
    return inner(arg)

