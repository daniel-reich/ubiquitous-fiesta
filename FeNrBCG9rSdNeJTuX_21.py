
def max_possible(n1, n2):
    t1 = [int(i) for i in str(n1)]
    t2 = [int(i) for i in str(n2)]
    for j in t1:
        for i in t2:
            try:
                if j < max(t2):
                    t1[t1.index(j)] = max(t2)
                    del t2[t2.index(max(t2))]
            except:
                pass
​
    return int(''.join([str(i) for i in t1]))

