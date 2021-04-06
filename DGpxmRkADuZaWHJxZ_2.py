
def maurice_wins(m, s):
  mw = 0
  if m[0] > s[2]: mw += 1
  if m[1] > s[0]: mw += 1
  if m[2] > s[1]: mw += 1
  return mw >= 2

