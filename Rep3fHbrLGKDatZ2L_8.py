
def complete_pattern(s):
  n = len(s)
  for i in range(1,n):
    pieces = {s[a:a+i] for a in range(0, n - n%i, i)}
    om_lst = [p for p in pieces if '_' in p]
    oth_lst = [p for p in pieces if '_' not in p]
    if len(oth_lst) == 1:
      oth = oth_lst[0]
      if len(om_lst)==1:
        om = om_lst[0]
        idx = om.index('_')
        if om[:idx] == oth[:idx] and om[idx+1:] == oth[idx+1:]:
          return oth[idx]
      elif len(om_lst)==0:
        idx = s[n-n%i:].index('_')
        return s[idx]

