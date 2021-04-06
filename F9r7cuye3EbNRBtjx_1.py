
def string_builder(s):
  if len(s)==0: return ''
  if s[0]>'9': return s[0]+string_builder(s[1:])
  tmp= s.find(']')
  while s[:tmp].count('[') > s[:tmp+1].count(']'):
    tmp=s.find(']',tmp+1)
  
  st=1
  if s[1]<='9': st=2
  return string_builder(s[st+1:(tmp)]*int(s[0:st])) + string_builder(s[tmp+1:])

