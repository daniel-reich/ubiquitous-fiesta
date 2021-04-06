
def non_repeats(radix):
    s=1
    k=1
    for i in range(radix-1,0,-1):
        k*=i
        s+=k
    return (radix-1)*s

