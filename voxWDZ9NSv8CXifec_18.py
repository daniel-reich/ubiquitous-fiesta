
def lemonade(bills):
    d = {b:bills.count(b) for b in [5, 10, 20]}
    
    if not d[5] >= 1:
        return False
    
    for b in bills:
        if b == 10:
            if not d[5] >= 1:
                return False
            d[5] -= 1
            
        elif b == 20:
            if d[5] >= 1 and d[10] >= 1:
                d[5] -= 1
                d[10] -= 1
            elif d[5] >= 3:
                d[5] -= 3
            else:
                return False
    return True

