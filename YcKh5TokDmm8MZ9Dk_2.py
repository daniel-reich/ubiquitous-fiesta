
def hidden_anagram(t,p):
  t,p=list(filter(str.isalpha,t.lower())),list(filter(str.isalpha,p.lower()))
  for i,x in enumerate(t):
    if x in p:
      if sorted(t[i:i+len(p)])==sorted(p):return''.join(t[i:i+len(p)])
  return'noutfond'

