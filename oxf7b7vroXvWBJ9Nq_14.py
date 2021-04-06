
def discount(n, txt):
  def find_possible_discounts(txt):
    discounts = txt.split(', ')
    from itertools import permutations as p
​
    alldiscounts = p(discounts, len(discounts))
​
    return list(alldiscounts)
  def apply_discount(n, discounts):
    def discount(n, dcount):
      if '%' in dcount:
        r = float(dcount[:-1])/ 100
        return n - (n * r)
      else:
        return n - float(dcount)
​
    for item in discounts:
      n = discount(n, item)
    
    return n
      
  if txt == '':
    return n
​
  alldiscounts = find_possible_discounts(txt)
  discounts = []
​
  for sale in alldiscounts:
    discounts.append(abs(apply_discount(n, sale)))
  
  return round(min(discounts),2)

