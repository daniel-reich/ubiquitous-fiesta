
def is_early_bird(r, n):
  r = ''.join(str(i) for i in range(r+1)); n = str(n); ln = len(n)
  res = [list(range(i,i+ln)) for i in range(len(r)-ln+1) if r[i:i+ln]==n]
  if len(res) > 1:
    res.append('Early Bird!')
  return res

