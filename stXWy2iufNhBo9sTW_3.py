
def valid_rondo(s):
  return s[0]=='A' and s[-1]=='A' and len(s)>2 and all([s[i-1]!=s[i] and s[i+1]!=s[i] for i in range(1,len(s)-1)])

