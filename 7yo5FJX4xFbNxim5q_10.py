
def harry(p):
    if p[0]==[]:  return -1
    m = list(zip(*p))
    return max(sum(p[0])+sum(m[-1])-p[0][-1], sum(p[-1])+sum(m[0])-p[-1][0])

