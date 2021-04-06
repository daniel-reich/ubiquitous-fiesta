
def tap_code(text):
  txt = text
  def l8rs_to_taps(l8rs):
​
    l8r_block = [['A', 'B', 'C', 'D', 'E'], 'F G H I J'.split(), 'L M N O P'.split(), 'Q R S T U'.split(), 'V W X Y Z'.split()]
​
    taps = []
​
    for l8r in l8rs:
      l8r = l8r.upper()
      if l8r == 'K':
        l8r = 'C'
      
      rownum = None
      colnum = None
​
      for n in range(0, len(l8r_block)):
        row = l8r_block[n]
        for num in range(0, 5):
          item = row[num]
          if item == l8r:
            rownum = n + 1
            colnum = num + 1
            break
      
      rowtap = ''
      coltap = ''
​
      for n in range(0, rownum):
        rowtap += '.'
      for n in range(0, colnum):
        coltap += '.'
      
      tap = rowtap + ' ' + coltap
​
      taps.append(tap)
    
    tr = ' '.join(taps)
​
    return tr
  def taps_to_l8rs(taps):
   
    taps = taps.split()
    
    idents = []
​
    for n in range(0, len(taps), 2):
      rowtapitem = taps[n]
      coltapitem = taps[n + 1]
​
      rownum = rowtapitem.count('.') - 1
      colnum = coltapitem.count('.') - 1 
​
      ident = '{r} {c}'.format(r = rownum, c = colnum)
​
      idents.append(ident)
    
    l8r_block = [['A', 'B', 'C', 'D', 'E'], 'F G H I J'.split(), 'L M N O P'.split(), 'Q R S T U'.split(), 'V W X Y Z'.split()]
​
    l8rs = []
​
    for ident in idents:
​
      i = ident.split()
      rowid = int(i[0])
      colid = int(i[1])
​
      l8r = l8r_block[rowid][colid]
​
      l8rs.append(l8r)
​
    return ''.join(l8rs).lower()
​
  tr = None
​
  if '.' in txt:
    tr = taps_to_l8rs(txt)
  else:
    tr = l8rs_to_taps(txt)
​
  return tr

