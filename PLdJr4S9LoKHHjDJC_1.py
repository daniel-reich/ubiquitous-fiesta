
def identify(*c):
  l=[len(x)for x in c]
  return('Non-Full','Full')[len(l)==l[0]]if len(set(l))<2else'Missing %s'%(abs(len(l)**2-sum(l)))

