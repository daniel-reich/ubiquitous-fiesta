
def num_type(n):
    f = sum(factors(n))
    if f == n:
        return "Perfect"
    elif sum(factors(f)) == n:
        return "Amicable"
    else:
        return "Neither"
    
def factors(x):
    return [i for i in range(1, x) if x % i == 0]

