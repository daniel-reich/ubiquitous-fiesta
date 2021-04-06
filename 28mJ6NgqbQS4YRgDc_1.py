
def can_pay_cost(mana_pool, cost):
  if not any([i.isdigit() for i in cost]):
    return all([mana_pool.count(i)>=cost.count(i) for i in cost])
  ca,cs = int(''.join([i for i in cost if i.isdigit()])),[i for i in cost if i.isalpha()]
  for i in cs:
    if i in mana_pool:
      mana_pool = mana_pool[:mana_pool.index(i)]+mana_pool[mana_pool.index(i)+1:]
    else:
      return False
  return len(mana_pool)>=ca

