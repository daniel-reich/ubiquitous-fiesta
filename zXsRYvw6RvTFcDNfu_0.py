
def factors(num):
    for ii in range(2,int(num**0.5)+1):
        if num%ii==0:
                return [ii] + factors(int(num/ii))
    return [num]
 
def ruth_aaron(n):
    aaron = ruth = False
    all_factors = [factors(n-1), factors(n), factors(n+1)]
    sums = [(sum(factors), sum(set(factors))) for factors in all_factors]
    ruth = ['Ruth', (2 if sums[1][0]==sums[2][0] else 0) +\
                    (1 if sums[1][1]==sums[2][1] else 0)]
    aaron = ['Aaron', (2 if sums[0][0]==sums[1][0] else 0) +\
                      (1 if sums[0][1]==sums[1][1] else 0)]
    
    return ruth[1] and ruth or aaron[1] and aaron

