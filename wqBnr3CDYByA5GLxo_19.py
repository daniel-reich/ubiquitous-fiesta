
def unravel(txt):
  chunks, combos = [], []
  while txt:
    if txt[0]=='[':
      chunks.append(txt[1:txt.index(']')].split('|'))
      txt = txt[txt.index(']')+1:]
    else:
      chunks.append(txt[0])
      txt = txt[1:]
  x = separate(chunks)
  return sorted(''.join(x[i:len(chunks)+i]) for i in range(0, len(x), len(chunks)))
  
def separate(lst):
    sep = []
    for i in range(len(lst)):
        if type(lst[i])!=list:
            continue
        else:
            for j in range(len(lst[i])):
                sep.append(lst[:i]+[lst[i][j]]+lst[i+1:])
            break
    if sep:
        combos = []
        for i in sep:
            combos.extend(separate(i))
        return combos
    else:
        return lst

