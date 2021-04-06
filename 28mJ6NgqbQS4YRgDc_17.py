
def can_pay_cost(mana_pool, cost):
  
  
  d = {'B':0,'W':0,'R':0,'G':0,'U':0,'C':0}
  e = {'B':0,'W':0,'R':0,'G':0,'U':0,'C':0}
  total = 0
  for i in range(0,len(mana_pool)):
    d[mana_pool[i]]+=1
      
  variable = 0
  i = 0
  while i<len(cost):
    if ord(cost[i])>57:
      e[cost[i]]+=1
      i+=1
    else:
      tmp = ""
      j = i
      val=-1
      while j<len(cost):
        if ord(cost[j])>57:
          val = j
          break
        else:
          tmp+=cost[j]
          j+=1
      variable+=int(tmp)
      if val>0:
        i = val
      else:
        break
      
  
  for x in e:
    if d[x]<e[x]:return False
    d[x]-=e[x]
    total+=d[x]
  return total>=variable

