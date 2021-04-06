
def get_lucky_number(size, nth):
    pool = list(range(1,size+1,2))
    i=1
    while i < len(pool):
        sieve = pool[i]
        pool = [pool[k] for k in range(len(pool)) if (k+1)%sieve!=0]
        i+=1
    return pool[nth-1]

