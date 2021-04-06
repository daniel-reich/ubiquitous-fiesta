
def smith_type(number):
    
    def fac(n):
        import math
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = int(math.sqrt(n)) + 1
        d = 1
        q = 2 if n % 2 == 0 else 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return [q] + fac(n // q) if q <= maxq else [n] if n > 1 else []
    
    def dsum(n):
        while n > 9:
            n = sum(map(int, list(str(n))))
        return n
    
    lw = fac(number)
    df = dsum(sum(lw))
    # digital sum n
    ds = dsum(number)
    if ds != df:
        return "Not a Smith"
    # Youngest Smith
    lyw = fac(number + 1)
    dyf = dsum(sum(lyw))
    dys = dsum(number + 1)
    if dyf == dys and len(lyw) > 1:
        return "Youngest Smith"
    # Oldest Smith
    low = fac(number - 1)
    dof = dsum(sum(low))
    dos = dsum(number - 1)
    while dys > 9:
        dys = sum(map(int, list(str(ds))))
    if dof == dos and len(low) > 1:
        return "Oldest Smith"
    # simple smith
    if len(lw) == 1:
        return "Trivial Smith"
    if df == ds:
        return "Single Smith"
def smith_type(number):
    
    def fac(n):
        import math
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = int(math.sqrt(n)) + 1
        d = 1
        q = 2 if n % 2 == 0 else 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return [q] + fac(n // q) if q <= maxq else [n] if n > 1 else []
    
    def dsum(n):
        while n > 9:
            n = sum(map(int, list(str(n))))
        return n
    
    lw = fac(number)
    df = dsum(sum(lw))
    # digital sum n
    ds = dsum(number)
    if ds != df:
        return "Not a Smith"
    # simple smith
    if len(lw) == 1:
        return "Trivial Smith"
    # Oldest Smith
    low = fac(number - 1)
    dof = dsum(sum(low))
    dos = dsum(number - 1)
    if dof == dos and len(low) > 1:
        return "Oldest Smith"
    # Youngest Smith
    lyw = fac(number + 1)
    dyf = dsum(sum(lyw))
    dys = dsum(number + 1)
    if dyf == dys and len(lyw) > 1:
        return "Youngest Smith"
    if df == ds:
        return "Single Smith"

