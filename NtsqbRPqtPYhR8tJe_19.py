
def blocks(step):
    n = 5
    diff = 7
    if step == 0:
        return 0
    elif step == 1:
        return 5
    else:
        return n + (step-1)*(7 + 7+step-2)/2

