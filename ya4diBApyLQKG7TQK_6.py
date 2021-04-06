
def validate_relationships(txt):
  s, v, t = [], 1, txt[0]
  if t in '0123456789-':
    v = 0
  for i in txt[1:]:
    if i in '0123456789-' and v == 0:
      t += i
    elif i in '0123456789-' and v == 1:
      s.append(t)
      t, v = i, 0
    elif i not in '0123456789-' and v == 0:
      s.append(t)
      t, v = i, 1
    else:
      t += i
  s.append(t)
  for g in range(0, len(s) - 2, 2):
    k1 = int(s[g])
    k2 = int(s[g + 2])
    if s[g + 1] == '>':
      if k1 <= k2:
        return False
    elif s[g + 1] == '>=':
      if k1 < k2:
        return False
    elif s[g + 1] == '=':
      if k1 != k2:
        return False
    elif s[g + 1] == '<=':
      if k1 > k2:
        return False
    else:
      if k1 >= k2:
        return False
  return True

