
def two_product(lst, n):
    res = []
    for i in lst:
        if i != 0 and not n%i: 
            if n/i in lst: res.append(i); res.append(int(n/i)); break
    return sorted(res) if res else None

