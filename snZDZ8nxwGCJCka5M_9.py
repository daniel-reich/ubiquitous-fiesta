
def pyramidal_string(s, t):
  p = [0]
  while p[-1] < len(s): p += [p[-1] + len(p)]
  if len(s) not in p: return "Error!"
  if t[-1]=="V": p = [len(s)-i for i in p[::-1]]
  return [" ".join(list(s[a:b])) for a,b in zip(p,p[1:])]

