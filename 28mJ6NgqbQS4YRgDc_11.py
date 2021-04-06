
def can_pay_cost(mana_pool, cost):
  if cost.isdigit():
    return len(mana_pool) >= int(cost)
  if not cost.isalpha():
    for i,c in enumerate(cost):
      if not c.isdigit():
        if len(mana_pool) < int(cost[:i]) + len(cost)-i:
          return False
        break
  if any([mana_pool.count(c) < cost.count(c) for c in 'WUBRGC']):
    return False
  return True

