
def digital_division(n):
    a = 1
    s = list(map(int,str(n)))
    
    for item in s:
        if item != 0:
            if n % item != 0:
                a -= 1
                break
    
    if n % sum(s) == 0:
        a += 1
    
    m = 1
    for item in s:
        m *= item
    
    if m != 0:
        if n % m == 0:
            a += 1
    
    if a == 3:
        return 'Perfect'
    if a == 1 or a == 2:
        return a
    return 'Indivisible'

