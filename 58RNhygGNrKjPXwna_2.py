
def longest_nonrepeating_substring(s):
  s1="";m=0;i=0
  while(i<len(s)):
    if s[i] not in s1:
      s1=s1+s[i]
      i=i+1
    else:
      if len(s1)>m:
        m=len(s1)
        s2=s1
      s1=""
      i=s.index(s[i])+1
      s="*"*len(s[0:i])+s[i:]
  if len(s1)>m:
    return(s1)
  else:
    return(s2)

