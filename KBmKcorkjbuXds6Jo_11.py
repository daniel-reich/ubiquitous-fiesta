
def chocolates_parcel(n_small, n_big, order):
    mb = order // 5
    if n_big < mb:
        mb = n_big
    
    for i in range(mb,-1,-1):        
        if (order - (i * 5)) % 2 == 0:
            if (order - (i * 5)) // 2 <= n_small:
                return (order - (i * 5)) // 2
    return -1

