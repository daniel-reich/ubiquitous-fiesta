
def valid_rondo(s):
  return 1<len(s)==2*len(set(s))-1 and all(s[i]==s[0] for i in range(0,len(s),2))

