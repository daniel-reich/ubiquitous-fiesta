
import re
def can_pay_cost(mana_pool, cost):
    dict_pool = dict()
    for c in set(mana_pool):
        dict_pool[c] = mana_pool.count(c)
    pool_digits = re.findall(r'\d+', cost)
    cost = re.sub(r'\d+', '', cost)
    any_pool_cost = int(pool_digits[0] if pool_digits else '0')
    dict_cost = dict()
    for c in set(cost):
        dict_cost[c] = cost.count(c)
​
    for c in dict_cost:
        if c in dict_pool and dict_cost[c] <= dict_pool[c]:
            dict_pool[c] -= dict_cost[c]
        else:
            return False
​
    remaining_mana = 0
    for c in dict_pool:
        remaining_mana += dict_pool[c]
    return any_pool_cost <= remaining_mana

