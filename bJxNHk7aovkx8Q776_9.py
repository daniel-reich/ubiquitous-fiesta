
def gold_distribution(gold):
  def choose(lst):
    if lst[-1] > lst[0]:
      return [lst[-1], lst[:-1]]
    else:
      return [lst[0], lst[1:]]
  
  muba = []
  matt = []
  mu = True
  
  while len(gold) > 0:
    c = choose(gold)
    if mu == True:
      muba.append(c[0])
      mu = False
    else:
      matt.append(c[0])
      mu = True
    gold = c[1]
  
  return [sum(muba), sum(matt)]

