
def shadow_sentence(a,b):
    '''
    Returns whether sentence a has same number and length of each word as b, and
    also has no letters in common between corresponding words.
    '''
    a, b = a.split(), b.split()
    
    return len(a) == len(b) and all(len(w1)==len(w2) \
            and all(l not in set(w2) for l in set(w1)) for w1,w2 in zip(a,b))

