
def change_to_0(arg):
    if arg == 'state':
        return 'S0'
    if arg == 'stop':
        return 'accept'
    if arg == 1:
        return change_to_1
    return change_to_0
​
​
def change_to_1(arg):
    if arg == 'state':
        return 'S1'
    if arg == 'stop':
        return 'reject'
    if arg == 1:
        return change_to_0
    else:
        return change_to_2
​
​
def change_to_2(arg):
    if arg == 'state':
        return 'S2'
    if arg == 'stop':
        return 'reject'
    if arg == 0:
        return change_to_1
    return change_to_2
​
​
def divisible(arg):
    if arg == 1:
        return change_to_1
    return change_to_0(arg)

