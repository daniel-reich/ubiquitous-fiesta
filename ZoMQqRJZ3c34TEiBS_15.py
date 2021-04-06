
def playfair(txt, keyword):
  a = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
  temp = ''
  for i in keyword:
    if i not in temp:
      temp += i
  keyword = temp
  txt,keyword = txt.upper(), keyword.upper()
  txt = ''.join([i for i in txt if i in a or i == ' '])
  for i in a:
    if i not in keyword:
      keyword += i
  it = 0  
  lst = [''] * 5
  for i in range(len(lst)):
    lst[i] = [''] * 5
  for i in range(len(lst)):
    for x in range(5):
      lst[i][x] = keyword[it]
      it += 1
  columns = []
  for i in range(len(lst[0])):
    columns.append(''.join([a[i] for a in lst]))
  rows = [''.join(i) for i in lst]
  if ' ' in txt:
    txt = txt.replace(' ','')
    pairs = [txt[i:i+2] for i in range(0,len(txt),2)]
    while not all([len(set(i)) != 1 for i in pairs]):
      pairs = ''.join(pairs)
      indexes = []
      check = False
      for i in range(1,len(pairs)):
        if pairs[i] == pairs[i-1] and i%2 == 1:
          indexes.append(i)
          check = True
      if check:
        pairs = pairs[:indexes[0]]+'X'+pairs[indexes[0]:]
      else:
        pairs += 'X'
      pairs = [pairs[i:i+2] for i in range(0,len(pairs),2)]
    for i in range(len(pairs)):
      a,b = pairs[i][0],pairs[i][1]
      check = False
      for x in range(5):
        if a in rows[x] and b in rows[x]:
          pairs[i] = rowfix(a,b,rows[x],'encode')
          check = True
        elif a in columns[x] and b in columns[x]:
          pairs[i] = colfix(a,b,columns[x],'encode')
          check = True
        if not check:
          pairs[i] = squarefix(a,b,lst)
  else:
    pairs = [txt[i:i+2] for i in range(0,len(txt),2)]
    for i in range(len(pairs)):
      a,b = pairs[i][0],pairs[i][1]
      check = False
      for x in range(5):
        if a in rows[x] and b in rows[x]:
          pairs[i] = rowfix(a,b,rows[x],'decode')
          check = True
        elif a in columns[x] and b in columns[x]:
          pairs[i] = colfix(a,b,columns[x],'decode')
          check = True
        if not check:
          pairs[i] = squarefix(a,b,lst)
  return ''.join(pairs)
  
def rowfix(a,b,row,instruction):
  if instruction == 'encode':
    if row.index(a) == 4:
      a = row[0]
    else:
      a = row[row.index(a)+1]
    if row.index(b) == 4:
      b = row[0]
    else:
      b = row[row.index(b)+1]
  elif instruction == 'decode':
    if row.index(a) == 0:
      a = row[4]
    else:
      a = row[row.index(a)-1]
    if row.index(b) == 0:
      b = row[4]
    else:
      b = row[row.index(b)-1]
  return a+b
      
def colfix(a,b,col,instruction):
  if instruction == 'encode':
    if col.index(a) == 4:
      a = col[0]
    else:
      a = col[col.index(a)+1]
    if col.index(b) == 4:
      b = col[0]
    else:
      b = col[col.index(b)+1]
  elif instruction == 'decode':
    if col.index(a) == 0:
      a = col[4]
    else:
      a = col[col.index(a)-1]
    if col.index(b) == 0:
      b = col[4]
    else:
      b = col[col.index(b)-1]
  return a+b
      
def squarefix(a,b,lst):
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      if lst[i][x] == a:
        aind = [i,x]
      if lst[i][x] == b:
        bind = [i,x]
  a = lst[aind[0]][bind[1]]
  b = lst[bind[0]][aind[1]]
  return a+b

