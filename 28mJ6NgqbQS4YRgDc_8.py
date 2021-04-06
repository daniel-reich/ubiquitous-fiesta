
def can_pay_cost(mana_pool, cost):
    mana_pool = list(mana_pool)
    num = "".join([x for x in  cost if x.isnumeric()])
    cost = cost[len(num) :]
    for i in cost:
        if i in mana_pool:
            mana_pool.remove(i)
        else:
            return False
    if num:
        return len(mana_pool) >= int(num)
    else:
        return True

