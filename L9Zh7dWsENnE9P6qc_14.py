
def josephus(n):
    if n == 1: return n
    pri = [i for i in range(n)]
    sur = [i for i in pri if i not in pri[1::2]]
    pri = ['-']*len(pri) + sur
    while len(sur) > 1:
        sur = [i for i in pri if i not in pri[1::2]]
        pri = ['-']*len(pri) + sur
    return sur[0]+1

