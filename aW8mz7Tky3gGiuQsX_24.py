
def is_powerful(n):
    factors, num, i = [], n, 2
    while i<num//2:
        if num%i==0:
            factors.append(i)
            num//=i
        else:
            i+=1
    factors.append(num)
    return all(n%(f**2)==0 for f in list(set(factors)))

