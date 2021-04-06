
def ulam(n):
    if n<5: return n
    u = [1,2,3,4,6]
    sums, discard = {7},{5}
    while len(u)<n:
        new = {u[-1]+j for j in u[:-1]} 
        discard=discard|(sums&new)
        sums = ((sums-{u[-1]})^new)-discard
        u.append(min(sums))
        sums.remove(min(sums))
    return u[-1]

