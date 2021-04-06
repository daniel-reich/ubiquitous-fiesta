
def ruth_aaron(n):
    factors_n = factors(n)
    factors_plus = factors(n+1)
    factors_minus = factors(n-1)
    discretefactors_n = discretefactors(factors_n)
    discretefactors_plus = discretefactors(factors_plus)
    discretefactors_minus = discretefactors(factors_minus)
    sum_n = sum(factors_n)
    sum_plus = sum(factors_plus)
    sum_minus = sum(factors_minus)
    discretesum_n = sum(discretefactors_n)
    discretesum_plus = sum(discretefactors_plus)
    discretesum_minus = sum(discretefactors_minus)
    total = 0
    if sum_n == sum_plus:
        if discretesum_n == discretesum_plus:
            return(["Ruth",3])
        else:
            return(["Ruth",2])
    if discretesum_n == discretesum_plus:
            return(["Ruth",1])
    
    if sum_n == sum_minus:
        if discretesum_n == discretesum_minus:
            return(["Aaron",3])
        else:
            return(["Aaron",2])
    if discretesum_n == discretesum_minus:
            return(["Aaron",1])
    return False
​
def factors(n):
    factors = []
    while n%2 == 0:
        factors.append(2)
        n = n/2
    for i in range(3,int(n**.5)+1,2):
        while n % i == 0:
            factors.append(int(i))
            n = n/i
    if n > 2:
        factors.append(int(n))
    return factors
​
def discretefactors(factors):
    discretefactors = []
    for i in factors:
        if i not in discretefactors:
            discretefactors.append(i)
    return discretefactors

