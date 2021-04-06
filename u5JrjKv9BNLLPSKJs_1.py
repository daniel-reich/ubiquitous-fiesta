
def num_ways(n, s):
    d1 = {}
    def helper(n, s):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in d1:
            d1[n] = sum([helper(n-i,s) for i in s])
        
        return d1[n]
    
    return helper(n,s)

