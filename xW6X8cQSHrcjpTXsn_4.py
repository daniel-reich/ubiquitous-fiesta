
def first_and_last(s):
    
    first_permutation = sorted(s)
    last_permutation = first_permutation[::-1]
​
    return [''.join(first_permutation), ''.join(last_permutation)]

