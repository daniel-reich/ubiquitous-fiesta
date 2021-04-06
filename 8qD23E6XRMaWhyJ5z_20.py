
def happiness_number(s):
  k=sum([1 for i in range(len(s)-1) if (s[i],s[i+1])==(':',')')or(s[i],s[i+1])==('(',':')])
  l=sum([1 for i in range(len(s)-1) if (s[i],s[i+1])==(':','(')or(s[i],s[i+1])==(')',':')])
  return k-l

