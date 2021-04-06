
def can_traverse(x):
    trans_x = list(zip(*x))    
    for i in range(1, len(trans_x)):
        diff = sum(trans_x[i]) - sum(trans_x[i - 1])
        if diff not in {-1, 0, 1}:
            return False
    return True

