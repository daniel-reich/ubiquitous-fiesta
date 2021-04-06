
def is_checkerboard(lst):
  def one_zero_check(item):
    length = len(item)
    even = []
    odd = []
    for n in range(0, length):
      i = item[n]
      r = n % 2
      if r == 0:
        even.append(i)
      else:
        odd.append(i)
    
    evensame = None
    oddsame = None
​
    elen = len(even)
    olen = len(odd)
​
    ec = even.count(even[0])
    oc = odd.count(odd[0])
​
    if ec == elen:
      evensame = True
    else:
      evensame = False
      return evensame
    
    if oc == olen:
      oddsame = True
    else:
      oddsame = False
      return oddsame
    
    if evensame == True and oddsame == True:
      diff = None
      if even[0] != odd[0]:
        diff = True
        ni = item[0]
        return [diff, ni]
      else:
        diff = False
        return diff
  
  rows = []
  
  for item in lst:
    t = one_zero_check(item)
    if t == False:
      return False
    else:
      rows.append(t[1])
  
  nt = one_zero_check(rows)
  
  try:
    return nt[0]
  except TypeError:
    return nt

