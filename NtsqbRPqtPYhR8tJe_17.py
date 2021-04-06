
def blocks(step):
    n=5
    if step==0:
        return 0
    else:
        for i in range(7,7+step-1):
            n=n+i
    return n

