
def most_overlapped_block(nbr,ranges):
    max = 0
    for j in range(1,nbr + 1):
        for k in range(1,nbr+1):
            onepoint = 0
            for (x,y,r) in ranges:
                if abs(x - j) + abs(y-k) <= r:
                    onepoint += 1 
            if onepoint > max:
                max = onepoint
    return max

