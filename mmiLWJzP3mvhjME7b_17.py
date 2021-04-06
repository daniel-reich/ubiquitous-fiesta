
def divisible(arg, current_state='S0'):
    if arg == 0:
        if current_state == 'S0':
            pass
        elif current_state == 'S1':
            current_state = 'S2'
        elif current_state == 'S2':
            current_state = 'S1'
    elif arg == 1:
        if current_state == 'S0':
            current_state = 'S1'
        elif current_state == 'S1':
            current_state = 'S0'
        elif current_state == 'S2':
            pass
    elif arg == 'state':
        return current_state
    elif arg == 'stop':
        if current_state == 'S0':
            return 'accept'
        else:
            return 'reject'
    return lambda x: divisible(x, current_state=current_state)

