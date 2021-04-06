
def alpha_range(start, stop, step=1):
  L=[chr(x) for x in range(ord('a'), ord('z')+1)]
  U=[x.upper() for x in L]
  if start.islower()*stop.islower():
    m=min(L.index(start), L.index(stop))
    M=max(L.index(start), L.index(stop))
    if step!=0 and -26<step<26:
      if step<0:
        if m==0:
          return L[M::step]
        else:
          return L[M:m-1:step]
      elif step>0:
        return L[m:M+1:step]
    else:
      return "step must be a non-zero value between -26 and 26, exclusive"
  elif start.isupper()*stop.isupper():
    m=min(U.index(start), U.index(stop))
    M=max(U.index(start), U.index(stop))
    if step!=0 and -26<step<26:
      if step<0:
        if m==0:
          return U[M::step]
        else:
          return U[M:m-1:step]
      elif step>0:
        return U[m:M+1:step]
    else:
      return "step must be a non-zero value between -26 and 26, exclusive"
  else:
    return "both start and stop must share the same case"

