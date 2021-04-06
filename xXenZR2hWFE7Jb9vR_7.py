
def is_isomorphic(s, t):
  
  if len(s) != len(t):
    return False
  
  converter1 = {}
  converter2 = {}
  
  for n in range(len(s)):
    s_char = s[n]
    t_char = t[n]
    
    if s_char not in converter1.keys():
      converter1[s_char] = t_char
    else:
      if converter1[s_char] != t_char:
        return False
    
    if t_char not in converter2.keys():
      converter2[t_char] = s_char
    else:
      if converter2[t_char] != s_char:
        return False
  
  return True

