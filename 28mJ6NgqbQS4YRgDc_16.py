
from collections import Counter
def can_pay_cost(mana_pool, cost):
    mana_pool_cnt = Counter(mana_pool)
    cnt = 0
    for i in range(len(cost)):
        if cost[i].isdigit():
            cnt += 1
    if cnt > 0:
       mana_cost_number = int(cost[:cnt])
       cost = cost[cnt:]
    else:
        mana_cost_number = 0
    cost_cnt = Counter(cost)
    if sum(cost_cnt[key] for key in cost_cnt) + mana_cost_number > sum(mana_pool_cnt[key] for key in mana_pool_cnt):
        return False
    for key in cost_cnt:
       if key not in mana_pool_cnt:
           return False
       elif key in mana_pool_cnt and cost_cnt[key] > mana_pool_cnt[key]:
                return False
    return True

