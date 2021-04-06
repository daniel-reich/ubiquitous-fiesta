
import re
def can_pay_cost(mana_pool, cost):
  if mana_pool == '': return cost == '0'
  d = re.match(r'\d+', cost)
  n, m = (int(d.group(0)), cost[len(d.group(0)):]) if d else (0, cost)
  for t in m: 
    if t in mana_pool:
      mana_pool = mana_pool.replace(t, '', 1)
    else:
      return False
  return len(mana_pool) >= n

