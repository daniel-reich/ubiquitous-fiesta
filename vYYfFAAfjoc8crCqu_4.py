
def tree(h):
  def hashes(h):
    rows = []
    current_num = 1
    for n in range(1, h+1):
      row = ''
      for num in range(current_num):
        row += '#'
      rows.append(row)
      current_num += 2
    return rows
  def spaces(hashes):
    
    target = len(hashes[-1])
    print(target)
    new_rows = []
    
    for row in hashes:
      dif = target - len(row)
      half = ''
      if dif != 0:
        for n in range(int(int(dif)/2)):
          half += ' '
      row = half + row + half
      new_rows.append(row)
    
    return new_rows
  if h == 0:
    return []
  rows = hashes(h)
  tree = spaces(rows)
  return tree

