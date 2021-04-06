
def quad_sequence(seq):
    '''
    Returns a list of the next n items of the quadratic sequence seq, where
    n is the length of n.
    '''
    # Uses the formula: ith item = Ai^2 + Bi + C where A, B and C are constants
    # and i is numbered from 1
    A = (seq[2] - seq[1] - seq[1] + seq[0])//2
    d1, d2 = seq[0] - A, seq[1] - 4 * A  # n1 - A(1^2), n2 - A(2^2)
    B, C = d2 - d1, 2 * d1 - d2
    
    return [A * i**2 + B * i + C for i in range(len(seq)+1, 2*len(seq)+1)]

