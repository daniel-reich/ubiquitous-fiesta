
def is_early_bird(_range, n):
    s = ''.join(['*' + str(x) if x == n else str(x)
                 for x in range(_range+1)])
    natural_idx = s.find('*')
    s = s.replace('*', '')
    
    loi = []
    start = 0    
    while True:
        i = s.find(str(n), start)
        if i == -1:
            break
        start = i + 1
        loi.append([x for x in range(i, i+len(str(n)))])
    if loi[0][0] < natural_idx:
        loi.append("Early Bird!")
    return loi

