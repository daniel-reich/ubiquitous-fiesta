
def concatenation_sum(n):
    d = len(str(n))
    return sum([9*10**(i-1)*i for i in range(1,d)])+(n-10**(d-1)+1)*d

