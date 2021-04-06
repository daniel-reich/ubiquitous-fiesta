
from collections import Counter
​
def can_pay_cost(mana_pool, cost):
    n = "0"
    while len(cost) > 0 and '0' <= cost[0] <= '9':
        n += cost[0]
        cost = cost[1:]
    C_mana = Counter(mana_pool)
    C_cost = Counter(cost)
    for mtype in "WUBRGC":
        if C_cost.get(mtype, 0) > C_mana.get(mtype, 0):
            return False
        if mtype in C_mana:
            C_mana[mtype] -= C_cost.get(mtype, 0)
    return sum(C_mana.values()) >= int(n)

