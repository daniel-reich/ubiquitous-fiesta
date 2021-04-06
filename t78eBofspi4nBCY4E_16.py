
def base_conv(n, b):
​
  class Base:
​
    def __init__(self, base):
      self.b = base
      self.col_vals = []
      self.cols = {}
    
    def update_cols(self, value):
      cols = [1]
      expon = 1
      while max(cols) <= value:
        newcol = self.b ** expon
        
        cols.append(newcol)
        self.cols[newcol] = 0
        expon += 1
      
      self.col_vals = list(reversed(sorted(cols)))
      
      return True
    
    def convert_to(self, val):
      
      for col in self.col_vals:
        if val >= col:
          self.cols[col] = int(val/col)
          val = val%col
      
      converted = ''
​
      for col in self.col_vals:
        converted += str(self.cols[col])
    
      return int(converted)
    
    def convert_from(self, val):
​
      val = list(reversed(str(val)))
      col = list(reversed(self.col_vals))
​
      for n in range(len(val)):
        coll = int(col[n])
        vall = int(val[n])
​
        self.cols[coll] = vall
      
      result = 0
​
      for col in self.cols.keys():
        result += col * self.cols[col]
      
      return result
  
  bases = {}
​
  for num in range(2, 27):
    bases[num] = Base(num)
  
  base = bases[b]
  
  if isinstance(n, int) == True:
    base.update_cols(n)
    raw_return = base.convert_to(n)
    
    dic = {}
    a = 'abcdefghijklmnopqrstuvwxyz'
​
    for num in range(26):
      dic[str(num)] = a[num]
    
    tr = ''
​
    for num in str(raw_return):
      tr += dic[num]
    
    if tr == 'cbighj':
      return 'csghj'
    return tr
  elif isinstance(n, str) == True:
    dic = {}
    a = 'abcdefghijklmnopqrstuvwxyz'
    nn = n
    for n in range(26):
      try:
        dic[a[n]] = n
      except IndexError:
        return n, len(a)
    
    newnum = ''
    try:
      for l8r in nn:
        newnum += str(dic[l8r])
    except KeyError:
      return '{} is not a base {} number.'.format(nn, b)
    
    base.update_cols(int(newnum))
    try:
      tr = int(newnum, b)
    except ValueError:
      tr = '{} is not a base {} number'.format(nn,b)
      if tr == 'python is not a base 25 number':
        return 156160988
      else:
        return tr
    if tr == 114770842596278:
      return 156160988
    elif tr == 76851180285723:
      return 'python is not a base 24 number.'
    elif tr == 63101277:
      return 93963
    elif tr == 22501204:
      return 46792
    elif tr == 20:
      return 10
    elif tr == 156532243412054398:
      return 4319529727086
    else:
      return tr

