
def is_ladder_safe(ldr):
  return span(ldr) and all([wide(i) for i in ldr]) and all([not_broken(i) for i in ldr])
  
def wide(s):
  return len(s)>=5
  
def not_broken(s):
  return all([i=='#' for i in s]) or (s[0]=='#' and s[-1]=='#' and all([i==' ' for i in s[1:-1]]))
  
def span(lst):
  rungs = [i for i in range(len(lst)) if all([x=='#' for x in lst[i]])]
  return len(rungs) >= 1 and (all([rungs[i+1]-rungs[i]==1 for i in range(len(rungs)-1)]) or all([rungs[i+1]-rungs[i]==2 for i in range(len(rungs)-1)]) or all([rungs[i+1]-rungs[i]==3 for i in range(len(rungs)-1)]))

