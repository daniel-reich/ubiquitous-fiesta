
def josephus(n):
    pool = list(range(1,n+1))
    kr_idx = 0
    while len(pool)>1:
        kd_idx = (kr_idx+1)%len(pool)
        kr_idx = (kr_idx+1)%len(pool)%(len(pool)-1)
        pool = pool[:kd_idx] + pool[kd_idx+1:]
    return pool[0]

