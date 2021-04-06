
def diag_dom(lst):
    D = [] #Diagonals    
    for i in range(len(lst)):
        D.append(abs(lst[i][i]))
        
    # list of sums before subtracing diagonal number    
    S = list(sum(abs(u) for u in i) for i in lst)
    
    # adds 1 to list if:
    # diagonal > (sum(row)) - diagonal
    return all(1 if d > (s-d) else 0 for d,s in zip(D,S))

