
def format_ascii(s, width):
  s_new = [] 
  while s:
    new = s[:width]
    s_new.append(new)
    s = s[width:]
​
  s_new = '\n'.join(s_new)
  return(s_new)

