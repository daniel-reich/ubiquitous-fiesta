
def both(n1, n2):
    return all([i<0 for i in [n1,n2] ]) or all([i>0 for i in [n1,n2]]) or all([i==0 for i in [n1,n2]])

