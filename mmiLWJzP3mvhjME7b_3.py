
fsa = {
    0: {0: 0, 1: 1},
    1: {1: 0, 0: 2},
    2: {1: 2, 0: 1}
}
​
def divisible(arg):
    state = 0
    def handler(arg):
        nonlocal state
        if arg == 'stop':
            return 'accept' if state == 0 else 'reject'
        if arg == 'state':
            return 'S' + str(state)
        state = fsa[state][arg]
        return handler
    return handler(arg)

