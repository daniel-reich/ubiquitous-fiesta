
def is_consecutive(s,t=None,step=1):
  # recursive code in here
  if t==None:
    for i in range(1,len(s)//2+1):
      if len(s)%i==0:
        if is_consecutive(s[i:],(s[:i]),1): return True
        if is_consecutive(s[i:],(s[:i]),-1): return True
    return False
  #if int(s[:len(t)])*step<=int(t)*step: return False # Ascending/Descending by any value
  if int(s[:len(t)])!=int(t)+step: return False # stepwise
  if len(s)>len(t): return is_consecutive(s[len(t):], s[:len(t)], step  )
  return True

