
def can_pay_cost(mana_pool, cost):
  m = list(mana_pool)
  c = ''
  for i in cost:
    if i.isalpha():
      if i in m:
        m.remove(i)
      else:
        return False
    else:
      c += i
  if c == '':
    count = 0
  else:
    count = int(c)
  if len(m) >= count:
    return True
  else:
    return False

