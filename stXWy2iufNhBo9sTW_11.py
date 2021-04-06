
def valid_rondo(s):
  flag=True
  for i in range(len(s)-2):
    if s[i]==s[i+1]:
      flag=False
  if s[0]!='A' or s[-1]!='A' or len(s)==1 or s[1:-1].count('B')>1 or s[1:-1].count('C')>1 or s[1:-1].count('D')>1:
      flag=False
  return flag

