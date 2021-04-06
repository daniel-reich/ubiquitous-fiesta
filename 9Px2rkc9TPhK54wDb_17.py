
def ecg_seq_index(n):
    '''
    Returns the index (numbered from 0) of n in the ECG Sequence as
    described above.
    '''
    def gcd(a, b):
        '''
        Helper to has_factors - returns the gcd of a and b
        '''
        if b == 0:
            return a
        a = a % b
        return gcd(b, a)
​
    def has_factors(a, b):
        '''
        Returns True if a and b have common factors
        '''
        return a * b // gcd(a, b) != a * b
        
    seq = [1,2]
    unused = [i for i in range(3, n ** 2 + 1)]
    index = 1
    
    while seq[-1] != n:
        for num in unused:
            if has_factors(seq[-1], num):
                seq.append(num)
                unused.remove(num)
                index += 1
                break
​
    return index

