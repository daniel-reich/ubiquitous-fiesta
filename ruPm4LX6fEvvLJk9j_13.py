
def esthetic(num):
    s = []
    for i in range(2, 11):
        b = str(base(num, i))
        if all([abs(int(b[i]) - int(b[i + 1])) == 1 for i in range(len(b) - 1)]):
            s.append(i)
    if not s:
        s = "Anti-Esthetic"
    return s 
    
def base(x, n):
    if n == 10:
        return x
    r = ""
    while x > 0: 
        x, b = divmod(x, n)
        r = str(b) + r
    return r

