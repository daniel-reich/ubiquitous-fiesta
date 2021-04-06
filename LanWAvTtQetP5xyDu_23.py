
def coins_div(lst):
  blank=[[],[],[]]
  if sum(lst)%3!=0: return False
  amount = int(sum(lst) / 3)
  if not(all([amount>=i for i in lst])): return False
  def calu(lst,rem,val):
      if len(blank[val])==1: lst.remove(max(lst))
      if sum(blank[val]) == amount:
          return blank
      else:
       if rem in lst:
          blank[val].append(rem)
          lst.remove(rem)
       else:
          blank[val].append(max(lst))
          rem1=amount-sum(blank[val])
          if (sum(blank[val])>amount) or all([i>rem1 for i in lst]):
              blank[val].pop()
              blank[val].append(min(lst))
              rem1 = amount - sum(blank[val])
              if (sum(blank[val]) > amount) or all([i > rem1 for i in lst]):return False
              lst.remove(min(lst))
          else: lst.remove(max(lst))
          calu(lst,rem1,x)
​
  for x in range(3):
   blank[x].append(max(lst))
   diff = amount - max(lst)
   (calu(lst, diff,x))
  return all([sum(i)==amount for i in blank])

