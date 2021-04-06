
def farey(n):
    lst = [str(i)+'/'+str(j) for i in range(0, n+1) for j in range(1, n+1) if i%j != 0 and i/j < 1]
    aux  = []
    for i in lst:
        if eval(i) not in aux:
            aux.append(eval(i))
            aux.append(i)
    aux = [i for i in aux if isinstance(i, str) == True]
    aux_eval = sorted([eval(i) for i in aux])
    res = ['0/1'] + [j for i in aux_eval for j in aux if eval(j) ==  i] + ['1/1']
    return res

