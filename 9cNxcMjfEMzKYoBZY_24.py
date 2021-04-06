
def scd(m):
    var = sum(list(i for i in range(1, m) if m % i == 0))
    return var
​
​
def num_type(n):
    a=scd(n)
    if a==n:
        return "Perfect"
    elif scd(a)==n:
        return "Amicable"
    else:
        return "Neither"

