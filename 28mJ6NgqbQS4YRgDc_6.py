
from collections import Counter
def can_pay_cost(mana_pool, cost):
    digits, manas = ''.join([x for x in cost if x.isdigit()]), [x for x in cost if x.isalpha()]
    a, b  = Counter(''.join(manas)), Counter(mana_pool)
    if manas:
        for x, y in a.items():
            if b[x] >= y:
                b[x] -= y
            else: return False
    
    if digits:
        return True if sum(b.values()) >= int(digits) else False
​
    return True

