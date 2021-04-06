
def classify_rug(pattern):
  x = list(set(list("".join(list(set(i))) for i in pattern)))
  ans = ''
  for i in pattern:ans+="".join(i)
  if ans[::-1] == ans:return 'perfect'
  if len(x)==1 and len(x[0])==1:return 'perfect'
  while(len(pattern)>1 and pattern[0]==pattern[-1]):pattern = pattern[1:-1]
  if len(pattern)<2:return 'horizontally symmetric'
  return 'vertically symmetric' if len(list(set(ans.count(i) for i in ans)))==1 else "imperfect"

