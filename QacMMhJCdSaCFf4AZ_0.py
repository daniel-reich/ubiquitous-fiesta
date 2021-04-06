
def sequence_generator(seq):
    d1, d2 = seq[1] - seq[0], seq[2] - seq[1]
    if d1 == d2:
        # arithmetic
        a = d1
        c = seq[0] - a
        return lambda n: a * n + c 
    # geometric
    a = d2 // d1
    c = seq[0] // a
    return lambda n: c * a**n

