
def cap_to_front(s):
  lowcase = s.lower()
  caps = ""
  low = ""
  
  for i in range(0, len(s)):
    if s[i] != lowcase[i]:
      caps = caps + s[i]
    else:
      low = low + s[i]
  
  return caps + low

