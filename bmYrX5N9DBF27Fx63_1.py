
def greatest_impact(l):
  n=['Weather','Meals','Sleep',10,3,10]
  r=[x/y for x,y in zip([sum(z)for z in zip(*l)][1:],n[3:])]
  return('Nothing',n[r.index(min(r))])[r!=[3]*3]

