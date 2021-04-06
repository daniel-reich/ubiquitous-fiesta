
def spiral_transposition(lst):
  rows, cols =  (-1,len(lst)), (-1,len(lst[0]))
  r, c = 0, 0
  track, res = set(), []
  direct = 1
​
  while len(res) < rows[1]*cols[1]:
    rn, cn = r, c
    if (r, c) not in track:
      res.append(lst[r][c])
      track.add((r,c))
​
    if direct == 1: cn += 1
    elif direct == 2: rn += 1
    elif direct == 3: cn -= 1
    else: rn -= 1
​
    if rn in rows or cn in cols or (rn, cn) in track:
      direct = direct+1 if direct < 4 else 1
    else:
      r, c = rn, cn
  return res

