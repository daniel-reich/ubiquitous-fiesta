
def can_pay_cost(mana_pool, cost):
    mana_pool = list(mana_pool)
    cost = list(cost)
    while any(ch.isalpha() for ch in cost):
        req = cost.pop()
        try:
            mana_pool.remove(req)
        except:
            return False
    return not cost or len(mana_pool) >= int(''.join(cost))

