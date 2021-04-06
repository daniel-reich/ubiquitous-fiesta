
def can_pay_cost(mana_pool, cost):
  import re
  mana_pool = list(mana_pool)
  extra_needed = "0" + "".join(re.split("\D",cost))
  for i in cost:
    if i in "WGUBRC":
      if i not in mana_pool:
        return False
      else:
        mana_pool.remove(i)
  return int(extra_needed) <= len(mana_pool)

