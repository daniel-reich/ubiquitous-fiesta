
def true_alphabetic(t):
  s,si,res = sorted(t.replace(' ','')),0,''
  for c in t:
    if c.isalpha():
      res += s[si]
      si += 1
    else:
      res += ' '
  return res

