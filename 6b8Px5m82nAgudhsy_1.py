
def next_number(num):
  s=list(str(num))
  i=len(s)-2
  while int(''.join(s))<=num and i>-1:
    if s[i:]==sorted(s[i:],reverse=True):
      i-=1
    else:
      tail=sorted(s[i:])
      s=s[:i] + [tail.pop(tail.index(s[i])+1)] + tail
  return int(''.join(s))

