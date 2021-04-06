
def c_cipher(msg, keyword):
    k = sorted(list(keyword))
    ind = [k.index(i) for i in keyword]
    n = len(keyword)
    if ' ' in msg: 
        msg = [i.lower() for i in msg if i.isalnum()]
        if len(msg)%n:
          msg += ['x']*(n-(len(msg)%n))
        groups = [[msg[j] for j in range(len(msg)) if j%n==i] for i in range(n)]
        g = sorted(groups, key=lambda x:ind[groups.index(x)])
        return ''.join(''.join(i) for i in g)
    else:
        groups = [msg[i:i+len(msg)//n] for i in range(0,len(msg),len(msg)//n)]
        g = sorted(groups, key=lambda x:ind.index(groups.index(x)))
        flip_arr = [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]
        return ''.join(''.join(i) for i in flip_arr)

