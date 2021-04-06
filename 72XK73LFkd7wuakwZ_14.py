
def junction_or_self(n):
    '''
    Returns a list of numbers in descending order which sum with their digits
    to n, or 'Self' if this does not apply to n
    '''
    junctions = [i for i in range(n-1,0,-1) if i + sum(int(d) for d in str(i))==n]
​
    return junctions if junctions else 'Self'

