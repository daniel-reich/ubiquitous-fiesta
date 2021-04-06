
def can_pay_cost(mana_pool, cost):
  def fixed_unfixed_sep(cost):
    unfixed = ''
    fixed = ''
​
    for n in range(len(cost)):
      try:
        unfixed += str(int(cost[n]))
      except ValueError:
        fixed += cost[n]
    
    try:
      return [int(unfixed), fixed]
    except ValueError:
      return [0, fixed]
  def remove_fixed(mana, fixed):
    tr = ''
    for l8r in set(mana):
      mc = mana.count(l8r)
      fc = fixed.count(l8r)
      print(mc, fc, l8r)
      if mc < fc:
        return False
      else:
        d = mc - fc
        for n in range(d):
          tr += l8r
    poss = True
    for l8r in set(fixed):
      if l8r not in mana:
        poss = False
        break
    if poss == False:
      return False
    return tr
​
  fus = fixed_unfixed_sep(cost)
  rf = remove_fixed(mana_pool, fus[1])
  
  try:
    return len(rf) >= fus[0]
  except TypeError:
    return False

