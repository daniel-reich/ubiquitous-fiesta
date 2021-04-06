
def square_root(n): 
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  
        if newr >= r:
            return r
        r = newr

