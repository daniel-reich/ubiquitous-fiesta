
def can_traverse(x):
    trans = [[i[j] for i in x] for j in range(len(x[0]))]
    for i,j in zip(trans,trans[1:]):
        if abs((i.count(1)-j.count(1))) >= 2: return False
    return True

