
def ruth_aaron(n):
    r, s = 0, ""
    m = get_factors(n - 1)
    o = get_factors(n + 1)
    n = get_factors(n)
    if sum(set(n)) == sum(set(m)):
        r += 1
        s = "Aaron"
    if sum(n) == sum(m):
        r += 2
        s = "Aaron"
    if sum(set(n)) == sum(set(o)):    
        r += 1
        s = "Ruth"
    if sum(n) == sum(o):
        r += 2
        s = "Ruth"
    if s == "":
        return False
    return [s, r]
        
def get_factors(x):
    f = []
    i = 2
    while x > 1:
        if x % i == 0:
            f.append(i)
            x = x // i
            i = 2
        else:
            i += 1
    return f

